"""独立运行天勤模拟交易；监控端请另外运行 monitor_strategy.py。

使用 notebook 对应的 quant-ml 环境，沿用原策略和退出平仓逻辑。
"""

import argparse
import os
import time
from pathlib import Path

from tqsdk import TargetPosTask
from trading_common import MLTrader, make_api

# 交易接口替换为天勤，日志与 ZeroMQ 发布/订阅流程沿用原书。
import datetime as dt
import pickle

import numpy as np
import pandas as pd
import zmq


def logger_monitor(message, publisher, log_file='automated_strategy.log', time=True, sep=True):
    """同一条消息写入日志文件，并通过 ZeroMQ 发布。"""
    msg = '\n' + str(dt.datetime.now()) + '\n' if time else ''
    if sep:
        msg += 80 * '=' + '\n'
    msg += str(message) + '\n\n'
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(msg)
    publisher.send_string(msg)


class MonitoredMLTrader(MLTrader):
    def __init__(self, algorithm, publisher, log_file, volume=1):
        super().__init__(algorithm, volume)
        self.publisher = publisher
        self.log_file = log_file
        self.recent_inputs = []
        self.bars = 0

    def report_trade(self, event, details):
        """打印、记录并发送目标指令或实际成交；通过 event 区分。"""
        message = f'*** {event} ***\n{details}'
        logger_monitor(message, publisher=self.publisher, log_file=self.log_file)
        print(message)

    def on_bar(self, close, updates=0):
        x = self.prepare_features(close)
        signal = int(self.model.predict(x)[0])
        self.bars += 1
        x.index = [close.index[-1]]                                                          # 本行输入所使用的最后一根已结束 K 线
        self.recent_inputs.append(x)
        self.recent_inputs = self.recent_inputs[-5:]

        logger_monitor(f'QUOTE UPDATES: {updates} | PROCESSED BARS: {self.bars}', publisher=self.publisher, log_file=self.log_file)
        logger_monitor('MOST RECENT INPUTS\n' + pd.concat(self.recent_inputs).to_string(), time=False, publisher=self.publisher, log_file=self.log_file)
        logger_monitor(f'features:\n{x.to_numpy()}\n'
                 f'previous target direction: {self.position}\n'
                 f'signal: {signal}', time=False, publisher=self.publisher, log_file=self.log_file)
        if signal != self.position:
            direction = 'LONG' if signal == 1 else 'SHORT'
            self.report_trade(f'GOING {direction} (TARGET)',
                              {'target_volume': signal * self.volume})
        else:
            logger_monitor('*** NO TRADE PLACED ***', publisher=self.publisher, log_file=self.log_file)
        self.position = signal
        logger_monitor('*** END OF CYCLE ***', time=False, sep=False, publisher=self.publisher, log_file=self.log_file)
        return signal * self.volume


def report_fills(api, trader, seen_trades):
    """读取新成交并报告；原地更新传入的 seen_trades，避免重复报告。"""
    trades = api.get_trade()
    for trade_id, trade in trades.items():
        if trade_id not in seen_trades:
            trader.report_trade('EXECUTED', dict(trade))
            seen_trades.add(trade_id)


def run_monitored(algorithm, stop=150, timeout=60,
                  bind_address='tcp://127.0.0.1:5555',
                  log_file='automated_strategy.log'):
    
    # 1. 创建日志文件和发布端。与原书一致，每次启动重新建立日志。
    with zmq.Context() as context, context.socket(zmq.PUB) as publisher:
        publisher.setsockopt(zmq.LINGER, 0)
        publisher.bind(bind_address)
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write('*** NEW LOG FILE ***\n' + str(dt.datetime.now()) + '\n')
        trader = MonitoredMLTrader(algorithm, publisher, log_file)

        # 2. 连接天勤模拟账户，准备行情及实际合约的目标持仓任务。
        with make_api() as api:
            quote = api.get_quote(trader.instrument)
            klines = api.get_kline_serial(trader.instrument, 
                                          trader.bar_seconds, 
                                          data_length=max(100, trader.window + trader.lags + 1)
                                         )
            deadline = time.time() + timeout
            while not (api.is_serial_ready(klines) and quote.underlying_symbol):
                if not api.wait_update(deadline=deadline):
                    raise TimeoutError('行情初始化超时。')
            contract = quote.underlying_symbol
            target_task = TargetPosTask(api, contract)
            position = api.get_position(contract)
            logger_monitor(f'SIGNAL INSTRUMENT: {trader.instrument} | CONTRACT: {contract}', publisher=publisher, log_file=log_file)
            
            # 不同交易所、账户或系统可能使用相同的编号，只要在各自规定的范围内能区分即可。            
            # 实际成交由天勤异步返回，独立于前面的目标持仓指令。
            seen_trades = set(api.get_trade())  # 跳过启动时已有成交；传参不会复制此集合。
            # 3. 新 K 线结束时记录输入与信号，再设置目标持仓。
            updates = 0
            deadline = time.time() + timeout
            try:
                while updates < stop:
                    if not (api.wait_update(deadline=deadline) and time.time() < deadline):
                        logger_monitor(f'连续 {timeout} 秒无报价更新，结束运行。', publisher=publisher, log_file=log_file)
                        break
                    report_fills(api, trader, seen_trades)
                    if api.is_changing(quote):
                        updates += 1
                        deadline = time.time() + timeout # 有了新的行情，更新deadline，避免空等
                    if api.is_changing(klines.iloc[-1], 'datetime'):
                        target = trader.on_bar(klines.iloc[:-1]['close'], updates)
                        target_task.set_target_volume(target)
                        logger_monitor(f'ACTUAL POSITION: long={position.pos_long}, short={position.pos_short}', publisher=publisher, log_file=log_file)

            # 4. 结束时平仓，记录平仓指令与随后收到的实际成交。
            finally:
                target_task.set_target_volume(0)
                trader.report_trade('GOING NEUTRAL (TARGET)', {'target_volume': 0})
                deadline = time.time() + 30
                while api.wait_update(deadline=deadline):
                    report_fills(api, trader, seen_trades)
                    if position.pos_long == 0 and position.pos_short == 0:
                        trader.position = 0
                        logger_monitor('当前持仓已清空。', publisher=publisher, log_file=log_file)
                        break
                else:
                    logger_monitor(f'平仓确认超时：多 {position.pos_long} 手，空 {position.pos_short} 手。', publisher=publisher, log_file=log_file)


def main():
    parser = argparse.ArgumentParser(description="独立运行天勤模拟交易。Ctrl+C结束时尝试平仓。")
    parser.add_argument("--stop", type=int, default=150, help="累计报价更新次数上限")
    parser.add_argument("--timeout", type=float, default=60, help="连续无报价更新的秒数上限")
    args = parser.parse_args()
    if args.stop <= 0 or args.timeout <= 0:
        parser.error("stop 和 timeout 必须大于0")

    root = Path(__file__).resolve().parent
    os.chdir(root)
    with (root / "algorithm.pkl").open("rb") as f:
        algorithm = pickle.load(f)
    try:
        run_monitored(algorithm, stop=args.stop, timeout=args.timeout)
    except KeyboardInterrupt:
        print("交易端已中断；已进入原有的退出处理流程。", flush=True)


if __name__ == "__main__":
    main()

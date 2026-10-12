#
# Python Script
# with Online Trading Algorithm
#
# Python for Algorithmic Trading
# (c) Dr. Yves J. Hilpisch
# The Python Quants GmbH
#
# 用法: 先启动 TickServer.py，再在另一终端运行
#   python MomentumOnline.py
# 订阅 5555 的 tick，按 5 秒重采样后打印动量做多/做空信号。
# 与 plotly_streaming 画图无关，是书中附录的独立示例。
#
import zmq
import datetime
import numpy as np
import pandas as pd

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://0.0.0.0:5555')
socket.setsockopt_string(zmq.SUBSCRIBE, 'SYMBOL')

df = pd.DataFrame()
mom = 3
min_length = mom + 1

while True:
    data = socket.recv_string()
    t = datetime.datetime.now()
    parts = data.split()  # SYMBOL 日期 时间 价格
    symbol, value = parts[0], float(parts[-1])
    # 收集 tick；pandas 2.0+ 用 concat
    df = pd.concat([df, pd.DataFrame({symbol: value}, index=[t])])
    dr = df.resample('5s', label='right').last()  # 按 5 秒重采样
    dr['returns'] = np.log(dr / dr.shift(1))      # 对数收益率
    if len(dr) > min_length:
        min_length += 1
        # 动量信号：收益率滚动均值的符号，+1 做多 / -1 做空
        dr['momentum'] = np.sign(dr['returns'].rolling(mom).mean())
        print('\n' + '=' * 51)
        print('NEW SIGNAL | {}'.format(datetime.datetime.now()))
        print('=' * 51)
        print(dr.iloc[:-1].tail())
        if dr['momentum'].iloc[-2] == 1.0:
            print('\nLong market position.')
            # take some action (e.g., place buy order)
        elif dr['momentum'].iloc[-2] == -1.0:
            print('\nShort market position.')
            # take some action (e.g., place sell order)

"""在线交易与日志监控 notebook 共用的预测类和天勤模拟连接。"""

import configparser

import numpy as np
import pandas as pd


class MLTrader:
    def __init__(self, algorithm, volume=1):  # 手数可调整，特征参数必须来自训练配置
        self.model = algorithm["model"]
        self.mu, self.std = algorithm["mu"], algorithm["std"]
        self.cols = list(algorithm["cols"])
        self.instrument = algorithm["instrument"]
        self.bar_seconds = algorithm["bar_seconds"]
        self.window, self.lags = algorithm["window"], algorithm["lags"]
        self.momentum_tol = algorithm["momentum_tol"]
        self.volume = volume

        # volatility：波动率；
        # momentum：动量方向。
        # 参数 volume 表示手数，行情列 volume 表示成交量。
        self.features = list(algorithm["features"])
        self.position = 0  # 初始为空仓；此变量记录目标方向，不代表成交已完成

    def prepare_features(self, close):
        """
        在线预测只需要最新一组 36 个特征，无需对整个收盘价序列重复计算。
        书中的写法便于展示完整流程，在数据较少、预测频率较低时，额外开销通常不大。
        本 Notebook 仅保留构造最新预测样本所需的历史：20 根滚动窗口、6 阶滞后，共需最近 26 根已结束 K 线的收盘价。
        """
        needed = self.window + self.lags
        if len(close) < needed:
            raise ValueError(f"至少需要 {needed} 根已结束 K 线。")
        data = pd.DataFrame({"close": close.iloc[-needed:]})
        data["return"] = np.log(data["close"] / data["close"].shift(1))
        data["volatility"] = data["return"].rolling(self.window).std()
        mean_return = data["return"].rolling(self.window).mean()
        # 与训练一致：接近零的均值记为 0，避免浮点误差改变动量方向。
        data["momentum"] = np.sign(
            mean_return.mask(mean_return.abs() <= self.momentum_tol, 0.0)
        )
        data["sma"] = data["close"].rolling(self.window).mean()
        data["min"] = data["close"].rolling(self.window).min()
        data["max"] = data["close"].rolling(self.window).max()

        # 取出每种特征最近 6 个时点的值，并命名，拼成一个字典
        values = {
            f"{feature}_lag_{lag}": data[feature].iloc[-lag]
            for feature in self.features
            for lag in range(1, self.lags + 1)
        }

        x = pd.DataFrame(
            [values], columns=self.cols
        )  # 按训练列顺序排列，形状为 (1, 36)
        x = (x - self.mu) / self.std  # 复用训练统计量
        if not np.isfinite(x.to_numpy()).all():
            raise ValueError("特征含缺失或无穷值，请检查行情和训练标准差。")
        return x

    def on_bar(self, close):  # 一根 K 线结束后调用一次，预测下一根方向
        signal = int(self.model.predict(self.prepare_features(close))[0])
        if signal != self.position:  # 仅在方向变化时打印；方向不变时仍返回相同目标手数
            print(f"NEW SIGNAL: {signal:+d} | 目标持仓 {signal * self.volume:+d} 手")
        self.position = signal
        return signal * self.volume


def make_api():
    """创建天勤模拟连接；调用时才读取配置并加载 SDK。"""
    from tqsdk import TqApi, TqAuth, TqSim

    config = configparser.ConfigParser()
    config.read("tqsdk.cfg", encoding="utf-8")  # 从同目录读取天勤认证配置
    return TqApi(
        account=TqSim(init_balance=100_000),  # 本地模拟账户，初始资金 10 万元
        auth=TqAuth(
            config.get("tqsdk", "user"), config.get("tqsdk", "password")
        ),  # 行情认证
        disable_print=True,
    )

"""独立消息监控端；请与 run_trading.py 分别启动。"""

import argparse
import zmq


def monitor_strategy(address="tcp://127.0.0.1:5555", timeout=60):
    """接收并打印消息；连续 timeout 秒没有消息就退出，不控制交易。"""
    with zmq.Context() as context, context.socket(zmq.SUB) as subscriber:
        subscriber.setsockopt(zmq.LINGER, 0)
        subscriber.setsockopt_string(zmq.SUBSCRIBE, "")
        subscriber.connect(address)
        print(f"监控端已启动，等待 {address} 的消息。", flush=True)
        while subscriber.poll(timeout=int(timeout * 1000)):
            print(subscriber.recv_string(), flush=True)
        print(f"连续 {timeout} 秒未收到消息，结束监控。", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--address", default="tcp://127.0.0.1:5555")
    parser.add_argument("--timeout", type=float, default=60)
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("timeout 必须大于0")
    try:
        monitor_strategy(args.address, args.timeout)
    except KeyboardInterrupt:
        print("监控端已停止。", flush=True)


if __name__ == "__main__":
    main()

import time

from src.tradingeconomics import macro_report

if __name__ == '__main__':
    start = time.time()
    macro_report()
    # google_trends_report()
    print(time.time() - start)

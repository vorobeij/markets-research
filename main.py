import time

from src.google_trends_report import google_trends_report
from src.tradingeconomics import tradingeconomics_report

if __name__ == '__main__':
    start = time.time()
    tradingeconomics_report()
    google_trends_report()
    print(time.time() - start)

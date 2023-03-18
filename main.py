import time

from src.crypto_report import crypto_report
from src.google_trends_report import google_trends_report

if __name__ == '__main__':
    start = time.time()
    # macro_report()
    # google_trends_report()
    crypto_report()
    print("\nDone in ms:")
    print(time.time() - start)

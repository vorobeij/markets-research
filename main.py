import time

from src.btc import btc
from src.nasdaq import spx

if __name__ == '__main__':
    start = time.time()
    spx()
    btc()
    print(time.time() - start)

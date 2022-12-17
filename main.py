import time

from src.btc import btc
from src.nasdaq import nsdq

if __name__ == '__main__':
    start = time.time()
    nsdq()
    btc()
    print(time.time() - start)

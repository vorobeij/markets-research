import time

from src.btc import btc
from src.macro import macro
from src.nasdaq import nsdq

if __name__ == '__main__':
    start = time.time()
    nsdq()
    macro()
    btc()
    print(time.time() - start)

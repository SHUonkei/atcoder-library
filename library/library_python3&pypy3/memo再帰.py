# 2. lrucache
from functools import lru_cache
@lru_cache(maxsize=None)
def fib2(i):
    if i == 0 or i == 1:
        return 1
    return fib2(i-1) + fib2(i-2)
n = int(input())
an = fib2(n)
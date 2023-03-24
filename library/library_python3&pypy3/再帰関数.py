from functools import lru_cache

import sys
sys.setrecursionlimit(10**7) # 再起回数の設定

@lru_cache
def f(n):
    if n == 0:
        return 1
    return f(n // 2) + f(n // 3)


print(f(int(input())))


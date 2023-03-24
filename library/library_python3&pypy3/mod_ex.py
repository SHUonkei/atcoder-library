#逆元求める時,素数じゃないけど互いに素

def modinv(a, b):
    p = b
    x, y, u, v = 1, 0, 0, 1
    while b:
        k = a // b
        x -= k * u
        y -= k * v
        x, u = u, x
        y, v = v, y
        a, b = b, a % b
    x %= p
    if x < 0:
        x += p
    return x

#拡張ユークリッド

def extGCD(a,b):
    x, y, u, v = 1, 0, 0, 1
    while b:
        k = a // b
        x -= k * u
        y -= k * v
        x, u = u, x
        y, v = v, y
        a, b = b, a % b
    return x, y



mod = 10 ** 9 +7
'''
逆元求める時
'''
#pow(x,mod-2,mod)

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)


n  = 10
r  = 5 

print(cmb(n, r, p))

"最小公倍数をTLEしないで求める"

n = int(input())
a = list(map(int,input().split()))
mod = 10**9 +7
from math import gcd

#TLE避けるのがむずい。。。
#最小公倍数で落ちてるはずなんだが。。。


from collections import defaultdict
res = defaultdict(int)
def prime_factors(n,res0):
    res = defaultdict(int)
    i = 2
    while i * i <= n:
        while n % i == 0:
            n = n // i
            res[i] += 1
        i += 1
    if n > 1:
        res[n] += 1
    for i in res.keys():
        res0[i] = max(res0[i],res[i])
    return res0


for i in range(n):
    res = prime_factors(a[i],res)

now = 1
for i in res.keys():
    now *= pow(i,res[i],mod)
    now %= mod
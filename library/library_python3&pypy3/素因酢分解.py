
from collections import defaultdict
def prime_factors(n):
    res = defaultdict(int)
    i = 2
    while i * i <= n:
        while n % i == 0:
            n = n // i
            res[i] += 1
        i += 1
    if n > 1:
        res[n] += 1
    return res

import itertools
import collections
def prime_factor_table(n):
    table = [0] * (n + 1)
    
    for i in range(2, n + 1):
        if table[i] == 0:
            for j in range(i + i, n + 1, i):
                table[j] = i
    
    return table

def prime_factor(n, prime_factor_table):
    prime_count = collections.Counter()
    
    while prime_factor_table[n] != 0:
        prime_count[prime_factor_table[n]] += 1
        n /= prime_factor_table[n]
    prime_count[n] += 1
    
    return prime_count

#素数判定O(1) 前処理O(nlognlogn) 
# O(NloglogN)
def eratosthenes_sieve(n):
    is_prime = [True]*(n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, n + 1):
        if is_prime[p]:
            for q in range(2*p, n + 1, p):
                is_prime[q] = False
    return is_prime


def Eratosthenes_num(N):#約数の個数を列挙？
    # テーブル
    isprime = [2] * (N+1)
    isprime[1] = 1

    # ふるい
    for p in range(2, N+1):
        # p 以外の p の倍数から素数ラベルを剥奪
        q = p * 2
        while q <= N:
            isprime[q] += 1
            q += p
    
    return isprime

print(Eratosthenes_num(50))



def Eratosthenes(N):#約数列挙
    # テーブル
    isprime = [2] * (N+1)
    isprime[1] = 1

    # ふるい
    for p in range(2, N+1):
        # p 以外の p の倍数から素数ラベルを剥奪
        if isprime[p] == 2:
            q = p * 2
            while q <= N:
                isprime[q] = p
                q += p
    
    return isprime





#N回高速素因数分解前処理NloglogN
#クエリ処理 logN

MAXN = 10**6+10#ここの値は適宜かえる
sieve = [i for i in range(MAXN+1)]
p = 2
while p*p <= MAXN:
    if sieve[p] == p:
        for q in range(2*p,MAXN+1,p):
            if sieve[q] == q:
                sieve[q] = p
    p += 1

#その数を最初で割り切る素数を持っとくと、sieveで破りまくってれば高速で素因数分解可能
from collections import defaultdict
def fac(a):
    tmp = defaultdict(int)
    while a > 1:
        tmp[sieve[a]]+=1
        a //= sieve[a]
    return tmp
"""""
for n in range(N):   # ベンチマーク用
    prime_factors(n)
"""""
print(prime_factors(3))


"nいかの最大の素数p"
H,A = map(int,input().split())

from collections import defaultdict
def prime_factors(n):
    res = defaultdict(int)
    i = 2
    while i * i <= n:
        while n % i == 0:
            n = n // i
            res[i] += 1
        i += 1
    if n > 1:
        res[n] += 1
    return res

for i in reversed(range(A+1)):
    l = prime_factors(i)
#    print(l)
    c = 0
    c2 = 0
    flag = False
    if len(l) != 1:
        continue
    for i in l.keys():
        if l[i] == 1:
            c += 1
    if c == 1:
        p = i
        break



"2,3で割る回数,nから2,3を除いたやつ"
def f(n):
    c2 = 0
    c3 = 0
    while n%2 == 0:
        n = n//2
        c2 += 1
    while n%3 == 0:
        n = n//3
        c3 += 1
    
    return (c2,c3,n//((2**c2)*(3**c3)))

#ミラーラビン
from math import gcd
def isprime(n):
    if n <= 2:
        return n == 2
    if n % 2 == 0:
        return False
    s = 0
    t = n - 1
    while t % 2 == 0:
        s += 1
        t //= 2
    
    for a in [2,3,325,9375,28178,450775,9780504,1795265022]:
        if a >= n:
            break
        x = pow(a, t, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s):
            x = (x * x) % n
            if x == n - 1:
                break
        if x == n - 1:
            continue

        return False
    return True

def Pollad(N):
    if N % 2 == 0:
        return 2
    if isprime(N):
        return N
    def f(x):
        return (x * x + 1) % N
    step = 0

    while True:
        step += 1
        x = step
        y = f(x)
        while True:
            p = gcd(y - x + N, N)
            if p == 0 or p == N:
                break
            if p != 1:
                return p
            x = f(x)
            y = f(f(y))


def Primefact(N):
    if N == 1:
        return []
    q = []
    q.append(N)
    ret = []
    while q:
        now = q.pop()
        if now == 1:
            continue
        p = Pollad(now)
        if p == now:
            ret.append(p)
        else:
            q.append(p)
            q.append(now // p)

    return ret

import sys
from collections import deque, Counter
sys.setrecursionlimit(5 * 10 ** 5)
from pypyjit import set_param
set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353

n = ii()

for _ in range(n):
    x = ii()
    print(x, int(isprime(x)))

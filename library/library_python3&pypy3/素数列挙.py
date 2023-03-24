def primes(n):
    sieve = [True] * ((n + 1) // 2)
    for i in range(1, (int(n ** 0.5) + 1) // 2):
        if sieve[i]:
            for j in range(i * 3 + 1, (n + 1) // 2, i * 2 + 1):
                sieve[j] = False
    res = [i * 2 + 1 for i, s in enumerate(sieve) if s]
    res[0] = 2
    return res
print(primes(10))

def Eratosthenes(N):
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

n = 5

#エラとす
ls = [1] * (n + 1)
ls[:2] = [0, 0]
for i in range(2, n):
  if ls[i] == 0:
    continue
  for j in range(i**2, n+1, i):
    ls[j] = 0
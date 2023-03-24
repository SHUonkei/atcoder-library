def divisors(n):
    res_low, res_high = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            res_low.append(i)
            if i != n // i:
                res_high.append(n // i)
        i += 1
    return res_low + res_high[::-1]
"""""
for n in range(N):   # ベンチマーク用
    divisors(n)
"""""
print(divisors(12))
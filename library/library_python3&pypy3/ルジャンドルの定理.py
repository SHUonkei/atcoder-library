# n! は p で何回割り切れるか（ルジャンドルの定理）
def legendre(n, p):
    res = 0
    p2 = p
    while True:
        tmp = n // p2
        if tmp == 0:
            break
        res += tmp
        p2 *= p
    return res
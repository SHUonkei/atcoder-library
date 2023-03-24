N = int(input())
now = 0
for i in range(N):
    t,a = input().split()
    if t == "+":
        now += int(a)%(10**4)
    elif t == "-":
        now -= int(a)%(10**4)
    elif t == "*":
        now *= int(a)%(10**4)
    now = now%(10**4)
    print(now)

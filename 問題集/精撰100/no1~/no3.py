s = input()
c = []
now = 0
c.append(0)
ok = ("A","T","G","C")
while True:
    if now >= len(s):
        break
    if not s[now] in ok:
        now += 1
        continue
    n = now
    while n < len(s) and s[n] in ok:
        n += 1
    c.append(n - 1 - (now - 1))
    now = n
print(max(c))
n,c = map(int,input().split())
t,a = map(int,input().split())
def func(t,a,b):
    if t == 1:
        return a&b
    if t == 2:
        return a|b
    if t == 3:
        return a^b
now = a
bf = func(t,c,a)
st = t
print(func(t,c,a))
    
for i in range(n-1):
    t,a = map(int,input().split())
    if t == 1:
        now &= a
    if t == 2:
        now |= a
    if t == 3:
        now ^= a
    print(func(st,bf,now))
    bf = func(st,bf,now)

print(9^3)
print((9^3)|5)
print(9^(3|5))

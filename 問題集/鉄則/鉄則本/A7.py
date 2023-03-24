D = int(input())
N = int(input())

d = [0]*D

for i in range(N):
    l,r = map(int,input().split())
    d[l-1] += 1
    if r <D:
        d[r] -= 1
#print(d)
s = 0
for i in range(D):
    s += d[i]
    print(s)
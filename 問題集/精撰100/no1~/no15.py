import math
import itertools

def dis(x,y,s,t):
    D = (x-s)**2 + (y-t)**2
    return math.sqrt(D)

def perm(n, r):
    return math.factorial(n) // math.factorial(n - r)


N = int(input())
xy = [list(map(int,input().split())) for _ in range(N)]

l = []
for i in range(N):
    l.append(i)

p = itertools.permutations(l,N)

sum = 0
for i in p:
    for j in range(N-1):
        n = i[j]
        m = i[j+1]
        d = dis(xy[n][0],xy[n][1],xy[m][0],xy[m][1])
        sum += d

print(sum/perm(N,N))
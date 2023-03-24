N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
#tuple 使えるように
import itertools

l = []
for i in range(1,N+1):
    l.append(i)
    
p = itertools.permutations(l,N)
p = list(p)

for i in range(len(p)):
    if P == p[i]:
        a = i
    if Q == p[i]:
        b = i

#print(p)

print(abs(a-b))
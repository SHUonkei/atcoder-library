n = int(input())
A = []
B = []
d = []
from heapq import *
for i in range(n):
    a,b= map(int,input().split())
    A.append(a)
    B.append(b)
    delta = b-a
    heappush(d,(delta,-a,i))

s = 0
for i in range(n):
    x = heappop(d)
    x
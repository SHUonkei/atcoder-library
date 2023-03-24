Q = int(input())

from collections import deque

q = deque()
for i in range(Q):
    query = list(map(str,input().split()))
    if query[0] == "1":
        q.append(query[1])
    if query[0] == "2":
        print(q[len(q)-1])
    if query[0] == "3":
        q.pop()

from collections import deque

Q = int(input())

q = deque()
for i in range(Q):
    query = list(map(str,input().split()))
    
    if query[0] == "1":
        q.append(query[1])
    if query[0] == "2":
        print(q[0])
    if query[0] == "3":
        q.popleft()
import heapq

Q = int(input())

q = []
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        heapq.heappush(q,query[1])
    if query[0] == 2:
        print(q[0])
    if query[0] == 3:
        heapq.heappop(q)
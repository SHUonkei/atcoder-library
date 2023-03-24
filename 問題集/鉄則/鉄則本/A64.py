N,M = map(int, input().split())
e = [[] for _ in range(N+1)]

for i in range(M):
    a,b,c = map(int, input().split())
    e[a].append([b,c])
    e[b].append([a,c])

def dijkstra(G,r):
    import heapq
    cur = [float("inf")]*len(G)
    que = []
    cur [r] = 0
    heapq.heappush(que,(0,r))
    
    while len(que)>0:
        c,v = heapq.heappop(que)
        if cur[v] <  c:
            continue
        for u, cost in G[v]:
            if cur[u] < c + cost:
                continue
            cur[u] = c + cost
            heapq.heappush(que,((c+cost),u))
    return cur

data = dijkstra(e,1)

for i in range(1,N+1):
    if not data[i] == float("inf"):
        print(data[i])
    else:
        print(-1)
    
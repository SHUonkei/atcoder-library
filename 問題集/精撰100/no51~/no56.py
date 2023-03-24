V,E,r = map(int, input().split())
std = [list(map(int, input().split())) for _ in range(E)]
e = []*V
for i in range(E):
    u,v = std[i]
    e[u-1].append(v-1)   
    e[v-1].append(u-1)



def dijkstra(G,s):
    import heapq
    cur = [[float("inf")]*V]
    
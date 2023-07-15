n,m = map(int,input().split())
G = [[[]for _ in range(n)] for _ in range(3)]
for i in range(m):
    u,v=  map(int,input().split())
    G[0][u-1].append((v-1,1))
    G[1][u-1].append((v-1,2))
    G[2][u-1].append((v-1,0))

s,t= map(int,input().split())
s-=1
t -=1
from collections import deque

d = deque()
d.append((s,0))
# d.append((s,1))
# d.append((s,2))

vis = [[-1]*n for _ in range(3)]
vis[0][s] = 0
# vis[1][s] = 0
# vis[2][s] = 0
while d:
    x,mod = d.popleft()
    for i,mm in G[mod][x]:
        if vis[mm][i] >= 0:
            continue
        vis[mm][i] = vis[mod][x] +1
        d.append((i,mm))

if vis[0][t] == -1:
    print(-1)
    exit()
print(vis[0][t]//3)
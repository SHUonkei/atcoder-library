from collections import deque

H, W = map(int, input().split())
che = [list(input()) for _ in range(H)]
c=0

for i in range(H):
    for j in range(W):
        if che[i][j] == ".":
            c += 1


dy = [1,0,-1,0]
dx = [0,1,0,-1]
ans = 0


def bfs(sy,sx,gy,gx):
    Q = deque()
    Q.append([sy,sx])
    dist = [[-1]*(W) for _ in range(H)]
    dist[sy][sx] = 0
    while len(Q)>0:
        z = Q.popleft()
        if che[z[0]][z[1]] == "#":
            continue
        for i in range(4):
            u = z[0]+dy[i]
            v = z[1]+dx[i]
            if 0 <= u < H and 0<= v < W and dist[u][v]==-1:#dist[u][v]でout of rangeになるときありそう
                dist[u][v] = dist[z[0]][z[1]]+1
                Q.append([u,v])
    global ans
    ans = dist[gy][gx]

bfs(0,0,H-1,W-1)
if ans == -1:
    print(-1)
    exit()
print(c-ans-1)
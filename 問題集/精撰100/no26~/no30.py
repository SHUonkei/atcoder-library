from collections import deque

H, W, N = map(int, input().split())
che = [list(input()) for _ in range(H)]

data = []
for i in range(H):
    for j in range(W):
        if che[i][j] == "S":
            data.append([i,j])

for n in range(N):
    for i in range(H):
        for j in range(W):
            if che[i][j] == str(n+1):
                data.append([i,j]) 

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
        if che[z[0]][z[1]] == "X":
            continue
        for i in range(4):
            u = z[0]+dy[i]
            v = z[1]+dx[i]
            if 0 <= u < H and 0<= v < W and dist[u][v]==-1:
                dist[u][v] = dist[z[0]][z[1]]+1
                Q.append([u,v])
    global ans
    ans += dist[gy][gx]
    che[gy][gx] == "."

for i in range(len(data)-1):
    bfs(data[i][0],data[i][1],data[i+1][0],data[i+1][1])
print(ans)
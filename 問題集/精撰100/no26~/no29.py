from collections import deque

R,C = map(int, input().split())
sy,sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [list(str(input())) for _ in range(R)]#入力マジ気をつける


dy = [1,0,-1,0]
dx = [0,1,0,-1]

Q = deque()
Q.append([sy-1,sx-1])
dist = [[-1]*(C) for _ in range(R)]
dist[sy-1][sx-1] = 0#c とdistは位置を一致させるQは1インデックス

while len(Q)>0:

    z = Q.popleft()

#壁とかかどうか判定
    if c[z[0]][z[1]] == "#":
        continue
#    if dist[z[0]][z[1]] == -1:
    for i in range(4):
        u = z[0]+dy[i]
        v = z[1]+dx[i]
        if 0 <= u < R and 0<= v < C:
            if dist[u][v]==-1 and c[u][v] == ".":
                dist[u][v] = dist[z[0]][z[1]]+1
                if 0 <= u < R and 0<= v < C:
                    Q.append([u,v])

print(dist[gy-1][gx-1])
#一回行ったかどうかとかその辺判定

#行ってなかったらdist(x)+1
#Qにappend
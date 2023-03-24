import sys
sys.setrecursionlimit(10**8) # 再起回数の設定

M = int(input())
N = int(input())
Area = [list(map(int, input().split())) for _ in range(N)]
X = Area
data = []

for i in range(N):
    for j in range(M):
        Area = X
        if Area[i][j] == 1:
            def dfs(x,y,now): 
                if x<0 or x>=N or y<0 or y>= M or Area[x][y] == 0:
                    return
                now += 1
                Area[x][y] = 0
                c = 0
                dx = [1,-1,0,0]
                dy = [0,0,1,-1]
                d = []
                u_1 = []
                u_2 = []
                for k in range(4):
                    if not (x+dx[k]<0 or x+dx[k]>=N or y+dy[k]<0 or y+dy[k]>= M):
                        d.append(k)
                for k in range(len(d)):
                    u_1.append(dx[d[k]])
                    u_2.append(dy[d[k]])
                for k in range(len(d)):
                    if Area[x+u_1[k]][y+u_2[k]] == 1:
                        c = 1
                        break
                if c == 0:
                    count = now
                    data.append(count)
                if c == 1:
                    dfs(x+1,y,now)
                    dfs(x-1,y,now)
                    dfs(x,y+1,now)
                    dfs(x,y-1,now)
                Area[x][y] = 1
            dfs(i,j,0)

print(max(data))
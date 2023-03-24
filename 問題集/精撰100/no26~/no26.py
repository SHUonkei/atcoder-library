import sys
sys.setrecursionlimit(10**8) # 再起回数の設定

N , Q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N-1)]
px = [list(map(int, input().split())) for _ in range(Q)]

data = [[] for _ in range(N)]


for i in range(N-1):#木構造をわかりやすいデータに
    a = ab[i][0]-1
    b = ab[i][1]-1
    data[a].append(b)
    data[b].append(a)

data_s = [0]*N

for i in range(Q):
    p = px[i][0] - 1 #0インデックスに 
    data_s[p] += px[i][1]#サンプル２のように二重に来た時に対応するために+=にしている

vis = [0]*N
ans = [0]*N

def dfs(x,y):
    ans[x] = y
    ans[x] += data_s[x]
    vis[x] = 1
#    print(ans,vis)
    for j in range(len(data[x])):
        if vis[data[x][j]] != 1:
            dfs(data[x][j],ans[x]) 
dfs(0,0)
print(*ans)
import sys
sys.setrecursionlimit(10**8) # 再起回数の設定

N,M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]
e = [[] for _ in range(N+1)]

for i in range(M):
    u,v = ab[i]
    e[u].append(v)
    e[v].append(u)

#print(e)

vis = [-1]*(N+1)
def dfs(x):
    vis[x] = 0
    for i in e[x]:
        if vis[i] == -1:
            #vis[i] = 0 ここだとdfsしないときに　一回めとか　ではげ　0にならない
            dfs(i)


dfs(1)

#print(vis)
for i in range(1,N+1):
    if vis[i] == -1:
        print("The graph is not connected.")
        exit()

print("The graph is connected.")

"""""
再起回数の設定
0インデックスにする
vis = -1 にするたいみんぐ
"""""
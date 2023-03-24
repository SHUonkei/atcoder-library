import sys
sys.setrecursionlimit(10**7) # 再起回数の設定

H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        if maze[h][w] == "s":
            sx, sy = h, w

# 深さ優先探索
def dfs(x, y):
    # 範囲外や壁の場合は終了
    if y >= W or y < 0 or x >= H or x < 0 or maze[x][y] == '#':
        return

    # ゴールに辿り着ければ終了
    if maze[x][y] == 'g':
        print('Yes')
        exit()

    maze[x][y] = '#' # 確認したルートは壁にしておく

    # 上下左右への移動パターンで再起していく
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

dfs(sx, sy) # スタート位置から深さ優先探索
print('No')


"""
連結グラフの個数カウント
"""
import sys
sys.setrecursionlimit(10**7) # 再起回数の設定

N,M = map(int, input().split())
ab = [list(map(int ,input().split())) for _ in range(M)]
e = [[] for _ in range(N)]

for i in range(M):
    u,v = ab[i]
    e[u-1].append(v-1)
    e[v-1].append(u-1)

vis = [False]*(N)

def dfs(x):
    vis[x] = True
    for i in e[x]:
        if vis[i]:
            continue
        dfs(i)

c = 0
l = set()
for i in range(N):
    if vis[i]:
        continue
    c += 1
    dfs(i)

print(c-1)


"""
dfsのパス復元 XからY なおこれは木
"""

import sys
sys.setrecursionlimit(10**7) # 再起回数の設定
N,X,Y = map(int,input().split())
data = [[] for _ in range(N)]
for i in range(N-1):
    u,v = map(int,input().split())
    data[u-1].append(v-1)
    data[v-1].append(u-1)

from collections import deque
l = deque()
l.append(X)
vis = [False]*(N)
def dfs(x):#0インデックス！
    vis[x] = True
    if x+1 == Y:
        print(*l)
        exit()
    for i in range(len(data[x])):
        if vis[data[x][i]] == True:
            continue
        l.append(data[x][i]+1)
        dfs(data[x][i])
        l.pop()

dfs(X-1)

"""
スタート地点に戻ってくる時
"""

import sys
sys.setrecursionlimit(10**7) # 再起回数の設定

H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        if maze[h][w] == "S":
            sx, sy = h, w


# 深さ優先探索
def dfs(x, y, flag):
    # 範囲外や壁の場合は終了
    if y >= W or y < 0 or x >= H or x < 0 or maze[x][y] == '#':
        return
    if flag == 2 and (x,y) == (sx,sy):
        return

    # ゴールに辿り着ければ終了
    if flag == 0:
        if maze[x][y] == 'S':
            print('Yes')
            exit()
    if flag != 1:
        maze[x][y] = '#' # 確認したルートは壁にしておく

    if flag == 1:
        dfs(x+1, y,2)
        dfs(x-1, y,2)
        dfs(x, y+1,2)
        dfs(x, y-1,2)
        return
    if flag == 2:
        if (x+1,y) != (sx,sy):
            dfs(x+1, y,0)
        if (x-1,y) != (sx,sy):
            dfs(x-1, y,0)
        if (x,y+1) != (sx,sy):
            dfs(x, y+1,0)
        if (x,y-1) != (sx,sy):
            dfs(x, y-1,0)
        return

    # 上下左右への移動パターンで再起していく
    dfs(x+1, y,0)
    dfs(x-1, y,0)
    dfs(x, y+1,0)
    dfs(x, y-1,0)

dfs(sx, sy,1) # スタート位置から深さ優先探索
print('No')

"非再帰実装"
from collections import defaultdict
N,M = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    u,v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

stack = []
stack.append(1)
visited = defaultdict(int)
ans = 0

while len(stack) > 0:
    pos = stack.pop()
    
    if pos > 0:
        
        visited[pos] = 1
        ans += 1
        
        for nx in G[pos]:
            if visited[nx] == 0:
                stack.append(~nx)
                stack.append(nx)
    
    if pos < 0:
        pos = ~pos
        visited[pos] = 0

print(ans)
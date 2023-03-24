#キューをインポート
from collections import deque

N,M = map(int ,input().split())
ab = [list(map(int, input().split())) for _ in range(M)]
e = [[] for _ in range(N)]

for i in range(M):
    u,v = ab[i]
    e[u-1].append(v-1)
    e[v-1].append(u-1)
""""
#キューを作って、スタート地点を追加
訪問時　先頭なのでキューから取り出せる。
"""""
Q = deque() #その時点での橙色頂点 (発見済みだが未訪問な頂点) を格納するキュー?
Q.append(0)
dist = [-1 for _ in range(N)]
dist[0] = 0
""""
dist[v] はスタート頂点から頂点 v まで何ステップで到達できるかを表す
配列 dist は初期状態として -1 に初期化しておくことで、「その頂点が発見済みかどうか」も同時に管理することができます。すなわち
dist[v] == -1
と
v は白色頂点である
が同値であるということになります。
"""""
while len(Q)>0:
    x = deque.popleft(Q)
    for i in e[x]:
        if dist[i] != -1:
            continue
        dist[i] = dist[x] + 1
        Q.append(i)


for i in range(N):
    print(dist[i])
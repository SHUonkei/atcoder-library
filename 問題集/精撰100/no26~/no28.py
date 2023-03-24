#キューをインポート
from collections import deque

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

""""
#キューをQにいれ、スタート地点を追加
訪問時　先頭なのでキューから取り出せる。
"""""

Q = deque() #その時点での橙色頂点 (発見済みだが未訪問な頂点) を格納するキュー?
Q.append(1)

""""
dist[v] はスタート頂点から頂点 v まで何ステップで到達できるかを表す

配列 dist は初期状態として -1 に初期化しておくことで、「その頂点が発見済みかどうか」も同時に管理することができます。すなわち

dist[v] == -1
と
v は白色頂点である

が同値であるということになります。
"""""

dist = [-1]*(N+1)
dist[0] = 0

while len(Q) > 0:
#    print(Q,dist)
    x = Q.popleft()#先頭取り出す
#    print(Q,dist)
    for i in range(2,len(data[x-1])):
        if dist[data[x-1][i]-1] == -1:
            dist[data[x-1][i]-1] = dist[x-1]+1
            Q.append(data[x-1][i])
#    print(Q,dist)

for i in range(N):        
    print(i+1, dist[i])
"また、移動におけるコストが "
"0 と 1 だけの場合は、01-BFSと呼ばれる実装が可能となります。"
"dequeを使用し、コストが "
"0 の移動先の頂点はdequeの先頭に、コストが "
"1 の移動先の頂点はdequeの末尾に追加することで、"
"距離順に探索をすることが可能となります。"
"ただし、コスト 1 で追加された頂点がその後コスト"
"0 の移動のみで追加された際、"
"2 回同じ頂点が追加されることになるため、その点の実装に注意してください。"


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
    
"迷路系"
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
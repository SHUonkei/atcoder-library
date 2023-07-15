#gridのdijkstra
n,V,ox,oy = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]
def Dijkstra(L,r,h,w):#1インデックス
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    """
    e:隣接リスト
    （隣接する頂点,重さ）
    ダイクストラ法。
    rから各頂点への最短コスト。
    O(ElogV)
    rはタプル
    """
    import heapq
    cur = [[float('inf')]*(w+1) for _ in range(h+1)]
    cur[r[0]][r[1]] = 0#rが初期位置
    que = []
    """""
    cur は　暫定の距離
    que は　未確定頂点の番号とcur(仮)のセットのタプルのリスト
    """""
    heapq.heappush(que,(0,r))#入れる

    while len(que) != 0:
        c,n = heapq.heappop(que)#未確定頂点のなかの最小値取り出して取得　nが重複している場合も全然ある
        if cur[n[0]][n[1]] < c:#cur のあたいがすでにかくていした頂点の場合（？？？未確定頂点からみたときにcurより小さいなら更新される
            continue
        for i in range(4):
            v = n[0]+dy[i]
            u = n[1]+dx[i]
            if 0<v<=h and 0<u<=w:
                cost = L[v-1][u-1]
            else:
                continue
            if cur[v][u] <= c+cost:#i[0]はノード、i[1]は重み
                continue
            heapq.heappush(que,(c+cost,(v,u)))#入れる そこまでの重みを先頭ということに注意
            cur[v][u] = min(cur[v][u],c+cost)#cur[i[0]] = c+i[1]でよくない？
    return cur

if ox == 0 and oy == 0:
    cur = Dijkstra(L,(1,1),n,n)
    if cur[n][n] < V:
        print("YES")
        exit()
    print("NO")
    exit()

cur1 = Dijkstra(L,(oy,ox),n,n)
now = (V-cur1[1][1]+L[0][0]-L[oy-1][ox-1])*2 - cur1[n][n]

if now > 0:
    print("YES")
    exit()

cur = Dijkstra(L,(1,1),n,n)
if cur[n][n] < V:
    print("YES")
    exit()

print("NO")









"経路復元機能付きdijkstra"
#e:隣接リスト
N,M = map(int,input().split())
e = [[] for i in range(N)] 
prev = [-1] * len(e) 
INF = 10**18
def dijkstra(G,r):
    import heapq
    cur = [INF]*len(G)
    que = []
    cur [r] = 0
    heapq.heappush(que,(0,r))
    
    while len(que)>0:
        c,v = heapq.heappop(que)
        if cur[v] <  c:
            continue
        for u, cost in G[v]:
            if cur[u] <= c + cost:
                continue
            cur[u] = c + cost
            heapq.heappush(que,((c+cost),u))
            prev[u] = v
    return cur

for i in range(M):
    u,v,c = map(int,input().split())
    e[u-1].append((v-1,c))
    e[v-1].append((u-1,c))

ans = dijkstra(e,0)

def get_path(t):
    path = []
    while t != -1:
        path.append(t+1) #0インデックスなので   # tがsになるまでprev[t]を辿っていく
        t = prev[t]
    # このままだとt->sの順になっているので逆順にする
    path.reverse()
    return path








#momoyuu


#e:隣接リスト
def Dijkstra(e,r):
    """
    e:隣接リスト
    （隣接する頂点,重さ）
    ダイクストラ法。
    rから各頂点への最短コスト。
    O(ElogV)っぽい。
    """
    import heapq
    cur = [float('inf') for _ in range(len(e))]
    cur[r] = 0#rが初期位置
    que = []
    """""
    cur は　暫定の距離
    que は　未確定頂点の番号とcur(仮)のセットのタプルのリスト
    """""
    heapq.heappush(que,(0,r))#入れる

    while len(que) != 0:
        c,n = heapq.heappop(que)#未確定頂点のなかの最小値取り出して取得　nが重複している場合も全然ある
        if cur[n] < c:#cur のあたいがすでにかくていした頂点の場合（？？？未確定頂点からみたときにcurより小さいなら更新される
            continue
        for t,cost in e[n]:#更新されるとそこから伸びてるノードについて見る
            if cur[t] <= c+cost:#i[0]はノード、i[1]は重み
                continue
            heapq.heappush(que,(c+cost,t))#入れる そこまでの重みを先頭ということに注意
            cur[t] = min(cur[t],c+cost)#cur[i[0]] = c+i[1]でよくない？
    return cur

    """"""""""""""
    #cur[0] = float("inf")　#であることに注意。
    """"""""""""""










INF = float('inf')

prev = []

V, E = map(int,input().split())    # Vは頂点数、Eは辺数
cost = [[INF] * V for _ in range(V)]    # cost[u][v]は辺e=(u,v)のコスト(存在しない場所はINF)
for _ in range(E):
    s, t, c = map(int,input().split())
    cost[s][t] = c
    cost[t][s] = c

"経路復元"
d = [INF for _ in range(V)]    # 最短距離
used = [False] * V    # すでに使われたかのフラグ
prev = [-1] * V    # 最短路の直前の頂点

# 始点sから各頂点への最短距離を求める
def dijkstra(s):
    d[s] = 0
    
    while True:
        v = -1
        for u in range(V):
            if not used[u] and (v == -1 or d[u] < d[v]):
                v = u
        
        if v == -1:
            break
        used[v] = True
        
        for u in range(V):
            if d[u] > d[v] + cost[v][u]:
                d[u] = d[v] + cost[v][u]
                prev[u] = v

# 頂点tへの最短路
def get_path(t):
    path = []
    while t != -1:
        path.append(t)    # tがsになるまでprev[t]を辿っていく
        t = prev[t]
    # このままだとt->sの順になっているので逆順にする
    path.reverse()
    return path

dijkstra(0)    # 頂点0を始点とする

path = get_path(6)    # 頂点0から頂点6への最短経路

print(path)
#部分木の大きさをdp配列に保存している！！
n = int(input())
# sum to deltas
e = [set() for _ in range(n+1)]
from collections import defaultdict
d = []
for _ in range(n-1):
    u,v = map(int,input().split())
    
    e[u-1].add((1,v-1))
    e[v-1].add((1,u-1))
    d.append((u-1,v-1,1))

def EulerTour(n,X,i0):#i0から始まる
    vis = [-1 for _ in range(n)]
    par = [0]*n
    par[0] = -1
    Q = [(~i0,0),(i0,-1)] #根をスタックに追加
    ET = []
    while Q:
        i,now = Q.pop()
        if i >= 0: #0以上つまり、行きがけの処理
            vis[i] = now + 1
#            ET.append(i) #
            for c, a in X[i]:
                if vis[a] >= 0:
                    continue
                par[a] = i
                Q.append((~a,0)) #帰りがけの処理をスタックに追加
                Q.append((a,vis[i])) #行きがけの処理をスタックに追加
        else: #0より小さい帰りがけの処理
            ET.append(~i)#-を+になおす
    return ET,vis,par
#帰りがけの処理だけにした

et,vis,par = EulerTour(n,e,0)

dp = [1 for _ in range(n)]#サイズ
for i in range(len(et)-1):#最後のpar[0] = -1だからおかしくなっちゃう
    x = et[i]
    root = par[x]
    dp[root] += dp[x]
ans = 0
#print(dp)
for i in range(n-1):
    u,v,w = d[i]
    if u == par[v]:
        ans += dp[v]*(n-dp[v])*w
    else:
        ans += dp[u]*(n-dp[u])*w
print(ans)
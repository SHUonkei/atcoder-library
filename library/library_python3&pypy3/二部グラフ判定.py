
import sys
sys.setrecursionlimit(10**7)

from collections import defaultdict 

N,M = map(int,input().split())
dict = defaultdict(set)

for i in range(M):
    a,b = list(map(int,input().split()))  

    dict[a].add(b)
    dict[b].add(a)

vis = [0]*(N+1)
ans = 0
s = 0
s2 = 0

d = []
color = [0 for _ in range(N+1)]
for j in range(1,N+1):
    if vis[j] == 1:
        continue
    global count2
    global count1
    
    count1 = 1
    count2 = 0
    from collections import deque
    
    color[j] = 1
    que = deque([j])#始点を追加
    bipartite = True

    while len(que):
        p = que.popleft()#直近で追加したグラフの頂点を取得
        vis[p] = 1
        for q in list(dict[p]):#結合しているグラフの頂点を参照
            if color[q] == 0:#塗られていないなら別の色で塗る
                color[q] = -color[p]
                if color[q] == 1:
                    count1 +=1
                else:
                    count2 += 1
                que.append(q)
            elif color[q] == color[p]:#同じ色だったら2部グラフではないと返し終了させる
                bipartite = False
                break


    if bipartite == False:
        print(0)
        exit()

    
    ans += count1*count2

    s += count1+count2
    d.append(count1+count2)


tot = [0]
now = 0
for i in range(len(d)):
    now += d[i]
    tot.append(now)

s2 = 0
for i in range(len(d)):
    s2 += d[i]*(s-tot[i+1])

#  print(ans)
#  print(d)
#    print(tot)

print(ans + s2 -M)

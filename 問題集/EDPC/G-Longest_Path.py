#入力　to 隣接リスト
n, m = map(int, input().split())
e = [[] for _ in range(n)]
into_num = [0 for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    e[a-1].append(b-1)
    into_num[b-1] += 1

from collections import deque
def topological_sort(G, into_num):
    dp = [None]*(n)
    #入ってくる有向辺を持たないノードを列挙
    q = deque()
    for i in range(n):
        if into_num[i] == 0:
            q.append(i)
            dp[i] = 0
    
    #以下、幅優先探索
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for adj in G[v]:
            into_num[adj] -= 1 #入次数を減らす　　頂点を消すことに対応
            if into_num[adj]==0:
                q.append(adj) #入次数が0になったら、キューに入れる
                if dp[adj] != None:
                    dp[adj] = max(dp[v]+1,dp[adj])
                else:
                    dp[adj] = dp[v]+1
                
    return ans,dp


x,y = topological_sort(e,into_num)

ans = max(y)
print(ans)
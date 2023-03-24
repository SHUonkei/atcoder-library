
"グラフ G は閉路の無い有向グラフ DAG である ⇔ グラフ G はトポロジカルソートできる"

"頂点に入る辺の数(入次数)に注目"
"次数が0であれば、トポロジカルソートをした時に先頭に持ってこられることを利用"

"トポロジカルソートを実行する際のポイントは、ノードの入次数を管理するリスト into_num "


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

    #入ってくる有向辺を持たないノードを列挙
    q = deque()
    for i in range(n):
        if into_num[i]==0:
            q.append(i)
    
    #以下、幅優先探索
    #辞書順最小出力したいときはdequeをheapqにすればできる
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for adj in G[v]:
            into_num[adj] -= 1 #入次数を減らす　　頂点を消すことに対応
            if into_num[adj]==0:
                q.append(adj) #入次数が0になったら、キューに入れる
    
    return ans




"閉路存在確認方法"

ans = topological_sort(e, into_num) #トポロジカルソート
#トポロジカルソートされたリストの頂点数　と　元のグラフの頂点数を比較
if len(ans)==len(e):
    print('閉路なし') #同じ頂点数なら閉路なし
else:
    print('閉路有り') #頂点数が異なると閉路が存在している
    
    


"再帰"
from collections import defaultdict 
 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def topologicalSortUtil(self,v,visited,stack): 
  
        visited[v] = True
  
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        stack.insert(0,v) 
  
    def topologicalSort(self): 
        visited = [False]*self.V 
        stack =[] 
  
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        print (stack) 
  
g= Graph(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 

print ("トポロジカルソートの実行結果：")
g.topologicalSort()


"最長経路の長さ出力"

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
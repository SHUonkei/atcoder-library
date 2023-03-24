# Union-Find 木
class unionfind:
# n 頂点の Union-Find 木を作成
# （ここでは頂点番号が 1-indexed になるように実装しているが、0-indexed の場合は par, size のサイズは n でよい）
    def __init__(self, n):
        self.n = n
        self.par = [ -1 ] * (n + 1) # 最初は親が無い　parents だからpar
        self.size = [ 1 ] * (n + 1) # 最初はグループの頂点数が 1

    # 頂点 x の根を返す関数
    def root(self, x):
        passed = [] #通過した頂点をすべていれる
        # 1 個先（親）がなくなる（つまり根に到達する）まで、1 個先（親）に進み続ける
        while self.par[x] != -1:
            passed.append(x)
            x = self.par[x]
        for v in passed: #通過した頂点の直接の親をxにする
            self.par[v] = x
        return x

    # 要素 u, v を統合する関数
    def unite(self, u, v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            # u と v が異なるグループのときのみ処理を行う
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]

    #  要素 u と v が同一のグループかどうかを返す関数
    def same(self, u, v):
        return self.root(u) == self.root(v)

N,M,Q = map(int,input().split())

uni = unionfind(N)
e = []
for i in range(M):
    a,b,c = map(int,input().split())
    e.append((c,a,b))
data= set()
querry = []
for j in range(Q):
    a,b,c = map(int,input().split())
    e.append((c,a,b))
    data.add((c,a,b))
    querry.append((c,a,b))
    

ans = set()
e.sort()
for i in range(M+Q):
    if not uni.same(e[i][1],e[i][2]):
        if not (e[i] in data):
            uni.unite(e[i][1],e[i][2])
        else:
            ans.add(e[i])

for i in range(Q):
    if querry[i] in ans:
        print("Yes")
        continue
    print("No")
n = int(input())
datax = []
datay = []
for i in range(n):
    x,y = map(int,input().split())
    datax.append((x,y,i))
    datay.append((y,x,i))

datax.sort()
datay.sort()

e = []
for i in range(n-1):
    x,y,idx = datax[i]
    x1,y1,idx1 = datax[i+1]
    u,v,idx2 = datay[i]
    u3,v3,idx3 = datay[i]

    e.append((min(abs(x-x1),abs(y-y1)),idx,idx1))
    e.append((min(abs(u-u3),abs(v-v3)),idx2,idx3))

e.sort()

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
ans = 0
uni = unionfind(n+1)
for i in range(len(e)):
    cost,u,v = e[i]
    if uni.same(u,v):
        continue
    uni.unite(u,v)
    ans += cost
print(ans)
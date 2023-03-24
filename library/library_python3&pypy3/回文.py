#貪欲？
#左からやってく貪欲だと反例ありそう
#ないか


#単調性あるか？


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


N = int(input())
if N == 1:
    print(0)
    exit()
A = list(map(int,input().split()))
M = max(A)
uni = unionfind(M)
s = set()
for i in range(N):
    s.add(A[i])

for i in range(N//2):
    uni.unite(A[i], A[N-1-i])
c = 0
for i in range(1,M+1):
    if uni.par[i] == -1 and i in s:
        c += 1
print(len(s) - c)
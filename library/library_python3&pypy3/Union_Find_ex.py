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





# Union-Find 木
class unionfind:
	# n 頂点の Union-Find 木を作成
	# （ここでは頂点番号が 1-indexed になるように実装しているが、0-indexed の場合は par, size のサイズは n でよい）
	def __init__(self, n):
		self.n = n
		self.par = [ -1 ] * (n + 1) # 最初は親が無い
		self.size = [ 1 ] * (n + 1) # 最初はグループの頂点数が 1
	
	# 頂点 x の根を返す関数
	def root(self, x):
		# 1 個先（親）がなくなる（つまり根に到達する）まで、1 個先（親）に進み続ける
		while self.par[x] != -1:
			x = self.par[x]
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







class UnionFind:
    # 参考 https://note.nkmk.me/python-union-find/
    # 参考 https://ikatakos.com/pot/programming_algorithm/data_structure/union_find_tree
    def __init__(self, n):
        self.parents = [-1] * n   # 負は親（数値は木の大きさ）、非負は子（数値は親インデックス）

    def root(self, x):       # 木の根 非再帰版  O(α(N))
        stack = []
        while self.parents[x] >= 0:
            stack.append(x)
            x = self.parents[x]
        for y in stack:
            self.parents[y] = x
        return x

    def union(self, x, y):   # 木を結合する  O(α(N))
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        
    def size(self, x):       # 木のサイズ     O(α(N))
        return -self.parents[self.root(x)]

    def same(self, x, y):    # 同じ木に属するか  O(α(N))
        return self.root(x) == self.root(y)

    def roots(self):         # O(N)
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):   # グループ数  O(N)
        return len(self.roots())


H, W = map(int, input().split())
Q = int(input())
q = [list(map(int, input().split())) for _ in range(Q)]

S = [[False] * W for _ in range(H)]

uf = UnionFind(W * H)
for query in q:
    if query[0] == 1:
        r, c = map(lambda x: x - 1, query[1:])
        S[r][c] = True
        for rd, cd in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            rr, cc = r + rd, c + cd
            if 0 <= rr < H and 0 <= cc < W and S[rr][cc]:
                uf.union(r * W + c, rr * W + cc)
    else:
        ra, ca, rb, cb = map(lambda x: x - 1, query[1:])
        if S[ra][ca] and S[rb][cb] and uf.same(ra * W + ca, rb * W + cb):
            print('Yes')
        else:
            print('No')
import sys
sys.setrecursionlimit(10**7)

N = int(input())
G = [[] for _ in range(N+1)]

for i in range(N-1):
    a,b,c = map(int,input().split())
    G[a].append((c,b))
    G[b].append((c,a))


# Euler Tour の構築
S = []
vis = [False] * (N+1)

F = [0]*(N+1)
depth = [0]*(N+1)
dist = [0]*(N+1)
def dfs(v, d, c):
    F[v] = len(S)
    depth[v] = d
    dist[v] = c
    vis[v] = True
    S.append(v)
    for cost,w in G[v]:
        if vis[w]:
            continue
        dfs(w, d+1,c+cost)
        S.append(v)

dfs(1, 0, 0)



#非再帰 SegTree

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

class SegTree:
    X_unit = 10**10#モノイドの単位元
    X_f = min

    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N) #1-based index

    def build(self, seq):
        for i, x in enumerate(seq, self.N):#indexの番号、要素の順に取得できる
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):#-1個飛ばしに
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])# | 1 は１を足してるだけ

    def set_val(self, i, x):
        i += self.N #初期値はNからスタートするので
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)


seg = SegTree(N+1)
A = [0]*(N+1)
seg.build(S)
Q,K = map(int,input().split())


#頂点xからyまでの最短距離を求める(未確認)
for i in range(Q):
    x,y = map(int,readline().split())
    left = min(F[x],F[y])
    right = max(F[x],F[y])
    u = seg.fold(left,right)
    print(dist[x]+dist[y]-2*dist[u])
    #print(seg.X)

#頂点の数字の合計とかはへんの貼り方を工夫して、4から5ならcost5,5から4ならcost4みたいにすればいけそー
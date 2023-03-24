#非再帰 SegTree

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

class SegTree:
    X_unit = -10**10#モノイドの単位元
    X_f = max

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

N, Q = map(int, readline().split())
seg = SegTree(N+1)
A = [0]*(N+1)
seg.build(A)

for i in range(Q):
    u,v,w = map(int,readline().split())
    if u == 1:
        seg.set_val(v,w)
        continue
    print(seg.fold(v,w))
    #print(seg.X)
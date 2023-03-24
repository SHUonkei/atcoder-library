n = int(input())
a = list(map(int,input().split()))

#座圧

b = sorted(list(set(a)))
d = {v:i for i,v in enumerate(b)}

for  i in range(n):
    a[i] = d[a[i]]+1

#非再帰 SegTree

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


#X_fとX_unit変えることに注意

#開区間
#0-indexed
#a0,a1,a2,...
#ベースの1-indexed

class SegTree:
    X_unit = -1 << 30#モノイドの単位元
    X_f = max

    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N) #

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

seg = SegTree(n+1)
dp = [0 for i in range(n+1)]
seg.build(dp)

for i in range(n):
    A = seg.fold(0,a[i]-1+1)

    dp[a[i]] = max(dp[a[i]],A+1)
    seg.set_val(a[i],dp[a[i]])
#    print(dp)

print(max(dp))
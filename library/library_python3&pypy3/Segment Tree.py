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
    X_unit = 1 << 30#モノイドの単位元
    X_f = min

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

N, Q = map(int, readline().split())
seg = SegTree(N)
A = map(int, readline().split())
seg.build(A)

m = map(int, read().split())
ans = (seg.fold(L,R) for L, R in zip(m, m))
print('\n'.join(map(str, ans)))



#xor

#クエリ処理
#一点更新

#BITかセグ木

#^がXOR

#非再帰 SegTree

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


#X_fとX_unit変えることに注意

class SegTree:
    X_unit = 0#モノイドの単位元

    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N) #

    def build(self, seq):
        for i, x in enumerate(seq, self.N):#indexの番号、要素の順に取得できる
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):#-1個飛ばしに
            self.X[i] = (self.X[i << 1] ^ self.X[i << 1 | 1])# | 1 は１を足してるだけ

    def set_val(self, i, x):
        i += self.N #初期値はNからスタートするので
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = (self.X[i << 1] ^ self.X[i << 1 | 1])

    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = (vL ^  self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = (self.X[R] ^  vR)
            L >>= 1
            R >>= 1
        return vL ^ vR

N, Q = map(int, readline().split())
seg = SegTree(N)
A = map(int, readline().split())
seg.build(A)

#print(seg.fold(0,1))
#print(seg.fold(0,2))
#print(seg.fold(0,3))
#print(seg.fold(1,3))
for i in range(Q):
    t,x,y = map(int,input().split())
    if t == 2:
        z = seg.fold(x-1,y-1+1)
#        print(seg.X)
        print(z)
        continue
    seg.set_val(x-1,seg.X[seg.N+x-1] ^ y)
#    print(seg.X)
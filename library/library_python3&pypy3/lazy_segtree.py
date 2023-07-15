import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


class LazySegTree:
    X_unit = (0, 0, 0)  # 無色、色1、色2
    A_unit = 0

    @classmethod
    def X_f(cls, x, y):
        a, b, c = x
        d, e, f = y
        return (a + d, b + e, c + f)

    @classmethod
    def A_f(cls, x, y):
        if not y:
            return x
        return y

    @classmethod
    def operate(cls, x, y):
        if not y:
            return x
        s = sum(x)
        if y == 1:
            return (0, s, 0)
        else:
            return (0, 0, s)

    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N)
        self.A = [self.A_unit] * (N + N)

    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def _eval_at(self, i):
        return self.operate(self.X[i], self.A[i])

    def _propagate_at(self, i):
        self.X[i] = self._eval_at(i)
        self.A[i << 1] = self.A_f(self.A[i << 1], self.A[i])
        self.A[i << 1 | 1] = self.A_f(self.A[i << 1 | 1], self.A[i])
        self.A[i] = self.A_unit

    def _propagate_above(self, i):
        H = i.bit_length() - 1
        for h in range(H, 0, -1):
            self._propagate_at(i >> h)

    def _recalc_above(self, i):
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self._eval_at(i << 1), self._eval_at(i << 1 | 1))

    def set_val(self, i, x):
        i += self.N
        self._propagate_above(i)
        self.X[i] = x
        self.A[i] = self.A_unit
        self._recalc_above(i)

    def fold(self, L, R):
        L += self.N
        R += self.N
        self._propagate_above(L // (L & -L))
        self._propagate_above(R // (R & -R) - 1)
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self._eval_at(L))
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self._eval_at(R), vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)

    def operate_range(self, L, R, x):
        L += self.N
        R += self.N
        L0 = L // (L & -L)
        R0 = R // (R & -R) - 1
        self._propagate_above(L0)
        self._propagate_above(R0)
        while L < R:
            if L & 1:
                self.A[L] = self.A_f(self.A[L], x)
                L += 1
            if R & 1:
                R -= 1
                self.A[R] = self.A_f(self.A[R], x)
            L >>= 1
            R >>= 1
        self._recalc_above(L0)
        self._recalc_above(R0)


N = int(readline())
Q = int(readline())

score_A = 0
score_B = 0
seg = LazySegTree(N)
seg.build([(1, 0, 0)] * N)
m = map(int, read().split())
for x, L, R in zip(m, m, m):
    R += 1
    if x == 0:
        _, a, b = seg.fold(L, R)
        if a > b:
            score_A += a
        elif b > a:
            score_B += b
    else:
        seg.operate_range(L, R, x)

_, a, b = seg.fold(0, N)
print(score_A + a, score_B + b)

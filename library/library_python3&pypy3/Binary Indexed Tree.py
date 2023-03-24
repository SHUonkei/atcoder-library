class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

# 使用例
bit = Bit(10)     # 要素数を与えてインスタンス化
bit.add(2, 10)    # a2に10を加える
bit.add(5, 5)     # a5に 5を加える
print(bit.sum(3)) # a1～a3の合計を返す => 10
print(bit.sum(6)) # a1～a6の合計を返す => 15
bit.add(3, -6)    # a3に-6を加える
print(bit.sum(6)) # a1～a6の合計を返す => 9
print(bit.sum(6) - bit.sum(3))  # a4～a6の合計 => 5

#RAQ Range add query


"転倒数"
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

N = int(input())
a = list(map(int,input().split()))

x = Bit(N)
ans = 0
for i in range(N):
    x.add(a[i],1)
    ans += x.sum(N)-x.sum(a[i])
#    print(ans)
print(ans)
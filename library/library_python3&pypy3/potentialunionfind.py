class unionfind_potential():
    #0-index
    def __init__(self,n: int):
        self.n = n
        self.par: list = [-1] * n
        self.values: list = [0 for _ in range(n)]
 
    def root(self, x: int) -> int:
        stack = []
        par = self.par
        vals = self.values
        while par[x] >= 0:
            stack.append(x)
            x = par[x]
        #経路圧縮
        if stack:
            val = 0
            while stack:
                y = stack.pop()
                val += vals[y]
                vals[y] = val
                par[y] = x
        return x

    def is_same(self, x: int, y: int) -> int:
        if self.root(x) == self.root(y):
            return 1
        else:
            return 0
 
    def diff(self, x: int, y: int) -> int:
        """
        x と y の差（y - x）を取得。同じグループに属さない場合は None。
        """
        if not self.is_same(x, y):
            return None
        vx = self.values[x]
        vy = self.values[y]
        return vy - vx
 
    def unite(self, x: int, y: int, d: int) -> bool:
        """
        x と y のグループを、y - x = d となるように統合。
        既に x と y が同グループで、矛盾する場合は AssertionError。矛盾しない場合はFalse。
        同グループで無く、新たな統合が発生した場合はTrue。
        """
        rx = self.root(x)
        ry = self.root(y)
        vx = self.values[x]
        vy = self.values[y]
        if rx == ry:
            assert vy + vx == d
            return False
 
        rd = vx + d - vy
        self.par[rx] += self.par[ry]
        self.par[ry] = rx
        self.values[ry] = rd
        return True
 
    def size(self, x: int) -> int:
        return -self.par[self.root(x)]
    
    def members(self, x:int) -> int:
        root_x = self.root(x)
        return [i for i in range(self.n) if self.root(i) == root_x]
    
    def group_count(self) -> int:
        count = 0
        for i in range(self.n):
            if self.par[i] < 0:
                count += 1
        return count

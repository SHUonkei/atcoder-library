# 座標圧縮したい数列
A = []
N = int(input())
for i in range(N):
    A.append(int(input()))

# 集合型にすることで重複を除去し、
# 小さい順にソートする
B = sorted(set(A))

#print(B) リストになってる

# B の各要素が何番目の要素なのかを辞書型で管理する
D = { v: i for i, v in enumerate(B) }

# 答え
x = list(map(lambda v: D[v], A))
for i in range(N):
    print(x[i])




#隣接リストの坐圧ver
from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)
for _ in range(n) :
    a, b = map(int, input().split())
    graph[a].append(b)#ふつうの dictだとここでkeyが既に設定されていない場合めんどいけどdefaultdict だと初期化されているからいける
    graph[b].append(a)#






#注意 get は動作が変わらない
d = {}
print(d.get('a'))
# Noneが返る

d = defaultdict(int)
print(d.get('a'))
# Noneが返る
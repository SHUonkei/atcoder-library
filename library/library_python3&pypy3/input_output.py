import sys
from sys import stdin
input = stdin.readline#一番最後に改（文字列のとき

#リストを空白なしで繋げて出力
ans = ["a","asdf","gs","afsfd"]
print("".join(map(str,ans)))

#最大ケースでTLEしないかテスト
import random
n = 10**4
a = [random.randint(1,10**5) for _ in range(n)]



for i in reversed(range(0, 5)):
    print(i)



#sort() リストの要素リストだと？

l = [[1,2],[1,3],[2,0],[0,0],[0,1]]
l.sort()
print(l)

#どうプリントされる？
dist = [[0]*5 for _ in range(5)]
print(dist)
print(*dist)
for i in range(5):
    print(*dist[i])

#リストってあとからかえたら前に代入した変数もかわっちゃう？
k = l
l = []
print(l)
print(k)

"mapにsetのせることできる！"
s = list(map(set,input().split()))
print(s)
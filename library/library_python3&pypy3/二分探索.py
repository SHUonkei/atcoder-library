import bisect
#bisect_leftは、挿入できるリストの添字を返します。
#同じ値がある場合は、その値の最も左側の添字になります。
li = [2, 5, 8, 13, 13, 18, 25, 30]

ind = bisect.bisect_left(li, 10)
print(ind)

ind = bisect.bisect_left(li, 13)
print(ind)

#
#3
#3
#

#bisect_rightとbisectは、挿入できるリストの添字を返します。
# 同じ値がある場合は、その値の最も右側の添字になります。
li = [2, 5, 8, 13, 13, 18, 25, 30]

ind = bisect.bisect_right(li, 10)
print(ind)

ind = bisect.bisect_right(li, 13)
print(ind)

ind = bisect.bisect(li, 10)
print(ind)

ind = bisect.bisect(li, 13)
print(ind)

#
#3
#5
#3
#5
#

a, b, x = map(int, input().split())


def is_ok(arg):
    #整数を変えればTを返す
    if a * arg + b * len(str(arg)) <= x:
        return True 
    else:
        return False

def meguru_bisect(ng, ok):
    while abs(ok - ng) >1 :
        mid =(ok +ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(10**9+1,0))

# #求めたい境目を境にして「左側はすべて偽で、右側はすべて真」である
# という単調性を仮定しましたが、「条件を満たす最小」を求めることにこだわらなければこの仮定はなくてもよく
# 二分探索の初期値の一方が真、もう一方が偽になるようにしておいて、真偽の境目を 1 つ求める
# という使い方もできます。単調性の仮定がなければ真偽の境目が複数あり得て、そのうちの 1 つが求まることになります。このような二分探索法フレームワークは、例えば方程式 f(x) = 0 の解をどれか 1 つ求めたい場面などで活用することができます。
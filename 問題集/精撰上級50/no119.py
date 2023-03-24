N = int(input())
S = input()
T = list(map(lambda c:ord(c) - ord("a") + 1,S))

mod = 2147483647
power100 = [None] * (N+1)
power100[0] = 1
for i in range(N):
    power100[i+1] = power100[i] * 1000 %mod

H = [ None ] * (N+1)
H[0] = 0

for i in range(N):
    H[i+1] = (H[i] * 1000 + T[i]) %mod

def hash_value(l,r):
    return (H[r] - H[l-1] * power100[r-l+1])%mod#rからl-1を引く！！！


#前探索無理
#xで可能か？のにぶたんできそう
#一回あたりNで探索できるから
#NlogN
from collections import defaultdict
def is_ok(arg):#argで可能か？
    s = set()
    d = defaultdict(list)
    for i in range(N-arg+1):
        x = hash_value(i+1,i+arg)
#        print(x)
        if x in s:
            if d[x][0] < i+1:
                return True
        s.add(x)
        d[x].append(i+arg)
    return False

def bis(left,right):
    while right - left > 1:
        mid = (right + left)//2
#        print(left,right,mid)
        if is_ok(mid):
            left = mid
            continue
        right = mid
    return left

print(bis(0,N+1))
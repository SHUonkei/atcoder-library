N,Q= map(int,input().split())
S = input()

# 文字を数値に変換（ここでは書籍とは異なり、0-indexed で実装しています）
# ord(c) で文字 c の文字コード（ASCII コード）を取得
T = list( map( lambda c:ord(c) - ord("a") + 1, S ) )

# 100 の n 乗を前計算
#define B1 100000007
B1 = 100000007
#define B2 1000000007
B2 = 1000000007

B = B1
mod = 2147483647
powerB = [ None ] * ( N+1 )
powerB[ 0 ] = 1
for i in range( N ):
    powerB[ i + 1 ] = powerB[ i ] * B  %mod#このmodないと死ぬ

# H[1], H[2], ..., H[N] を計算する

H = [ None ] * (N + 1)
H[ 0 ] = 0
for i in range( N ):
    H[ i+1 ] = ( H[ i ] * B + T[ i ] ) % mod

# ハッシュ値を求める関数
# S[l-1:r] のハッシュ値は (H[r] - H[l - 1] * power100[r - l + 1]) % mod で計算
# C++ とは異なり、（負の値）% M (M >= 1) も 0 以上 M-1 以下になることに注意

def hash_value(l,r):
    #閉区間での実装
    #H[1]は1乗
    #H[r] はr乗,H[l-1]はl-1乗よって100^{r-(l-1)}をかけて
    #最高位の桁(=先頭の文字の100^n)を揃えて引き算する
    #最後mod取るの忘れずに
    return (H[r] - H[l-1] * powerB[r-l+1])%mod

for i in range(Q):
    a,b,c,d = map(int,input().split())
    hash1 = hash_value(a,b)
    hash2 = hash_value(c,d)
#    print(hash1)
#    print(hash2)
    if hash1 == hash2:
        print("Yes")
        continue
    print("No")



#後ろ側から

N = int(input())
#N = 2*N #文字列のながさが2カケルN
S = list(input())

T = list(map(lambda c:ord(c) - ord("a") + 1,S))


B = 1000
mod = 2147483647
pB = [None]*(N+1)

pB[0] = 1
for i in range(N):
    pB[i+1] = pB[i] * B %mod


H = [None] * (N+1)
H[0] = 0

for i in range(N):
    H[i+1] = (H[i] * B + T[i])%mod

def hash_value(l,r):
    return (H[r]-H[l-1] * pB[r-l+1])%mod#最高位の桁のB^nを揃える

#iを決定することでTからSの唯一の候補が得られる
#それが一致するかを調べるとき、にハッシュ値を用いればO(1)でO(N)が全体
#でもハッシュ値を文字列反転した時のやつを得るのは難しいから
#逆側からローリングハッシュを使ってそれと一致するかでみるか

aH = [None] * (N+1)
aH[N] = 0

#H[N]が0
#H[N-1]がT[N-1]

for i in reversed(range(1,N+1)):
   aH[i-1] = (aH[i] * B + T[i-1])%mod#H[j]の最高位がB^(N-j)

def hash_ad_value(l,r):
    return (aH[l-1] - aH[r-1+1] * pB[r-(l-1)])%mod
#   return (aH[l-1] - aH[r-1+1] * pB[N-(l-1) - (N-(r-1+1))])%mod

#print(H)
#print(aH)


#for i in range(N//2):
#    x = hash_value(1,i+1) * pB[N//2-(i+1)] %mod
#    y = hash_value(N//2+i+2,N)
#    z = hash_ad_value(i+1+1,N//2+i+1)
#    print(x,y,(x+y)%mod,z,i+1)
#    if (x+y)%mod  == z:
        #一番前のやつのB^0の項が、Bの（後ろのながさ乗）になるといいので
#        print("".join(S[0:i+1]+S[N//2+i+1:N]))
#        print(i+1)
#        exit()
#print(-1)
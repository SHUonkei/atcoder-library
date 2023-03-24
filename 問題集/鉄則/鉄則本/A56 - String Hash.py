N,Q= map(int,input().split())
S = input()

# 文字を数値に変換（ここでは書籍とは異なり、0-indexed で実装しています）
# ord(c) で文字 c の文字コード（ASCII コード）を取得
T = list( map( lambda c:ord(c) - ord("a") + 1, S ) )

# 100 の n 乗を前計算
mod = 2147483647
power100 = [ None ] * ( N+1 )
power100[ 0 ] = 1
for i in range( N ):
    power100[ i + 1 ] = power100[ i ] * 100  %mod

# H[1], H[2], ..., H[N] を計算する

H = [ None ] * (N + 1)
H[ 0 ] = 0
for i in range( N ):
    H[ i+1 ] = ( H[ i ] * 100 + T[ i ] ) % mod

# ハッシュ値を求める関数
# S[l-1:r] のハッシュ値は (H[r] - H[l - 1] * power100[r - l + 1]) % mod で計算
# C++ とは異なり、（負の値）% M (M >= 1) も 0 以上 M-1 以下になることに注意

def hash_value(l,r):
    #閉区間での実装
    #H[1]は1乗
    #H[r] はr乗,H[l-1]はl-1乗よって100^{r-(l-1)}をかけて
    #最高位の桁(=先頭の文字の100^n)を揃えて引き算する
    #最後mod取るの忘れずに
    return (H[r] - H[l-1] * power100[r-l+1])%mod

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
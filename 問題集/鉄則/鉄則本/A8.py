H,W = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(H)]

Q = int(input())
sum = [[0]*(W+1) for _ in range(H+1)]

for i in range(1,H+1):
    for j in range(1,W+1):
        sum[i][j] = sum[i][j-1] +X[i-1][j-1]


"累積和では、和をとる方向が変化すると添字も逆になるので気を付ける！！！"
for i in range(1,W+1):
    for j in range(1,H+1):
        sum[j][i] += sum[j-1][i]
        "←ここでいったんREになってた"

#for i in range(H+1):
#    print(*sum[i])

for i in range(Q):
    a,b,c,d = map(int,input().split())
    print(sum[c][d]+sum[a-1][b-1]-sum[a-1][d]-sum[c][b-1])
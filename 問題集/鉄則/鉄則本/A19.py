N,W = map(int,input().split())
wv = [list(map(int,input().split())) for _ in range(N)]

dp = [[-10**15]*(W+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1,N+1):
    for j in range(W+1):
        if j >= wv[i-1][0]:
            dp[i][j] = max(dp[i-1][j-wv[i-1][0]] + wv[i-1][1],dp[i-1][j])#ピッタリjのときの最大は元止まる
        else:
            dp[i][j] = dp[i-1][j]
now = 0
for i in range(W+1):
    now = max(now,dp[N][i])
#print(dp)
print(now)
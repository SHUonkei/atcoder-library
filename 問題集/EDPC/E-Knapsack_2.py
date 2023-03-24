n,W = map(int,input().split())

wv = [list(map(int,input().split())) for _ in range(n)]
m = 0
for i in range(n):
    m = max(m,wv[i][1])

dp = [[float("inf")]*(m*n+1) for _ in range(n)]

for i in range(n):
    dp[i][0] = 0

if wv[0][0] <= W:
    dp[0][wv[0][1]] = wv[0][0]
    now = wv[0][1]
else:
    now = 0
for i in range(1,n):
    for j in range(1,m*n+1):
        if dp[i-1][j-wv[i][1]]+wv[i][0] <=W:
            dp[i][j] = min(dp[i-1][j],dp[i-1][j-wv[i][1]]+wv[i][0])
        else:
            dp[i][j] = dp[i-1][j]
        if dp[i][j] != float("inf"):
            now = max(now,j)
#print(dp)
print(now)
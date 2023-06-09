N = int(input())
p = list(map(float,input().split()))

dp = [[0]*(N+1) for _ in range(N)]

dp[0][1] = p[0]
dp[0][0] = 1-p[0]

for i in range(1,N):
    dp[i][0] = dp[i-1][0]*(1-p[i])


for i in range(1,N):
    for j in range(1,i+2):
        dp[i][j] = dp[i-1][j]*(1-p[i]) + dp[i-1][j-1]*p[i]

x = ((N)//2 +1)
ans = 0
for i in range(x,N+1):
    ans += dp[N-1][i]
#for i in range(N):
#    print(dp[i])
print(ans)
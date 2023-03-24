N = int(input())
a = list(map(int,input().split()))
par = [[-1] for _ in range(N+1)]
for i in range(2,N+1):
    par[i][0] = a[i-2]#0インデックス

dp = [0]*(N+1)

for i in reversed(range(2,N+1)):
    dp[par[i][0]] += dp[i]+1

for i in range(1,N+1):
    print(dp[i],end = " ")
n = int(input())
a = list(map(int,input().split()))
S = [0]
now = 0
for i in range(n):
    now += a[i]
    S.append(now)

dp=[[-1]*(n) for _ in range(n+1)]
#dp[iコメ][jが一個前の休日]

def f(delta):
    if delta %2 == 0:
        return S[delta//2]*2
    return S[delta//2]*2 + a[delta//2]

for i in range(n):
    dp[i][0] = f(n-1)

ans = 0
for i in range(n):
    for j in range(i):
        if dp[i][j] == -1:
            continue
        dp[i+1][j] = max(dp[i][j],dp[i+1][j])
        dp[i+1][i] = max(dp[i][j]-f(n-j-1)+f(i-j-1)+f(n-i-1),dp[i+1][i])
        
for i in range(n+1):
    for j in range(n):
        ans = max(dp[i][j],ans)
#print(dp)
print(ans)

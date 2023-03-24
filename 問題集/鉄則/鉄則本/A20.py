S = list(input())
T = list(input())
s = len(S)
t = len(T)
dp = [[0]*(s+1) for _ in range(t+1)]

'''
T[0] とかS[0]をみるときにちゃんと→カウントできるように、s+1,t+1にしている
'''
for i in range(1,t+1):
    for j in range(1,s+1):
        if T[i-1] == S[j-1]:
            dp[i][j] = max(dp[i-1][j-1] +1,dp[i-1][j],dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])



'''
dp復元の練習
dpコンテストのF
'''
ans = []

ct = 0
cs = 0
while len(ans) < dp[t][s]:
    if T[t-ct-1] == S[s-cs-1]:
        ans.append(T[t-ct-1])
        ct += 1
        cs += 1
    else:
        if dp[t-ct][s-cs] == dp[t-ct-1][s-cs]:
            ct += 1
        else:
            cs += 1
ans.reverse()

print("".join(map(str,ans)))

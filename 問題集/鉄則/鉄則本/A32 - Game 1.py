N,A,B = map(int,input().split())

#先手勝利を0とする
dp = [1]*(N+1)

for i in range(min(A,B),N+1):
    if i-A >= 0 and i-B >= 0:
        if dp[i-A] == 1 or dp[i-B] == 1:
            dp[i] = 0
    elif i-min(A,B) >= 0:
        if dp[i-min(A,B)] == 1:
            dp[i] = 0
    
#print(dp)
if dp[N] == 0:
    print("First")
    exit()
print("Second")

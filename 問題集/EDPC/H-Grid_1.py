H,W = map(int,input().split())

a = [list(input()) for _ in range(H)]

dp = [[0]*W for _ in range(H)]
dp[0][0] = 1


dy = [0,1]
dx = [1,0]

for i in range(H):
    for j in range(W):
        for k in range(4):
            u = i + dy[k]
            v = j + dx[k]
            if 0<= u < H and 0 <= v < W and a[u][v] != "#":
                dp[u][v] += dp[i][j]
#print(dp)
print(dp[H-1][W-1]%(10**9+7))
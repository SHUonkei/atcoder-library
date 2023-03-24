N,S = map(int,input().split())
A = list(map(int ,input().split()))
dp = [[0]*(S+1) for _ in range(N)]#同じインデックスのやつをたくさん参照すると少し早くなる



#オーダー的にSつかう→なら二次元DPかー？
#部分話問題がDPは典型

#S=0の時絶対できる

for i in range(S+1):
    if i ==0:#非常に忘れがち
        dp[0][i] = 1
        continue
    if i == A[0]:
        dp[0][i] = 1
        if i == S:
            print("Yes")
            exit()
        continue
    dp[0][i] = 0

for i in range(1,N):
    dx = A[i]
    for j in range(S+1):
        if j>=dx:
            if dp[i-1][j] == 1:
                dp[i][j] = 1
            else:
                if dp[i-1][j-dx] == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
        else:
            if dp[i-1][j] == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = 0

#print(dp)
if dp[N-1][S] == 1:
    print("Yes")
    exit()
print("No")

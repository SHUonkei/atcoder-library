N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(M)]
dp = [[10**15]*(2**N) for _ in range(M+1)]
#最小値なので超でかいやつにしとく
dp[0][0] = 0
data = [set() for _ in range(2**N)]

for i in range(2**N):
    for j in range(N):
        if i>>j &1:
            data[i].add(j+1)

a = [set() for _ in range(M)]

for i in range(M):
    for j in range(N):
        if A[i][j] == 1:
            a[i].add(j+1)

#print(a)


#print(data)

for i in range(M):
    for j in range(2**N):
        u = data[j].union(a[i])
#        print(data[j],u)
        if  u == data[j]:
            dp[i+1][j] = min(dp[i+1][j],dp[i][j])
        else:
            dp[i+1][j] = min(dp[i+1][j],dp[i][j])
            s = 0
            for k in u:
                s+=2**(k-1)
#            print(i,j,s)
            dp[i+1][s] = min(dp[i+1][s],dp[i][j]+1)
#print(data)
#for i in range(M):
#    print(dp[i])
if dp[M][2**N-1] == 10**15:
    print(-1)
    exit()
print(dp[M][2**N-1])

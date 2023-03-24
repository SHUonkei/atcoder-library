N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

DP = [0]*N
DP[1] = A[0]
for i in range(2,N):
    x = DP[i-1] + A[i-1]
    y = DP[i-2] + B[i-2]
    DP[i] = min(x,y)
print(DP[N-1])

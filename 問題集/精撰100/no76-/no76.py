N = int(input())
A = list(map(int,input().split()))

sum = [0]*(N+1)
sum[1] = A[0]

for i in range(1,N):
    sum[i+1] = sum[i]+A[i]

for k in range(1,N+1):
    m = 0
    for i in range(N+1-k):
        m = max(sum[i+k] -sum[i],m)
    print(m)

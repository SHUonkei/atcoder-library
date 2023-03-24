N,K = map(int, input().split())
A = list(map(int ,input().split()))
R = [0]*N
for i in range(N):
    if i != 0:
        R[i] = R[i-1]
    for j in range(R[i-1]+1,N):
        if A[j]-A[i]>K:
            break
        R[i] += 1
sum =0
for i in range(N):
    sum += (R[i]-i)
print(sum)
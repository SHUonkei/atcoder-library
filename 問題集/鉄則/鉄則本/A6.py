N,Q = map(int,input().split())

A= list(map(int,input().split()))

sum = [0]
s = 0
for i in range(N):
    s += A[i]
    sum.append(s)

for j in range(Q):
    l,r  = map(int,input().split())
    print(sum[r]-sum[l-1])
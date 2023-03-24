N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

DP = [0]*N
DP2 = [N]
DP[1] = A[0]
for i in range(2,N):
    x = DP[i-1] + A[i-1]
    y = DP[i-2] + B[i-2]
    DP[i] = min(x,y)
c =N-1
while c >= 1:
    if DP[c] == DP[c-1]+A[c-1]:
        DP2.append(c)
        c-=1
        continue
    DP2.append(c-1)
    c-=2

ans = []
for i in range(len(DP2)):
    ans.append(DP2[len(DP2)-1-i])
print(len(ans))
print(*ans)
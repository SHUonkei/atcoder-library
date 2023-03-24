N,K = map(int,input().split())

ab = [list(map(int,input().split())) for _ in range(N)]


"何を全探索するか"
"何を固定するか"
ans = 0
for i in range(1,100-K):
    for j in range(1,100-K):
        c = 0
        for k in range(N):
            if i<=ab[k][0]<=i+K and j<=ab[k][1]<=j+K:
                c += 1
        ans = max(ans,c)

print(ans)
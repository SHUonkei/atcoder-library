n, m = map(int, input().split())
axy= [list(map(int, input().split())) for _ in range(n)]
now = 0
for i in range(m):
    for j in range(i+1, m):
        sum=0
        for k in range(n):
            sum += max(axy[k][i], axy[k][j])
        now = max(now, sum)
print(now)
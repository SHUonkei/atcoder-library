n, m = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(m)]
ans = 0
for i in range(2**n):
    cand=[]
    data={}
    now = 0
    count = 0
    for j in range(n):
        if (i>>j) & 1:#jと議員の番号一個ずれてることに気をつけて
            now += 1
            cand.append(j+1)
    if now*(now-1)/2 <= m:
        data = set(cand)
        for k in range(m):
            if xy[k][0] in data and xy[k][1] in data:
                count += 1
        if count == now*(now-1)/2:
            ans = max(len(data),ans)
print(ans)

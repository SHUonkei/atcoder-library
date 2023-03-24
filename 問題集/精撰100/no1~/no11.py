n , m = map(int, input().split())
K = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

ans = 0
for i in range(2**n):#スイッチのonoff
    count = 0
    for k in range(m):#どの行をみるか
        now = 0
        for j in range(n):#ビットで行でスイッチのオンオフとの対応をみる
            if ((i>>j)& 1):
                for h in range(1,K[k][0]+1):
                    if K[k][h] == 1+j:
                        now += 1
        if now %2 == p[k]:
            count += 1
    if count == m:
        ans += 1
print(ans)
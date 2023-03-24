import sys
sys.setrecursionlimit(10**7) # 再起回数の設定

N = int(input())
ukv = [list(map(int, input().split())) for _ in range(N)]
d = [0]*(N+1)
f = [0]*(N+1)

now = 0

def dfs(x):
    global now
    now  +=  1 
    if d[x] == 0:
        d[x] = now
    if ukv[x-1][1] == 0:
        f[x] = now
        return
    if ukv[x-1][1] != 0:
        for i in range(2,ukv[x-1][1]+1):
            dfs(ukv[x-1][i])
        return

dfs(1)

for i in range(N):
    print(i+1, d[i+1], f[i+1])
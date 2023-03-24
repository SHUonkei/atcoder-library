import sys
sys.setrecursionlimit(10*8) # 再起回数の設定

ans = []
while True:
    now = 0
    W , H = map(int, input().split())
    if W == H ==0:
        break
    c = [list(map(int, input().split())) for _ in range(H)] #cの添字とリストの番号ズレてるのに注意
    def dfs(x,y):
        if x <= 0 or x > H or y <= 0 or y > W or c[x-1][y-1] == 0:
            return
        if c[x-1][y-1] == 1:
            c[x-1][y-1] = 0
            dfs(x+1,y)
            dfs(x+1,y+1)
            dfs(x+1,y-1)
            dfs(x-1,y)
            dfs(x-1,y+1)
            dfs(x-1,y-1)
            dfs(x,y+1)
            dfs(x,y-1)
    for i in range(1,H+1):
        for j in range(1,1+W):
            if c[i-1][j-1] == 1:
                now += 1
                dfs(i,j)
    ans.append(now)

for i in range(len(ans)):
    print(ans[i])
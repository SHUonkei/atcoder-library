H,W,N = map(int,input().split())

data = [[0]*(W+2) for _ in range(H+2)]

for i in range(N):
    a,b,c,d = map(int,input().split())
    data[a][b]     += 1
    data[a][d+1]   -= 1
    data[c+1][b]   -= 1
    data[c+1][d+1] += 1

for i in range(1,H+2):
    for j in range(1,W+2):
        data[i][j] += data[i][j-1]

for i in range(1,W+2):
    for j in range(1,H+2):
        data[j][i] += data[j-1][i]

for i in range(H):
    print(*data[i+1][1:W+1])
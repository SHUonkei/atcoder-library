N = int(input())

S = [list(input()) for _ in range(N)]

tate = [[0]*(N+1) for _ in range(N+1)]
yoko = [[0]*(N+1) for _ in range(N+1)]



for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            S[i][j] = 1
            continue
        S[i][j] = 0

for i in range(N):
    s = 0
    for j in range(N):
        s += S[i][j]
        yoko[i+1][j+1] = s
        if j >= 5:
            if yoko[i+1][j+1] - yoko[i+1][j-5] >= 4:
                print("Yes")
                exit()

for i in range(N):
    s = 0
    for j in range(N):
        s += S[j][i]
        tate[j+1][i+1] = s
        if j >= 5:
            if tate[j+1][i+1] - tate[j-5][i+1] >= 4:
                print("Yes")
                exit()

#斜め

naname = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        naname[i+1][j+1] = naname[i][j] + S[i][j]
        if j >= 5 and i >= 5:
            if naname[i+1][j+1] - naname[i-5][j-5] >= 4:
                print("Yes")
                exit()

naname2 = [[0]*(N+2) for _ in range(N+1)]

for i in range(N):
    for j in reversed(range(N)):
        naname2[i+1][j+1] = naname2[i][j+2] + S[i][j]
        if N+1 >= j+7  and i >= 5:
            if naname2[i+1][j+1] - naname2[i-5][j+7] >= 4:
                print("Yes")
                exit()
#for i in range(N+1):
#    print(*naname2[i])
print("No")


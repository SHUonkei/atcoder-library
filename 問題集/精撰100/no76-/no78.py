import sys
from sys import stdin
input = stdin.readline#一番最後に改（文字列のとき


M,N = map(int,input().split())
K = int(input())
area = [list(input()) for _ in range(M)]

"累積和"
sumj = [[0]*(N+1) for _ in range(M+1)]
sumi = [[0]*(N+1) for _ in range(M+1)]
sumo = [[0]*(N+1) for _ in range(M+1)]

for i in range(1,M+1):
    for j in range(1,N+1):
        x = area[i-1][j-1]
        if x == "J":
            sumj[i][j] = sumj[i][j-1] + 1
            sumi[i][j] = sumi[i][j-1]
            sumo[i][j] = sumo[i][j-1]

        if x == "I":
            sumi[i][j] = sumi[i][j-1] +1
            sumj[i][j] = sumj[i][j-1]
            sumo[i][j] = sumo[i][j-1]
        if x == "O":
            sumo[i][j] = sumo[i][j-1] +1
            sumj[i][j] = sumj[i][j-1]
            sumi[i][j] = sumi[i][j-1]

sumJ = [[0]*(N+1) for _ in range(M+1)]
sumI = [[0]*(N+1) for _ in range(M+1)]
sumO = [[0]*(N+1) for _ in range(M+1)]

for i in range(1,M+1):#キャッシュ　列と行たす順かえた
    for j in range(1,N+1):
        sumJ[i][j] = sumJ[i-1][j]+sumj[i][j]
        sumI[i][j] = sumI[i-1][j]+sumi[i][j]
        sumO[i][j] = sumO[i-1][j]+sumo[i][j]


#exit()
#print(sumI)
#print(sumJ)

for i in range(K):
    a,b,c,d = map(int,input().split())
    x = sumJ[c][d]+sumJ[a-1][b-1]-sumJ[a-1][d]-sumJ[c][b-1]
    z = sumI[c][d]+sumI[a-1][b-1]-sumI[a-1][d]-sumI[c][b-1]
    y = sumO[c][d]+sumO[a-1][b-1]-sumO[a-1][d]-sumO[c][b-1]
    print(x,y,z)

"改善"
def main():
    import sys
    I = sys.stdin.buffer.readline
    ii = int
    M,N = map(ii,I().split())
    K = ii(I())
    sumj = [0]*((M+1)*(N+1))
    sumi = [0]*((M+1)*(N+1))
    mm = list(range(1,M+1))
    nn = list(range(1,N+1))
    for i in mm:
        sumi[i*(N+1):(i+1)*(N+1)] = sumi[(i-1)*(N+1):(i)*(N+1)]
        sumj[i*(N+1):(i+1)*(N+1)] = sumj[(i-1)*(N+1):(i)*(N+1)]
        y = tuple(I())
        ci = 0
        cj = 0
        for j,x in zip(nn,y):
            if x == 74:cj+=1
            if x == 73:ci+=1
            sumi[i*(N+1)+j] += ci
            sumj[i*(N+1)+j] += cj
    for _ in '_'*K:
        a,b,c,d = map(ii,I().split())
        x = sumj[c*(N+1)+d]+sumj[(a-1)*(N+1)+b-1]-sumj[(a-1)*(N+1)+d]-sumj[c*(N+1)+b-1]
        z = sumi[c*(N+1)+d]+sumi[(a-1)*(N+1)+b-1]-sumi[(a-1)*(N+1)+d]-sumi[c*(N+1)+b-1]
        print('%d %d %d'%(x,(c-a+1)*(d-b+1)-x-z,z))
if __name__ == '__main__':
    main()
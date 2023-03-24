#考察ゲー　abs(x-i)　の和　の　計算を考えて　中央値で最小値をとるというプログラム
n = int(input())
axy = [list(map(int, input().split())) for _ in range(n)]

#ます番号-1がリストの番号に注意
a=[]
b=[]
for i in range(n):
    a.append(axy[i][0])
a.sort()
ans1 = a[len(a)//2]

for i in range(n):
    b.append(axy[i][1])
b.sort()
ans2 = b[len(b)//2]

sum = 0
for i in range(n):
    sum += abs(ans1-axy[i][0]) + abs(ans2-axy[i][1]) + abs(axy[i][0]-axy[i][1])
print(sum)
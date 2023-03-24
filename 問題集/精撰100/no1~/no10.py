n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

w = max(m)
u = min(m) 
data = []
for i in range(2 ** n):
    now = 0
    x   = 0
    for j in range(n):
        if ((i >> j) & 1):
            now += A[j]
        if now>w:
            break
    data.append(now)
    
data1=set(data)

for i in range(q):
    count = 0
    if m[i] in data1:#大事
        print("yes")
    else:
        print("no")
#TLEする　よくわからん
#リストのままならそのあと二分探索
#リストから集合
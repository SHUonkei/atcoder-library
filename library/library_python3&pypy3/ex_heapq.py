
import heapq
#heapq.pop　取り出して取得
#heapq.heappush　入れる
#max　取り出したいときは -つけて　富豪反転で最小値えてから　ーで符号戻す


n, m = map(int, input().split())
a = []

for i in input().split():
    # Pythonのheapは最小値がpopされるため、マイナスを付与した上でheapに入れる
    heapq.heappush(a, -int(i))

# 割引券がなくなるまで繰り返す
for j in range(m):
    # 最も高い値段を取り出す
    highest = heapq.heappop(a)
    # 半額にしてheapに戻す
    heapq.heappush(a, -(-highest // 2))

print(-sum(a))

"""""
つよい
"""""

N = int(input())
A = list(map(int, input().split()))

if N == 2:
    if A[0]%2 != A[1]%2:
        print(-1)
        exit()

even = []
odd  = []

for i in range(N):
    if A[i]%2 == 0:
        heapq.heappush(even,-A[i])
    else:
        heapq.heappush(odd,-A[i])

u1=0
u2=0
v1=0
v2=0

if len(even) >1:
    u1 = -heapq.heappop(even)
    u2 = -heapq.heappop(even)
if len(odd) >1:
    v1 = -heapq.heappop(odd)
    v2 = -heapq.heappop(odd)

ans = max(u1+u2,v1+v2)
print(ans)
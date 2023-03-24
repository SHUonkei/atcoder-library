Q = int(input())
lr = [list(map(int ,input().split())) for _ in range(Q)]
now1 = 10**9
now2 = 0

for i in range(Q):
    now2 = min(lr[0], now2)
    now = max(now, lr[1])
prime = []
for i in range(now2,now2+1):
    if prime
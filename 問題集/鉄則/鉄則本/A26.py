Q = int(input())
import math
for i in range(Q):
    u = int(input())
    c = 0
    for i in range(2,math.floor(math.sqrt(u))+1):
        if u%i == 0:
            c += 1
    if c >= 1:
        print("No")
        continue
    print("Yes")
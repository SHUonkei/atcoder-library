n = int(input())
import math
sum = 0
for j in range(1,n+1):
    if j%2 ==1 :
        m = math.floor(math.sqrt(j))
        count = 0
        for i in range(1, m+1):
            if j%i == 0:
                count += 1
        if count == 4:
            sum += 1
print(sum)
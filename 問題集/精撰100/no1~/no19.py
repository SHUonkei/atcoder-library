D = int(input())
N = int(input())
M = int(input())
data_1 = [0]
for i in range(N-1):
    x = int(input())
    data_1.append(x)
data_1.sort()
data_1.append(D)
for i in range(N-1):
    data_1.append(D+data_1[i+1])

data_2 = []
for j in range(M):
    y = int(input())
    data_2.append(y)

x=0
def is_ok(arg):
    if data_1[arg] >= x:
        return True
    else:
        return False

def binary(left, right):
    while abs(right - left) > 1:
        mid = (left + right)//2
        if is_ok(mid):
            right = mid
        else:
            left =  mid
    return min(abs(data_1[right]-x),abs(data_1[left]-x))
sum = 0
for i in data_2:
    x = i
    sum += binary(-1,2*N-1)

print(sum)
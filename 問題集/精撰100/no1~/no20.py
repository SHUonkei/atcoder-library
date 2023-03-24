N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()
x = 0
def is_ok_a(y):
    if A[y] >= x:#真に大きい rightに=が入る
        return True
    else:
        return False

def binary_a(left, right):
    while abs(right - left) > 1:
        mid = abs(right + left)//2
        if is_ok_a(mid):
            right = mid
        else:
            left = mid
    return right

def is_ok_c(z):
    if C[z] > x:
        return True
    else:
        return False

def binary_c(left, right):
    while abs(right - left) > 1:
        mid = abs(right + left)//2
        if is_ok_c(mid):
            right = mid
        else:
            left = mid
    return right

count = 0
for i in B:
    x = i
    count += binary_a(-1,N) * (len(C)-binary_c(-1,N))

print(count)
#二分探索であわないとき、境界やばいかも
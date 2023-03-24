N,K = map(int, input().split())
A = list(map(int, input().split()))

def is_ok(arg):
    c = 0
    for i in range(N):
        c += arg//A[i]
    if c >= K:
        return True
    else:
        return False

def binary(left,right):
    while abs(right - left) > 1:
        mid = (right + left)//2
        if is_ok(mid):
            right = mid
        else:
            left = mid
    return right

print(binary(-1,10**9+1))
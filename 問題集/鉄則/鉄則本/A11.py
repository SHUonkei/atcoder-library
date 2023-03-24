N,X =map(int,input().split())
A = list(map(int, input().split()))

def is_ok(arg):
    if A[arg] >= X:
        return True
    else:
        return False

def binary(left,right):
    while (right - left) > 1:
        mid = (right+left)//2
        if is_ok(mid):
            right = mid
        else:
            left = mid
    return right

print(binary(-1,N)+1)
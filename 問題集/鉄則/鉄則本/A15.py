N = int(input())
A = list(map(int,input().split()))
b = set(A)
B = list(b)
B.sort()

def is_ok(arg,x):
    if B[arg] >= x:
        return True 
    else:
        return False

def meguru_bisect(ng, ok,x):
    while abs(ok - ng) >1 :
        mid =(ok +ng) // 2
        if is_ok(mid,x):
            ok = mid
        else:
            ng = mid
    return ok
ans = []
for i in range(N):
    x = meguru_bisect(-1,len(b)-1,A[i])
    ans.append(x+1)
print(*ans)
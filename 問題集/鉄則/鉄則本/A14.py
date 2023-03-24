N,K = map(int, input().split())
A = list(map(int ,input().split()))
B = list(map(int, input().split()))
C = list(map(int ,input().split()))
D = list(map(int, input().split()))

u = []
d = []

for i in range(N):
    for j in range(N):
        u.append(A[i]+B[j])
        d.append(C[i]+D[j])
u.sort()
d.sort()

def is_ok(arg,m):
    if d[arg] >= m:
        return True
    else:
        return False

def binary(left, right,m):
    while abs(right-left) > 1:
        mid = (right+left)//2
        if is_ok(mid,m):
            right = mid
        else:
            left = mid
    return right

    
for i in range(N**2):
    if K-u[i] < 0:
        continue
    x = K - u[i]
    if not d[binary(-1,N**2-1,x)] == x:
        continue
    print("Yes")
    exit()
    
print("No")
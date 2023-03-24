N = int(input())
S = list(map(int, input().split()))
Q = int(input())
T = list(map(int, input().split()))

x = 0
def is_ok(arg):
    #整数を越えればTを返す
    if S[arg] >= x:
        return True 
    else:
        return False

def meguru_bisect(ng, ok):
    while abs(ok - ng) >1 :
        mid =(ok +ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

count = 0
for i in range(Q):
    x = T[i]
    if S[meguru_bisect(-1,len(S)-1)] == x:
        count += 1
print(count)


A, B, K = map(int,input().split())
if A>=K:
    print(A-K,B)
    exit()
if A+B>=K:
    print(0,A+B-K)
    exit()
print(0,0)

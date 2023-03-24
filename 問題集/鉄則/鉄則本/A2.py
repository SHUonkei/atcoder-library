N,X = map(int,input().split())
A = list(map(int,input().split()))

a = set(A)
if X in a:
    print("Yes")
    exit()
print("No")
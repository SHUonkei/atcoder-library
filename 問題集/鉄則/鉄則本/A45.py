n,c= input().split()
n = int(n)

"演算として見る XORとかこういうのある"

def f(x):
    if x == "R":
        return 1
    if x == "B":
        return 2
    if x == "W":
        return 0

A = list(input())
now = 0
for i in range(n):
    now += f(A[i])

if now%3 == f(c):
    print("Yes")
    exit()
print("No")


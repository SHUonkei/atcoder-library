n,m,b = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))

suma = 0
sumc = 0

for i in range(n):
    suma += A[i]
for i in range(m):
    sumc += C[i]
    
print(n*m*b + m*suma + n*sumc)
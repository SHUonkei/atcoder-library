N,K = map(int,input().split())

c = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if N>=K-i-j>0:
            c +=1
print(c)
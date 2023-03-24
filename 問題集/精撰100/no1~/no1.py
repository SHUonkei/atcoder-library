while True:
    n,x = map(int, input().split())
    if n==0 and x ==0:
        exit()
    else:
        count=0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                for k in range(j+1,n+1):
                    if i !=k and i!=j and j!=k:
                        if i+j+k==x:
                            count+=1
        print(count)

#無限ループで while True
#for で　自然数扱うときは、0からなことを忘れない。
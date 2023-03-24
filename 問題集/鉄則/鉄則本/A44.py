N,Q = map(int,input().split())

A = [i+1 for i in range(N)]
now = 0
for i in range(Q):
    #print(A)
    query = list(map(int,input().split()))
    if query[0] == 1:
        if now == 0:
            A[query[1]-1] = query[2]
        if now:
            A[N-query[1]] = query[2]
    if query[0] == 2:
       now = abs(now-1)
    if query[0] == 3:
        if now == 0:
            print(A[query[1]-1])
        if now:
            print(A[N - query[1]])
    
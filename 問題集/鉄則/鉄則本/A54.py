Q = int(input())

q = {}

for i in range(Q):
    query = list(map(str,input().split()))
    if query[0] == "1":
        q[str(query[1])] = query[2] 
    if query[0] == "2":
        print(q[str(query[1])])
n,l = map(int,input().split())
E = l
W = 0
for i in range(n):
    a,b = input().split()
    if b == "E":
        E = min(int(a),E)
    else:
        W = max(int(a),W)

print(max(l-E,W))

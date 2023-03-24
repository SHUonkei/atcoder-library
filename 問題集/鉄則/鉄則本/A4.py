N = int(input())
ans = []
i = 0
while i <10:
    if N>>i & 1:
        ans.append(1)
    else:
        ans.append(0)
    i+=1

ans.reverse()

print("".join(map(str,ans)))

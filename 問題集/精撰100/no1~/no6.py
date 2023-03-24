n = int(input())
s = input()
count=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            now = str(i)+str(j)+str(k)
            ni = 0
            for l in range(n):
                if now[ni]==s[l]:
                    ni += 1
                if ni ==3:
                    count += 1
                    break
print(count)
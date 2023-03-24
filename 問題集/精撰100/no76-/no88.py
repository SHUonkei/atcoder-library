N = int(input())
ans = []
for i in range(N):
    ans.append(int(input()))

from collections import deque
def rle(s):
    tmp, count, ans = s[0], 1, deque()
    for i in range(1,len(s)):
        if tmp == s[i]:
            count += 1
        else:
            if i%2:
                tmp = s[i]
                count += 1
                if len(ans) == 0:
                    continue
                if tmp == ans[len(ans)-1][0]:
                    count += ans[len(ans)-1][1]
                    ans.pop()
                continue
            if len(ans)>0:
                if tmp == ans[len(ans)-1][0]:
                    ans[len(ans)-1][1] += count
                else:
                    ans.append([tmp,count])#s[i-1]の文字をencode
            else:
                ans.append([tmp,count])#s[i-1]の文字をencode
            tmp = s[i]
            count = 1
    if len(ans)>0:
        if tmp == ans[len(ans)-1][0]:
            ans[len(ans)-1][1] += count
            return ans
        else:
            ans.append([tmp,count])#s[i-1]の文字をencode
            return ans
    elif len(ans) == 0:
            ans.append([tmp,count])#s[i-1]の文字をencode
            return ans


data = rle(ans)
#print(data)
ans = 0
#print(data)
for i in range(len(data)):
    if data[i][0] == 0:
        ans += data[i][1]


print(ans)
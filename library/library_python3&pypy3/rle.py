def rle(s):
    tmp, count, ans = s[0], 1, []
    for i in range(1,len(s)):
        if tmp == s[i]:
            count += 1
        else:
            ans.append((tmp,count))#s[i-1]の文字をencode
            tmp = s[i]
            count = 1
    ans.append((tmp,count))#ラストだけループから外れてansに足されてないのでこの文章がいる
    return ans


"文字列に"
s = input()
x = rle(s)
ans = []
for i in range(len(x)):
    ans.append(x[i][0])
    ans.append(x[i][1])
    
print("".join(map(str,ans)))
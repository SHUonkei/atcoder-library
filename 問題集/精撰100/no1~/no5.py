a, b, c, x, y= map(int, input().split())
now = a*x + b*y
for i in range(max(x,y)+1):
    if x-i>= 0 and y-i >=0:
        now = min(now,a*(x-i)+b*(y-i)+c*2*i)
    if x-i < 0 and y- i >= 0:
        now = min(now,b*(y-i)+c*2*i)
    if x-i >= 0 and y-i < 0:
        now = min(now,a*(x-i)+c*2*i)
    if x-i < 0 and y-i < 0:
        now = min(now,c*(max(x,y)))
print(now)

#now =min(now,(2*c*i) + (a*max(x-i,0)) +(b*max(y-i,0)))
#で分岐いらんかった
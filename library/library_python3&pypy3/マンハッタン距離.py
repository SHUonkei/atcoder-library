n,q = map(int,input().split())
points = []
for i in range(n):
    x,y = map(int,input().split())
    points.append((x,y))
x_max = -10**18
x_min = 10**18
y_max = -10**18
y_min = 10**18

def mrot(x,y):
    return x-y,x+y

for i in range(n):
    x,y = points[i]
    xx,yy = mrot(x,y)
    x_max = max(xx,x_max)
    x_min = min(xx,x_min)
    y_max = max(yy,y_max)
    y_min = min(yy,y_min)
    


#print(x_max,x_min,y_max,y_min)
for i in range(q):
    p = int(input())
    x,y = points[p-1]
    xx= x-y
    yy = x+y
    print(max(abs(xx-x_max),abs(xx-x_min),abs(yy-y_max),abs(yy-y_min)))

T = int(input())
#3は2のまとまり

#   6 + 2,2
#or 8 + 2

#2,2,2,2,2 4,4,4
#4,4,2 4,2,2,2
# 6 6 6 4 4 2 2 2 2
# 6 4 ,  6 4, 6, 
#6, と2
#
for _ in range(T):
    n2,n3,n4 = map(int,input().split())
    n6 = n3//2
    if n6 > n4:
        print(n4 + min(n6,n2//2) + (n2 - min(n6,n2//2))//5)
    if n4 >= n6:
        print(n6 + min((n4-n6)//2,n2) + (n2 - min((n4-n6)//2,n2))//5)

# 
#    print(min(n6,n2)+(n2-min(n6,n2))//5)
    
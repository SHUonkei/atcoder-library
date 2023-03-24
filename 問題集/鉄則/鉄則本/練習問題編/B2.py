A,B =map(int,input().split())
divisor = {1,2,4,5,10,20,25,50,100}
for i in divisor:
    if A<= i<=B:
        print("Yes")
        exit()
print("No")
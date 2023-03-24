import math
def p(x):
    c = 0
    prime = set()
    
    for i in range(2,x+1):
        print(i)
        for j in prime:
            print(i,c)
            if i%j !=j:
                c+=1
        if c == len(prime):
            prime.add(i)
    
    return prime

print(p(20))
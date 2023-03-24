P = float(input())

h = 10**18
l = 0

def func(x):
    return P * pow(2, -(x/1.5)) + x

for _ in range(10**4):
    c1 = (2*l+h)/3
    c2 = (l+2*h)/3
    
    if func(c1) >= func(c2):
        l = c1

    else:
        h = c2

print(func(h))
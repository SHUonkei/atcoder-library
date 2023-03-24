P = float(input())

def f(x):
    return x + P*pow(2,-(x/1.5))

def g(low,high):
    d = high - low
    while d>10**(-4):
        c1 = (high+2*low)/3 
        c2 = (2*high+low)/3
        if f(c1) < f(c2):
            high = c2
        else:
            low = c1
        d = high - low
    return f(low)

print(g(0,10**18))
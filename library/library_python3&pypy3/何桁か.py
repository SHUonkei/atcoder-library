def f(x):
    i = 0
    while True:
        if 10**i <=x<10**(i+1):
            return i
        else:
            i += 1
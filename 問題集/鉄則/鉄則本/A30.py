mod = 10**9+7
n,r = map(int,input().split())

import math
u = math.factorial(n-r)%mod
v = (math.factorial(r)%mod * u)%mod
s = math.factorial(n)%mod

p = pow(v,mod-2,mod)

print((s*p)%mod)


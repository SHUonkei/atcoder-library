N = int(input())

n = N-N%3
m = N-N%5
k = N-N%15

print(n//3+m//5-k//15)
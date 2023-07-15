import sys
sys.setrecursionlimit(10 ** 9)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
 
n, MOD = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    edges[x].append(y)
    edges[y].append(x)
 
dp = [1] * n
def dfs1(pos, bpos):
    for npos in edges[pos]:
        if npos == bpos:
            continue
        dfs1(npos, pos)
        dp[pos] *= dp[npos] + 1
        dp[pos] %= MOD
dfs1(0, -1)
 
ans = [1] * n
def dfs2(pos, bpos):
    for npos in edges[pos]:
        ans[pos] *= dp[npos] + 1
        ans[pos] %= MOD
        
    left = [1]
    for npos in edges[pos]:
        left.append(left[-1] * (dp[npos] + 1) % MOD)
        
    right = [1]
    for npos in edges[pos][::-1]:
        right.append(right[-1] * (dp[npos] + 1) % MOD)
    right = right[::-1]
    for i, npos in enumerate(edges[pos]):
        if npos == bpos:
            continue
        dp[pos] = left[i] * right[i + 1] % MOD
        dfs2(npos, pos)
    
    
dfs2(0, -1)
print(*ans, sep="\n")
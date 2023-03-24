nn = 101
fa = [1] * (nn+1)
for i in range(nn):
    fa[i+1] = fa[i] * (i+1)

def kth_permutation(n, k):
    S = [i for i in range(n)]
    L = []
    for i in range(n):
        a = fa[n-1-i]
        j = k // a
        k %= a
        L.append(S[j])
        S = S[:j] + S[j+1:]
    return L

def id_of_permutation(L):
    ret = 0
    while len(L) > 1:
        a = len([l for l in L if l < L[0]])
        ret += a * fa[len(L) - 1]
        L = L[1:]
    return ret

"""
N があまり大きくないので、 
P が何番目の順列かを実際に計算する方法でも解くことができます。

「順列を与えたときにその ID （長さ 
N の順列のうち辞書順で何番目か）を返す関数」、
「ID を与えたときにその順列を返す関数」を事前に準備しておくと実装が簡単です。

ID の桁数はそれなりに大きくなるので、多倍長整数が使える言語・環境が必要になります。
"""

nn = 101
fa = [1] * (nn+1)
for i in range(nn):
    fa[i+1] = fa[i] * (i+1)

def kth_permutation(n, k):
    S = [i for i in range(n)]
    L = []
    for i in range(n):
        a = fa[n-1-i]
        j = k // a
        k %= a
        L.append(S[j])
        S = S[:j] + S[j+1:]
    return L

def id_of_permutation(L):
    ret = 0
    while len(L) > 1:
        a = len([l for l in L if l < L[0]])
        ret += a * fa[len(L) - 1]
        L = L[1:]
    return ret

N = int(input())
P = [int(a) - 1 for a in input().split()]
print(*[a + 1 for a in kth_permutation(N, id_of_permutation(P) - 1)])
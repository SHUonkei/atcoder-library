def dot(A1,A2,n):
    # n:行列のサイズ
    A = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                A[i][j] += A1[i][k]*A2[k][j]
    return A

def pow_mat(A,k,n):
    # A:累乗する行列, k:累乗数, n:行列Aのサイズ
    P = [[0]*n for _ in range(n)]
    
    for i in range(n):
        P[i][i] = 1
    
    while k:
        if k&1:
            P = dot(P,A,n)
        A = dot(A,A,n)
        k >>= 1
    
    return P
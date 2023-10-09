def array_mult(A, B):
    n = len(A)
    m = len(B[0])
    C = [[0] * m for i in range(n)]
    for k in range(len(A[0])):
        for i in range(n):
            for j in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C
    
M1 = [[1, 2, 3], [-2, 3, 7]]
M2 = [[1,0,0],[0,1,0],[0,0,1]]
print(array_mult(M1, M2))
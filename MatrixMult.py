def matrixmult (A, B):
    if (len(A[0])!=len(B)):
        return []
    c=[]
    for row in range(len(A)):
        caux=[]
        for col in range(len(B[0])):
            caux.append(0)
        c.append(caux)

    for i in range(0,len(A)):
        for j in range(0,len(B[0])):
            for k in range(0,len(B)):
                c[i][j] += A[i][k]*B[k][j]
    return c



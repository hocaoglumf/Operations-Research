import Matris_Transpose

def AltMatris(A,i,j):
    #B =  A[:i-1] + A[i :]
    B=[]
    for ii in range(0,len(A)):
        satir=[]
        if (ii!=i):
            for jj in range(0,len(A[0])):
                if (jj!=j):
                    satir.append(A[ii][jj])
        if (len(satir)>0):
            B.append(satir)

    D= Matris_Transpose.Transpose(B)
    return B

def Determinant(A):
    if (len(A)==2 and len(A[0])==2):
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    else:
        det =0
        for j in range(len(A[0])):
            X=AltMatris(A,0,j)
            det = det +(-1)**(j+2)*A[0][j]*Determinant(X)
    return det

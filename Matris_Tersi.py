import Matris_determinant
import  MatrixMult
import Matris_Transpose

def MatrixInverse(A):
    detA= Matris_determinant.Determinant(A)
    mtrx=[]

    for i in range(len(A)):
        satir=[]
        for j in range(len(A[0])):
            C=Matris_determinant.AltMatris(A,i,j)
            d = Matris_determinant.Determinant(C)
            satir.append((-1)**(i+j+2)*d)
        mtrx.append(satir)

    mtrx=Matris_Transpose.Transpose(mtrx)

    for i in range(len(mtrx)):
        for j in range(len(mtrx[0])):
            A[i][j]=1/detA*mtrx[i][j]

    return A

#A=[[1,4,2],[3,3,1],[2,0,1]]
#AI=MatrixInverse(A)
#print(AI)


import Functions

import Determinant
import MatrisIslemleri
import Matris_Tersi
import Matris_determinant
import MatrixMult


def MultiVarNewtonRaphson(Value, Gradient, MultiVarF):
    print(Value)
    X =MatrixMult.matrixmult(Matris_Tersi.MatrixInverse(Gradient(Value)), MultiVarF(Value))
    y=[]
    yy=[]
    for m in X:
        y.append(m[0])
    yy.append(y)
    FX=MatrisIslemleri.MatrisToplaCikar([Value], yy, -1)
    ii=0
    for i in range(len(Value)):
        if (abs(Value[i]-FX[0][i])<0.0001):
            ii += 1

    if (ii==len(Value)):
        return
    Value=FX[0]
    MultiVarNewtonRaphson(Value, Gradient, MultiVarF)
    return


MultiVarNewtonRaphson([1,1,1], Functions.Gradient1, Functions.MultiVarFonksiyon)
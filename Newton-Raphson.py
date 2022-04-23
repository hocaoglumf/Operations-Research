import matplotlib.pyplot as plt
import math
import FunctionGraph
import Functions

def DrawLine(x0,y0,x1,y1,mplt):
    pointsX=[]
    pointsY=[]
    for r in range(0,100):
        rr=r/100
        x0n = rr*x0 +(1-rr)*x1
        y0n = rr*y0 +(1-rr)*y1
        pointsX.append(x0n)
        pointsY.append(y0n)

    mplt.plot(pointsX, pointsY)
    return mplt

def NewtonRaphson(Fonk, Deriv, initValue, resolution):
    i=0
    print("İterasyon", "  Yeni Değer", "    Önceki Değer")
    print("---------------------------------------------")
    sonuc=""
    b=0
    while (True):
        i +=1
        initValueNew = initValue - Fonk([initValue])/Deriv([initValue])
#        m=DrawLine(initValue, Deriv([initValue]), initValueNew,Deriv([initValueNew]), mplt)
      #  m.show()
        print(i, "   ", initValueNew, "    ", initValue, sonuc)
        if (abs(initValueNew-initValue) <resolution):
            print("Çözüm ", initValueNew, "  ", Fonk([initValueNew]))
            break
        else:
            initValue = initValueNew

NewtonRaphson(Functions.FuncNewtonExp, Functions.FuncNewtonExpDeriv, 10, 0.01)

import matplotlib.pyplot as plt
import math
import FunctionGraph
import Functions

# Maksimizasyon problemlerini çözer

def DichotomousSearch(Fonk, interval, delta):
    i=0
    print("İterasyon", "  Aralık ", "    Fonksiyon Değerleri")
    print("---------------------------------------------")
    sonuc=""
    b=0
    while (True):
        i +=1
        xL= (interval[0] + interval[1]-delta)/2
        fL= Fonk([xL])
        xR= (interval[0] + interval[1]+delta)/2
        fR= Fonk([xR])
        print(i, " [", interval[0], ",", interval[1], "]", " f(xL):", fL, "  f(xR) :" , fR)
        if (fL < fR ):
            s=xL
            interval[0]=xL
        elif (fL>fR):
            s=xR
            interval[1]=xR
        else:
            s=xR
            interval[0]=xL
            interval[1]=xR

        if (abs(interval[0]-interval[1])<delta ):
            print("[",interval[0], ",", interval[1],"]")
            print ("Sonuç : ", s, Fonk([s]) )
            break

#DichotomousSearch(Functions.Dichotomous, [2,5], 0.0001)
DichotomousSearch(Functions.FluidDynamics, [0,4000], 0.0001)

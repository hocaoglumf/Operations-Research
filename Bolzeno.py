import matplotlib.pyplot as plt
import math
import FunctionGraph
import Functions

def Bolzeno(Deriv, interval, epsilon):
    i=0
    print("İterasyon", "  Aralık ", " Orta Nokta ","    Fonksiyon Değeri ")
    print("---------------------------------------------")
    sonuc=""
    b=0
    while (True):
        initValue=(interval[0]+interval[1])/2

        i +=1

        initValueNew = Deriv([initValue])
        if (initValueNew >=0):
            interval[0]=initValue
        else:
            interval[1] = initValue

        print(i, "  ",  interval," ", (interval[1]+interval[0])/2, "   ",initValueNew )
        if (abs(interval[1]-interval[0])<=2*epsilon):
            print("x ", (interval[0]+interval[1])/2)
            break

Bolzeno(Functions.BolzenoExp, [0,3],0.00001)
#Bolzeno(Functions.FluidDynamicsDeriv, [0,2],0.00001)
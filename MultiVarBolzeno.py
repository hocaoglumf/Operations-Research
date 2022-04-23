import matplotlib.pyplot as plt
import math
import FunctionGraph
import Functions


def MultivarBolzeno(DerivL, intervalL, epsilonL):
    control=0
    iterD=0
    print ("İterasyon   ", "Değişken Aralığı ")
    while True:
        iterD +=1
        iter = 0
        control=0
        for i in range(0,len(DerivL)):
            iter +=1
            Deriv=DerivL[i]
            if (intervalL[i][1]-intervalL[i][0]<=2*epsilonL[i]):
                control+=1
                continue

            initValues=[]
            for i in range(0,len(DerivL)):
                initValues.append((intervalL[i][0] + intervalL[i][1]) / 2)

            initValueNew, n = Deriv(initValues)
            if (initValueNew >=0):
                intervalL[n][0]=initValues[n]
            else:
                intervalL[n][1] = initValues[n]

        #print ("İterasyon :",str(iterD))
        s=str(iterD)+"-"
        for i in range(0,len(DerivL)):
            s +="x"+str(i+1)+"="+ str(intervalL[i])+"/ "
        print(s)
        if (control==len(epsilonL)):
            for i in range (0,len(DerivL)):
                print("x"+str(i+1)+"=", (intervalL[i][0]+intervalL[i][1])/2)
            break


#MultivarBolzeno([Functions.BolzenoDerivX1, Functions.BolzenoDerivX2, Functions.BolzenoDerivX3], [[-1,1],[0,1],[1,2]],[0.001,0.001,0.0001])
MultivarBolzeno([Functions.BolzenoVizeDerivX1, Functions.BolzenoVizeDerivX2], [[-1,1],[0,1]],[0.001,0.001])

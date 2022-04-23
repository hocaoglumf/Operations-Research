import matplotlib.pyplot as plt
import math
import Functions

def Graph(Func, x0,x1,step):
    x_Axis = []
    y_Axis = []
    x=x0
    while (x<x1):
        y=Func([x])
        x_Axis.append(x)
        y_Axis.append(y)
        x +=step
    plt.plot(x_Axis, y_Axis)
    #plt.show()
    return plt


#Graph(Functions.FuncNewtonDerivExp, -10,10,0.01)
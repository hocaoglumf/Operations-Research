import math
import Functions

def Golden_Section_Search(Function, interval, epsilon):
    iteration=0
    print ("İterasyon ", "Aralık ", "Hesaplanan Değer")
    print("-------------------------------------------")
    while True:
        a=interval[0]+(5**.5-1)/2*(interval[1]-interval[0])
        b=interval[1]-(5**.5-1)/2*(interval[1]-interval[0])

        fa=Function([a])
        fb=Function([b])
        if (fa>=fb):
            interval[0]=b
        else:
            interval[1]=a
        iteration +=1
        print ('{:2}'.format(iteration)," [",'{:9}'.format(round(interval[0],5)),",",'{:9}'.format(round(interval[1],5)),"] f(a)=", '{:9}'.format(round(fa,5)), "  f(b)=",'{:9}'.format(round(fb,5)))
        if (abs(a-b)<=epsilon):
            print("--------------------------------------")
            print(" x = ",'{:18}'.format((interval[0]+interval[1])/2))
            print("--------------------------------------")
            break


#Golden_Section_Search(Functions.GoldenExp,[0,3],0.001)
#Golden_Section_Search(Functions.GutterFunction, [0,3],0.05)


Golden_Section_Search(Functions.FluidDynamics,[0,9],0.00001)
import math
import Functions

def Golden_Section_Search(Function, varName, interval, epsilon):
    iteration=0
    print ("İterasyon ", "Aralık ", "Hesaplanan Değer")
    print("-------------------------------------------")
    i=-1
    while True:
        i+=1
        if (i == len (interval)):
            i=0
        while True:
            a=interval[i][0]+(5**.5-1)/2*(interval[i][1]-interval[i][0])
            b=interval[i][1]-(5**.5-1)/2*(interval[i][1]-interval[i][0])

            interval_l=[]
            interval_u=[]
            for j in range(0,len(interval)):
                if (i==j):
                    pass
                else:
                    interval_l.append(interval[j][1])
                    interval_u.append(interval[j][1])

            interval_l.insert(i,a)
            interval_u.insert(i,b)

            fa=Function(interval_l)
            fb=Function(interval_u)
            if (fa>=fb):
                interval[i][0]=b
            else:
                interval[i][1]=a
            iteration +=1
            print ('{:2}'.format(iteration)," [",'{:18}'.format(interval[i][0]),",",'{:18}'.format(interval[i][1]),"] f(a)=", '{:18}'.format(fa), "  f(b)=",'{:18}'.format(fb))
            if (abs(interval[i][1]-interval[i][0])<=epsilon):
                print("--------------------------------------")
                for h in range(len(varName)):
                    print(varName[h]," =",'{:18}'.format((interval[h][0]+interval[h][1])/2))
                print("--------------------------------------")
                break


Golden_Section_Search(Functions.GutterFunction,["l","theta"], [[0,3],[0,math.pi/6]],0.05)



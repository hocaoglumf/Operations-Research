import Functions
import math

def FuncP(Param):
    return Param[0]*(5*math.pi-Param[0])


def AralikSil(i,j,L):
    del L[i:j]
    return L

def Search(Aralik, Function, epsilon):
    if (Aralik[1]-Aralik[0] <=epsilon):
        return 0
    points=[]
    l=Aralik[1]-Aralik[0]
    adim=l/4
    for i in range(1,4):
        points.append(Aralik[0]+i*adim)
    fonk=[]
    for i in points:
        fonk.append(Function([i]))
    print(points, "    ", fonk)
    indx= fonk.index(max(fonk))

    if (indx==0):
        inds =0
    else:
        inds = indx -1
    sol=points[inds]
    sag = points[indx+1]

#    if (sag>= len(fonk)):
#        sag=points[len(fonk)-1]+adim

    Search([sol, sag], Function, epsilon)

Search([0,20],FuncP, 1)
Search([0,2],Functions.FluidDynamics,0.0001)
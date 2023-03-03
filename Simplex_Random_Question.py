from scipy.optimize import linprog
import random
import math
import SinifListesiOku
import Sinif_Soru_Yaz



def CreateLinearProgrammingProblem(numberofconst, numberofvar):
    mtrx=[]
    for i in range(numberofconst):
        s=[]
        for j in range(numberofvar):
            xx=0
            while xx==0:
                xx=random.randint(-10,10)
            s.append(xx)
        mtrx.append(s)

    rhs=[]
    for i in range(numberofconst):
        rhs.append(random.randint(-20,20))

    obj=[]
    for j in range(numberofvar):
        xx=0
        while xx==0:
            xx=random.randint(-10,10)
        obj.append(xx)

    lhs_ineq=[]
    lhs_eq=[]
    rhs_ineq=[]
    rhs_eq=[]
    sgnin=[]
    sgneq=[]

    for i in range(numberofconst):
        rnd = random.randint(1, 100)
        if (rnd<30):
            lhs_eq.append(mtrx[i])
            rhs_eq.append(rhs[i])
            sgneq.append("=")
        else:
            lhs_ineq.append(mtrx[i])
            rhs_ineq.append(rhs[i])
            sgnin.append("<=")

    bnd=[]

    for i in range(numberofvar):
        bnd.append((0, float("inf")))
    success=False
    opt=None
    if (len(lhs_ineq)>0 and len(lhs_eq)>0):
        opt =linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
                   A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
                   method="revised simplex")
        success=opt.success

    return success, obj, sgnin, sgneq, lhs_ineq, rhs_ineq, lhs_eq, rhs_eq,opt

def Arrange(obj,sgnin,sgneq, lhs_ineq, rhs_ineq, lhs_eq, rhs_eq,opt):
    for i in range(len(rhs_ineq)):
        if (rhs_ineq[i]<0):
            rhs_ineq[i]=-1*rhs_ineq[i]
            for j in range(len(lhs_ineq[i])):
                lhs_ineq[i][j]=-1*lhs_ineq[i][j]
            sgnin[i]=">="
    return obj,sgnin,sgneq, lhs_ineq, rhs_ineq, lhs_eq, rhs_eq,opt


def Write(obj,sgnin,sgneq, lhs_ineq, rhs_ineq, lhs_eq, rhs_eq,opt):
    print("İterasyon Sayısı:", opt.nit)
    problem=""
    sayalim=0
    carpan=1
    goal = "Min z = "
    for i in obj:
        if (i<0):
            sayalim +=1
    if (sayalim>len(obj)%2):
        carpan=-1
        goal="Max z = "
    for i in range(len(obj)):
        a=carpan*obj[i]
        if (a<0 or i==0):
            t=""
        else:
            t="+"

        goal=goal+t+ str(a)+"x"+str(i+1)+" "
    print(goal)
    problem +=goal +chr(13)
    for i in range(len(lhs_ineq)):
        s=""
        for j in range(len(lhs_ineq[0])):
            if (j >0):
                if (lhs_ineq[i][j] < 0):
                    t=""
                else:
                    t= "+"
            else:
                t=""
            s=s+ t+ str(lhs_ineq[i][j])+ "x"+ str(j+1)
        print(s +sgnin[i]+ str(rhs_ineq[i]))
        problem += s +sgnin[i]+ str(rhs_ineq[i])+chr(13)

    for i in range(len(lhs_eq)):
        s=""
        for j in range(len(lhs_eq[0])):
            if (j >0):
                if (lhs_eq[i][j] < 0):
                    t=""
                else:
                    t= "+"
            else:
                t=""
            s=s+ t+str(lhs_eq[i][j])+ "x"+ str(j+1)
        print(s +sgneq[i]+ str(rhs_eq[i]))
        problem += s +sgneq[i]+ str(rhs_eq[i])+chr(13)

    print("Optimum :", opt.x)
    return problem



sinif=SinifListesiOku.ReadSinif("C://Academic//Dersler//OR-1//Sinavlar//2021//liste.xlsx")
scn=0
number=len(sinif)

while (scn<number):
    numberofvar = random.randint(3, 3)
    numberofconst = random.randint(2, 4)
    success, obj, sgnin,sgneq, lhs_ineq, rhs_ineq, lhs_eq, rhs_eq,opt=CreateLinearProgrammingProblem(numberofconst, numberofvar)
    if (success):
        n=0
        signc=False
#        for i in sgn:
#            signc =signc or i==">=" or i=="="

        nk=0
        nb=0
        ne=len(sgneq)
        for i in sgnin:
            if (i=="<="):
                nk +=1
            if (i == ">="):
                nb += 1
        if (nb>=1 and nk>=1 and ne>=1):
            signc =True


        for i in opt.x:
            if (math.modf(i)[0]>0):
                n +=1
        if (n>=2 and len(rhs_ineq) + len(rhs_eq)>=3 ):
            obj, sgnin,sgneq, lhs_ineq, rhs_ineq, lhs_eq, rhs_eq, opt=Arrange(obj, sgnin, sgneq, lhs_ineq, rhs_ineq, lhs_eq, rhs_eq, opt)
            if (opt.nit>=2 and opt.nit <=4):

                problem = Write(obj, sgnin,sgneq, lhs_ineq, rhs_ineq, lhs_eq, rhs_eq, opt)
                sinif[scn].append(problem)
                sinif[scn].append(list(opt.x))
                scn +=1
            #SendEmail(person, problem)
Sinif_Soru_Yaz.WriteQuestion(sinif, "C://Academic//temp.xls")
for i in sinif:
    print (i)
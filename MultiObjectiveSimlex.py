# Doç. Dr. M. Fatih Hocaoğlu
# İstanbul Medeniyet Üniversitesi
#
# Bu kod birden fazla amaı olan bir doğrusal modeli
# Simpleks kullanarak çözer.
# Birinci amaca göre çözülen problem ikinci amaç için çözlürken
# önceden çözülen amaç kısıt olarak probleme eklenir. Modele kısıt olarak eklenirken,
# kısıt >= formunda eklenir. amaç katsayıları kısıtın sol tarfnı amaç değeri
# sağ tarafı belirler.
#
# Simpleks problemi maksimizasyon olarak çözer.
# Problem tanımı için aşağıdaki değişkenler tanımlar:
# goals listesinde her bir amaç için değişken katsayılarını içeren bir liste yazılır.
#       amaç katsayıları kanonik formda birinci amaç dikkate alınarak yazılır.
# problem matrisi kanonik formda kısıt katsayılarını içeren bir matris olarak girilir.
#       Her bir kısıt bir liste formundadır.
# variables birinci amaç dikkate aınarak değişkenleri içerir. Sonradan eklenecek
#       kısıtlar için değişkenler çözüm esnasında belirlenir.
# baseCoeff başlangıçta temelde yeralan değişkenler amaç katsayılarıyla birer ikili
#       formunda yazılır.
#
# Çözüm dual simpleks'i içerir. Eğer sağ taraf değişkenlerinde negatif varsa önce
# dual simplks ile çözüm ilerletilir.
#

def WriteProblem():
    for i in problem:
        print (i)
    print ("-----------------")

def C_Z():
    C=problem[len(problem)-1]
    C_Z=[]
    for i in range(len(variables)):
        z=0
        for j in range(len(baseCoeff)):
            y,x=baseCoeff[j][1],problem[j][i]
            z +=y*x
        C_Z.append(C[i]- z)
    return C_Z

def EnteringVariable(CZ):
    enb=CZ[0]
    ei=0
    for i in range(1,len(CZ)):
        if (enb<CZ[i]):
            enb=CZ[i]
            ei=i

    return ei

def LeavingVariable(entering):
    leaving=[]

    for i in range(len(baseCoeff)):
        if (problem[i][entering]>0):
            leaving.append(problem[i][len(problem[0])-1]/ problem[i][entering])
        else:
            leaving.append(99999999999999999)

    enk=leaving[0]
    li=0
    for i in range(1,len(leaving)):
        if (leaving[i]>0 and leaving[i]<enk):
            li=i
            enk=leaving[i]
    return li

def IsFeasible():
    b=True
    for i in range(len(baseCoeff)):
        b = b and problem[i][len(problem[0]) - 1]>=0
    return b

def IsOptimum():
    cz=C_Z()
    b=True
    for i in range(len(cz)):
        b = b and cz[i]<=0.0000

    return b

def NewTable(ei,li):
    pivot=problem[li][ei]

    new_problem=[]
    for i in range(len(problem)-1):
        row=[]
        for j in range(len(problem[0])):
            row.append(0)
        new_problem.append(row)
    #pivot satırı
    for i in range(len(problem[0])):
        new_problem[li][i]=problem[li][i]/pivot

    #pivot sütunu
    for i in range(len(baseCoeff)):
        new_problem[i][ei]=int(li==i)

    #diğer kısımlar
    for i in range(len(problem)-1):
        for j in range(len(problem[0])):
            if (li==i or ei==j):
                continue
            else:
                new_problem[i][j]=problem[i][j]-problem[li][j]*problem[i][ei]/pivot

    for i in range(len(problem)-1):
        for j in range(len(problem[0])):
            problem[i][j]=new_problem[i][j]
    return

def UpdateBaseCoeff(li,ei):
    baseCoeff[li][0]=variables[ei]
    baseCoeff[li][1]=problem[len(problem)-1][ei]

    return

def DefineGoalAsConstraint(number,Z):
    constraint = goals[number]
    for i in range(len(constraint)):
        constraint[i]=-1*constraint[i]

    constraint= constraint + [0]*(len(problem)-1)
    constraint.append(1)
    constraint.append(-1*Z)
    M=[]
    for i in range(len(problem)-1):
        s=[]
        for j in range(len(problem)):
            s.append(0)
        M.append(s)

    for i in range(len(M)):
        M[i][i]=1
    j=0

    for i in range(len(problem)-1):
        rhs=problem[i][len(problem[i])-1]
        problem[i].pop(len(problem[i])-1)
        problem[i]=problem[i]+M[j]+[rhs]
        j +=1

    problem.pop(len(problem)-1)
    problem.append(constraint)
    M=-99999999
    for i in range(len(problem)):
        goals[number+1].append(M)
    goals[number+1].append(1)

    problem.append(goals[number+1])
    baseCoeff.clear()
    #variables.clear()
    for i in range(len(problem)-1):
        baseCoeff.append(["A_"+str(number+1)+str(i+1),M])
        variables.append("A_" + str(number + 1)+str(i+1))
    tobe=baseCoeff[len(baseCoeff)-1][0]
    baseCoeff[len(baseCoeff)-1][0]=tobe.replace('A','S')
    tobe=variables[len(variables)-1]
    variables[len(variables)-1]=tobe.replace('A','S')

    return 0

def CalculateGoal(number):
    z=0
    for j in range(len(baseCoeff)):
        y, x = baseCoeff[j][1], problem[j][len(problem[0])-1]
        z += y * x
    return z


def DualLeaving():
    enb=-1 # problem[0][len(problem[0])-1]
    indx=-1
    for i in range(len(problem)):
        if (problem[i][len(problem[i])-1]<0 and abs(problem[i][len(problem[i])-1])>enb):
            indx=i
            enb=abs(problem[i][len(problem[i])-1])


    return indx

def InBase(vr):
    for i in baseCoeff:
        if (i[0]==vr):
            return True
    return False

def DualEntering(li):
    enteringList=[]
    for i in range(len(problem[li])-1):
        if (problem[li][i]<0 and not(InBase(variables[i]))):
            enteringList.append(problem[len(problem)-1][i]/problem[li][i])
        else:
            enteringList.append(99999999)
    min=enteringList[0]
    indx=0
    for i in range(len(enteringList)-1):
        if (abs(enteringList[i])<min):
            min =enteringList[i]
            indx=i
    return indx


"""
max z = 2x + 5y + 2z
max G = 4x + 2y + 8z
st
2x + 3y + z <= 4.5
3x + 2y + z <= 11
z          <= 5
x,y,z >= 0
"""
variables=["x1","x2","x3","s1","s2","s3"]

goalValues=[]
goals=[[2,5,2,0,0,0], [4,2,8,0,0,0]]
baseCoeff=[["s1",0],["s2",0],["s3",0]]
problem=[[2,3,1,1,0,0,4.5],
         [3,2,1,0,1,0,11],
         [0,0,1,0,0,1,5],
         goals[0]]
goalNumber=0
while True:
    while True:
        opt=IsOptimum()
        feasible=IsFeasible()
        if (opt and feasible):
            z=CalculateGoal(goalNumber)
            WriteProblem()
            print(baseCoeff)
            print("Goal :", z)
            print(C_Z())
            goalValues.append(z)
            break

        if (not(IsFeasible())):
            li=DualLeaving()
            ei=DualEntering(li)

        if (IsFeasible()):
            cz=C_Z()
            ei=EnteringVariable(cz)
            li=LeavingVariable(ei)

        UpdateBaseCoeff(li,ei)
        WriteProblem()
        print("*",cz)
        NewTable(ei,li)
        WriteProblem()
        print(baseCoeff)
    if (len(goals)-1>goalNumber):
        DefineGoalAsConstraint(goalNumber,goalValues[goalNumber])
        goalNumber +=1
    else:
        break

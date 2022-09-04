
import random
jobs=[1,2,3,4,5,6]
lastNSolution=20
MaxtIter=1000

dueDates={1:27,2:22,3:44,4:26,5:43,6:22}
penalties={1:17,2:13,3:35,4:14,5:32,6:11}

processTimes={1:3,2:17,3:16,4:4,5:12,6:5}

def TheBestSolution():
    global solutions
    theBestSolution=float(solutions[list(solutions.keys())[0]])
    value=list(solutions.keys())[0]
    for i in solutions.keys():
        v= float(solutions[i])
        if (theBestSolution>=v):
            theBestSolution=solutions[i]
            value=i

    return theBestSolution, value

def Penalty(L):
    totalProcessingTime=0
    tardeness=0
    penalty=0
    for i in L:
        totalProcessingTime +=processTimes[i]
        diff=totalProcessingTime-dueDates[i]
        if (diff>0):
            penalty +=penalties[i]*diff

    return penalty

def Member(L,r1,r2):
    return r1*10+r2 in L.keys() or r2*10+r1 in L.keys()

def DecreaseTabuList(L):
    for i in L.keys():
        L[i]=L[i]-1
    tabu_aux={}
    for i in L.keys():
        if (L[i]>0):
            tabu_aux[i]=L[i]
    return tabu_aux


def Aspiration(rnd1, rnd2, L):
    global tabuList
    if (rnd1==rnd2 or not(Member(tabuList,rnd1+1,rnd2+1))):
        return 0

    LL=[]
    for i in L:
        LL.append(i)

    LL[rnd1], LL[rnd2]=LL[rnd2], LL[rnd1]
    pasp=Penalty(LL)
    cst, _=TheBestSolution()
    if (pasp<cst):
        L[rnd1], L[rnd2]=L[rnd2], L[rnd1]
        tabuList[L[rnd1]*10+L[rnd2]]=0
        tabuList[L[rnd2] * 10 + L[rnd1]] = 0
        return 1
    return 0

def Swap(L):
    global tabuList
    rnd1=0
    rnd2=0
    b=True
    while rnd1==rnd2 and b:
        rnd1=random.randint(0,len(jobs)-1)
        rnd2=random.randint(0,len(jobs)-1)
        aspP=Aspiration(rnd1, rnd2,L)
        if (aspP==1):
            break
        b = not(Member(tabuList,rnd1,rnd2))

    L[rnd1], L[rnd2]=L[rnd2], L[rnd1]
    tabuList=DecreaseTabuList(tabuList)
    tabuList[L[rnd1]*10+L[rnd2]]=3
    tabuList[L[rnd2]*10+L[rnd1]]=3
    return L



solution=jobs
solutions={}
tabuList={}
oldBest=0
lastSolutionIter,iter=0,0
while True:
    ftns=Penalty(solution)
    solutions[str(solution)]=ftns
    solution=Swap(solution)
    best,value=TheBestSolution()
    if (oldBest==best):
        lastSolutionIter +=1
    else:
        lastSolutionIter=0
    if (lastSolutionIter>=lastNSolution):
        break

    iter +=1
    if (iter>=MaxtIter):
        break
    oldBest=best
    print(best, "  ", value)

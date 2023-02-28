import random
def Function(Param):
    x1 = Param[0]
    x2 = Param[1]
    x3 = Param[2]
    x4 = Param[3]
    return 100*(x2-x1**2)**2 +(1-x1**2)**2+x3**2-x4**2
class Colony:
    def __init__(self):
        self.colony={}
        self.failureLimit=0
        self.selection=[99999999999,0]

    def SetFailureLimit(self,FL):
        self.failureLimit=FL

    def Join(self,bee):
        self.colony[bee.id]=bee
        self.failure=0

    def NewValue(self,phi):
        for i in self.colony.keys():
            self.colony[ i].NewValue(len(self.colony),phi)

    def CheckLimit(self):
        for i in self.colony.keys():
            if (self.colony[i].failure == self.failureLimit):
                self.ReGenerate(i)

    def ReGenerate(self, id):
        N=len(self.colony[id].Param)
        self.colony[id].Param=[]
        self.colony[id].failure=0
        for i in range(N):
            self.colony[id].Param.append(random.random())
        return

    def MonteCarlo(self):
        cum=0
        topl=0
        for i in self.colony.keys():
            topl += 1/self.colony[ i].Evaluate()

        for i in self.colony.keys():
            cum += 1/self.colony[ i].Evaluate()/topl
            self.colony[ i].cumFitness= cum

        chs=random.random()
        i=0
        chsId=0
        for i in self.colony.keys():
            if (self.colony[i].cumFitness >chs):
                chsId = i
                break
        return chsId



class Bee:
    def __init__(self,id):
        self.id=id
        self.Param=[]
        self.colony=None
        self.cumFitness=0
        self.failure=0


    def SetColony(self,colony):
        self.colony=colony

    def Init(self, N, intervals):
        for i in range(N):
            a=intervals[i][0]*100
            b=intervals[i][1]*100
            self.Param.append(random.randint(a,b)/100)

    def Evaluate(self):
        return Function(self.Param)

    def ChooseNeighbourPlace(self, N):
        i2=self.id
        i3=self.id
        while i2==self.id:
            i2= random.randint(1,N)

        i3= random.randint(0,N-1)

        return i2,i3

    def NewValue(self,N,phi):
        i2,i3=self.ChooseNeighbourPlace(N)
        stored=self.Param[i3]
        oldValue=self.Evaluate()
        self.Param[i3] += phi*(self.Param[i3]-self.colony.colony[i2].Param[i3])

        newValue=self.Evaluate()
        epsilon = abs(newValue)
        if (self.colony.selection [0]> epsilon):
            self.colony.selection=[epsilon, self.id, [newValue, self.Param]]
        if (abs(oldValue) <=abs(newValue)):
            self.Param[i3]=stored
            self.failure += 1
        else:
            self.failure=0
        print (self.Param, "  f:", newValue)
        return 0

    def UpdatePosition(self):
        return 0




def Solver(Maxitr, epsln, flimit, nBees, numberofVariables, intervals):
    MAXITR=Maxitr
    epsilon =epsln
    colony=Colony()
    colony.SetFailureLimit(flimit)
    for i in range(1,nBees+1):
        b=Bee(i)
        b.Init(numberofVariables, intervals)
        colony.Join(b)
        b.SetColony(colony)


    iter=0
    colony.NewValue(.25)
    while True:
        chsBee=colony.MonteCarlo()
        phi=random.randint(10,50)/100
        colony.colony[chsBee].NewValue(numberofBees,phi)
        colony.CheckLimit()
        iter +=1
        if (colony.selection[0]<=epsilon):
            print (iter, " Çözüm : ", colony.selection)
            break
        if (iter==MAXITR):
            break

numberofVariables=int(input("Değişken sayısı "))
intervals=[]
for i in range(numberofVariables):
    alt=int(input(str(i+1)+". değişken alt aralığı "))
    ust=int(input(str(i+1)+". değişken üst aralığı "))
    intervals.append([alt,ust])

numberofBees=int(input("Arı Sayısı "))
mxiter=int(input("Maksimum iterason "))
eps=float(input("Epsilon ") )
fl=int(input("Hata Limiti "))

Solver(mxiter, eps, fl, numberofBees, numberofVariables, intervals)


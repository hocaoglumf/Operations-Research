class Node:
    def __init__(self, x, val=[0,0]):
        self.parent=x
        self.value=val
        self.cumulative=list()
        self.valueSet=[]

    def Empty(self):
        return len(self.valueSet) == 0

    def AddValues(self, V):
        if (self.Empty()):
            for i in V:
                self.valueSet.append(Node(self,i))
        else:
            for i in self.valueSet:
                i.AddValues(V)

    def Write(self):
        print(self.value)
        s=""
        for i in self.valueSet:
            s += str(i.value) + " / "
        print (s)
        for i in self.valueSet:
            i.Write()

    def Cumulative(self, xx=[0,0]):
        a=self.value[0]
        x=xx[0] + self.value[0]
        y=xx[1] + self.value[1]
        self.cumulative=[x, y]

        if (self.Empty()):
            if (self.cumulative[0] ==9):
                print(self.cumulative)
        else:
            for i in self.valueSet:
                i.Cumulative(self.cumulative)

    def Parent(self):
        if (self.Empty()):
            print("no memeber", self.value)
            return
        if (self.parent==None):
            pass
        else:
            print("parent ",self.value, "  ",self.parent.value)
        for i in self.valueSet:
            i.Parent()





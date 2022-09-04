import random
import Codes.GAs.BinaryDecimalConverter

def GenerateValues(Param, l):
    maxX1=Param[0][1]
    minX1=Param[0][0]

    maxX2=Param[1][1]
    minX2=Param[1][0]

    rand1=random.randint(0,100)
    rand2=random.randint(0,100)
    x1= minX1 +((maxX1-minX1)/(2**l-1))*rand1
    x2= minX2 +((maxX2-minX2)/(2**l-1))*rand2
    return x1, x2, rand1, rand2

def BinaryJustify(binary, l):
    if (not (l - len(binary) == 0)):
        binary = (l - len(binary)) * "0" + binary
    return binary

def Function(P):
    x1=P[0]
    x2=P[1]
    return (-2*x1**2 + x2**2)


def GenerateCandidateSolutions(n):
    maks = -999999999999
    for i in range(n):
        x1,x2,r1,r2=GenerateValues([[-.5,.5],[-.5,.5]],l)
        f=Function([x1,x2])
        binR=[]
        binR.append(Codes.GAs.BinaryDecimalConverter.dec_to_bin(r1))
        binR.append(Codes.GAs.BinaryDecimalConverter.dec_to_bin(r2))
        for k in [0,1]:
            binary = str(binR[k])
            bnr= BinaryJustify(binary,l)
            binR[k]=bnr

        if (maks <= f):
            saved=f
            savedR1=r1
            savedR2=r2
            savedX1=x1
            savedX2=x2
            savedbinR1=binR[0]
            savedbinR2=binR[1]
            maks=f
        binr1=str(Codes.GAs.BinaryDecimalConverter.dec_to_bin(r1))
        binr2=str(Codes.GAs.BinaryDecimalConverter.dec_to_bin(r2))
        res.append([f,x1,x2,r1,r2, binR[0], binR[1]])

    tabu.append([f,x1,x2,r1,r2, binR[0], binR[1]])

def InTabu(f, tabu):
    for i in tabu:
        if (abs(i[0]-f[0])<=0.0001):
            return True
    return False

def SwitchGene(L,x):
    sL=str(L)
    a=str(int(not(int(sL[x]))))
    sL = sL[0:x] + a+ sL[x + 1:]
    return sL

def ChangeBinaries(geneTobeChanged):

    for i in res:
        f = InTabu(i, tabu)
        if (not (f)):
            for j in range(5, 7):
                binary = str(i[j])
                bnr = BinaryJustify(binary, l)
                i[j]=SwitchGene(bnr, geneTobeChanged)
                i[j-2]=Codes.GAs.BinaryDecimalConverter.bin_to_dec(i[j])

def Evaluate():
    for i in res:
        rs1=i[5]
        rs2=i[6]
        x1=par[0][0]+((par[0][1]-par[0][0])/(2**l-1))*Codes.GAs.BinaryDecimalConverter.bin_to_dec(i[5])
        x2=par[1][0]+((par[1][1]-par[1][0])/(2**l-1))*Codes.GAs.BinaryDecimalConverter.bin_to_dec(i[6])
        i[1]=x1
        i[2]=x2
        i[0]=-2*x1**2 + x2**2

    for i in res:
        if (i[0]> tabu[0][0]):
            tabu.clear()
            tabu.append(i)

def PrintSolution():
    print(geneTobeChanged, "------------------")
    for i in res:
        line = ""
        b=InTabu(i,tabu)
        ek=""
        if (b):
            ek="*"

        for j in i:
            if (type(j) ==str):
                line +=j + "&"
            else:
                line +=str(round(j,5)) + "&"
        line +=ek
        print(line)

n=5
l=8

res=[]
tabu= []
par = [[-.5, .5], [.5, .5]]
GenerateCandidateSolutions(n)
geneTobeChanged=l-1
PrintSolution()

while geneTobeChanged>=0:
    ChangeBinaries(geneTobeChanged)
    Evaluate()
    PrintSolution()
    geneTobeChanged -=1

print ("tabu")
print (tabu[0])
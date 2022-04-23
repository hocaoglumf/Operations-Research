# Yöneylem Araştırması
# Doç. Dr. M. Fatih Hocaoğlu
# İstanbul Medeniyet Üniversitesi
# Agena BST
def SatirEkle(M):
    M.append([0]*n)
    return M

def SutunEkle(M):
    for i in M:
        i.append(0)
    return M

def FindMin():
    min = 9*10**10
    plce=[-1,-1]
    for i in range(len(satirK)):
        for j in range(len(kolonK)):
            if (matris[i][j]<=min and satirK[i]>0 and kolonK[j]>0):
                min =matris[i][j]
                plce[0], plce[1]=i, j
    plce.append(min)
    return plce

def Assignment(p):
    if (kolonK[p[1]]<=satirK[p[0]]):
        atanan = kolonK[p[1]]
    else:
        atanan = satirK[p[0]]
    satirK[p[0]] -=atanan
    kolonK[p[1]] -=atanan
    atamaMatrisi[p[0]][p[1]]=atanan

def Write():
    k=0
    for i in atamaMatrisi:
        print(i , " - ", copyofSatirK[k])
        k+=1
    print (copyofkolonK)

m=int(input("Satir Sayısı (Talep veya Arz):"))
n=int(input("Sütun Sayısı (Arz veya Talep):"))

atamaMatrisi=[]
matris=[]
for i in range(m):
    satir=[]
    for j in range(n):
        satir.append(int(input(str(i+1)+". Satır "+str(j+1)+". sütun maliyeti")))
    matris.append(satir)

satirK, kolonK,copyofSatirK,copyofkolonK=[],[],[],[]

TS,TK=0,0
for i in range(m):
    e=int(input(str(i+1)+". Satır kapasitesi "))
    TS +=e
    satirK.append(e)

for i in range(n):
    e=int(input(str(i+1)+". Sütun kapasitesi "))
    TK +=e
    kolonK.append(e)

if (TS>TK):
    kolonK.append(TS-TK)
    SutunEkle(matris)
elif (TK>TS):
    satirK.append(TK-TS)
    SatirEkle(matris)

for i in kolonK:
    copyofkolonK.append(i)
for i in satirK:
    copyofSatirK.append(i)

for i in range(len(satirK)):
    atamaMatrisi.append([0]*len(kolonK))

while True:
    plc= FindMin()
    if (plc[0]==-1):
        Write()
        break
    Assignment(plc)




def SatirSutunSil(A,i,j):
    s=[]
    for r in range(0,len(A)):
        s_aux=[]
        if r==i:
            continue
        for c in range(0,len(A[0])):
            if (c==j):
                continue
            else:
                s_aux.append(A[r][c])
        s.append(s_aux)
    return s

print("*** Satir Sütün Silme Programı Yüklendi *******")

#3A=[[1,3,2,4],
#   [3,2,4,5],
#   [5,7,3,8],
#   [2,5,3,2]]

#P=SatirSutunSil(A,1,2)

#for i in P:
#    print(i)
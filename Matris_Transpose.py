
def Transpose(A):
    res=[]
    for i in range(len(A[0])):
        satir=[]
        for j in range(len(A)):
            satir.append(A[j][i])
        res.append(satir)
    return res


#A=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

#print(Transpose(A))
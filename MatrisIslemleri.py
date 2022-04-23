def MatrisToplaCikar(M,N,R):
    T=[]
    for i in range(0,len(M)):
        satir=[]
        for j in range(0, len(N[0])):
            satir.append((M[i][j] + R*N[i][j]))
        T.append(satir)
    return T

#A=[[1,2,4], [3,2,6],[4,5,6],[5,8,7]]
#B=[[2,3,5], [1,0,9],[1,51,5],[3,-2,7]]


#print(MatrisToplaCikar(A,B,1))
#print(MatrisToplaCikar(A,B,-1))

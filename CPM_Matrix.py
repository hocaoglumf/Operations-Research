M=[[-1,3,-1,-1,-1,-1],
   [-1,-1,3,2,-1,-1],
   [-1,-1,-1,0,3,2],
   [-1,-1,-1,-1,7,5],
   [-1,-1,-1,-1,-1,6]]


nodes=["A","B","C","D","E","F","G","H","I",	"J","K","L","M","N","O"]

M=[
[-1,	2,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1],
[-1,	-1,	4,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1],
[-1,	-1,	-1,	7,	3,	-1,	-1,	-1,	6,	-1,	-1,	-1,	-1,	-1,	-1],
[-1,	-1,	-1,	-1,	-1,	-1,	6,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1],
[-1,	-1,	-1,	-1,	-1,	6,	-1,	5,	-1,	-1,	-1,	-1,	-1,	-1,	-1],
[-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	8,	-1,	-1,	-1,	-1,	-1],
[-1,	-1,	-1,	-1,	-1,	-1,	-1,	1,	-1,	-1,	-1,	-1,	-1,	-1,	-1],
[-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	2,	-1,	-1],
[-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	4,	-1,	-1,	-1,	-1,	-1],
[-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	2,	10,	-1,	-1,	-1],
[-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	4,	-1],
[-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	2,	-1],
[-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	5],
[-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	7],
[-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1]
]
def GoForward(M):
    row=[0]

    for i in range(1,len(M[0])):
        tpl_aux=[]
        for j in range(i):
            if (M[j][i]==-1):
                t=-9999999999
            else:
                t=M[j][i]
            tpl_aux.append(t + row[j])

        row.append(max(tpl_aux))

    column=[row[len(row)-1]]
    return row,row[len(row)-1]

def GoBackward(M,longest):
    column=[0 for i in range(len(nodes)-1)]
    column.append(longest)
    for i in range(len(M)-2, 0,-1):
        temp=[]
        for j in range(len(M[0])-1,i,-1):
            if (M[i][j]>=0):
                temp.append(column[j]-M[i][j])

        column[i]=min(temp)
    return column


row, enb=GoForward(M)
col=GoBackward(M,enb)

#critical Path
crt=""
for i in range(len(row)-1):
    if ((row[i]-col[i])==0):
        crt +=nodes[i]

crt +=nodes[len(nodes)-1]

print(crt)

print(row)
print(col)



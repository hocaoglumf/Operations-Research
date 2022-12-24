#rho=2/3
#p0=1-rho

xlambda=float(input("\u03BB "))
xmu =float(input("\u03BC "))
n=int(input("n "))
rho = xlambda/xmu

pn=[]
for i in range(n+1):
    pn.append([i,(1-rho)*rho**i])

cum=0
print ("n     pn  ","   Kümülatif Pn")
print ("----------------------------")
for i in pn:
    cum +=i[1]
    print (i[0], "  ", round(i[1],5), "  ", round(cum,5))
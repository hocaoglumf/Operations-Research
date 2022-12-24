import math
import Factorial


def PureDeathPn(mu, t, N, n):
    pn= ((mu*t)**(N-n)*math.e**(-mu*t))/Factorial.Factorial(N-n)
    return pn
tpl=0
n=5
mu=3
N=18
p0=0
tt=7
def CalculateP0(N,t):
    p0=0
    for n in range(1,N+1):
        p0 +=((mu*t)**(N-n)*math.e**(-mu*t))/Factorial.Factorial(N-n)
    p0=1-p0
    return p0

pns=[]
for t in range(1,tt+1):
    pn =0
    for i in range(1,n+1):
        pn +=PureDeathPn(mu, t,N, i)
    pns.append([t, CalculateP0(N,t)+ pn])

print("\u03BC :",mu,", N :", N)
print("t     pn   ")
for i in pns:
    print (i[0], "   ", i[1])


# Atılacak gül sayısı


atilacak=0
t=7

for i in range(N+1):
    atilacak +=i*PureDeathPn(mu,t, N, i)

print("Hafta sonu atılacak gül sayısı: ",round(atilacak,3))

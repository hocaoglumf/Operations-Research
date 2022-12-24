import Factorial

p0=0
c=4
lmbd=16
mu= 5
n=1
rho=lmbd/mu
print("\u03C1=\u03BB/\u03BC :",lmbd/mu, "\u03C1/c :",rho/c, "< 1",rho/c<1)
print ("\u03BB :", lmbd, "\u03BC :",mu, "c :",c )
for i in range(c):
    p0 += rho**i/Factorial.Factorial(i)

p0 +=(rho**c/Factorial.Factorial(c))*(1/(1-rho/c))
p0=p0**-1

print("p0 ",round(p0,5))
if (n>=c):
    pn=rho**n/(Factorial.Factorial(c)*c**(n-c))*p0
else:
    pn=(rho**n/Factorial.Factorial(n))*p0
print("pn  ", round(pn,4), "for n=",n)
Lq=(rho**(c+1)/(Factorial.Factorial(c-1)*(c-rho)**2))*p0
Ls=Lq + rho
print("Lq : ",round(Lq,4), "Ls :", round(Ls,4))
print("Wq :", round(Lq/lmbd,4), "Ws :", round(Ls/lmbd,4))

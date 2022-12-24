def Factorial(x):
    if x==0:
        return 1
    return x*Factorial(x-1)


def CalculateP0(c, lmbd, mu):
    global p0
    rho=lmbd/mu
    for i in range(c):
            p0 += rho**i/Factorial(i)
    if (rho / c == 1):
        p0 += (rho ** c / Factorial(c)) * (N - c + 1)
    else:
        p0 += rho ** c * (1 - (rho / c) ** (N - c + 1)) / (Factorial(c) * (1 - rho / c))

    p0 = p0 ** -1

    return p0

def CalculatePn(n, c, lmbd, mu):
    rho =lmbd/mu
    if (n < c):
        pn = rho ** n / Factorial(n)
    elif (n >= c and n <= N):
        pn = rho ** n / (Factorial(c) * c ** (n - c))

    pn = pn * p0
    return pn


p0=0
lmbd=16
mu=5
c=4
n=4
N=19
rho=lmbd/mu

CalculateP0(c, lmbd, mu)

print("p0 :", round(p0,5))
A=(rho/c)**(N-c+1)
B=1-rho/c
C=(rho/c)**(N-c)
D=rho**(c+1)/((Factorial(c-1)*(c-rho)**2))
Lq=D*(1-A-(N-c+1)*B*C)*p0

print("Lq :", round(Lq,4))
cumPn=0
print("n ", " pn ", "Kümülatif pn   ", "\u03BB Efektif")
print("---------------------------------------------------------------")
for n in range(N+1):
    pn= CalculatePn(n,c, lmbd, mu)
    cumPn +=pn
    lambdaEff= lmbd-lmbd*pn


    print(n, round(pn,4), round(cumPn,4),"       ", round(lambdaEff,4))


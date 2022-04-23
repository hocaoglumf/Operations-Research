import math

def FuncP(Param):
    return Param[0]*(5*math.pi-Param[0]**2)

def MyFunc(Param):
    return Param[0]*(5*math.pi - Param[0])

def Parabol(Param):
    return -2*Param[0]**2+ 4*Param[0] + 2

def FuncNewtonExp(Param):
    return (3*Param[0] -2)**2 * (2*Param[0]-3)**2-2*Param[0]

def FuncNewtonExpDeriv(Param):
    x=Param[0]
    return 72*x**3 -234*x**2 + 241*x -80

def FuncNewtonExpSecondDeriv(Param):
    x=Param[0]
    return 3*72*x**2 -2*234*x + 241

def Karekok2(Param):
    return Param[0]**2 -2

def Karekok2Deriv(Param):
    return 2*Param[0]

def Gradient1(Param):
    x1=Param[0]
    x2=Param[1]
    x3=Param[2]
    return [[3, x3*math.sin(x2*x3), x2*math.sin(x2*x3)],
            [8*x1, -1250*x2, 2],
            [-x2*math.e**(-x1*x2), -x1*math.e**(-x1*x2),20]]

def MultiVarFonksiyon(Param):
    x1=Param[0]
    x2=Param[1]
    x3=Param[2]
    return [[3*x1 -math.cos(x2*x3)-3/2],
            [4*x1**2-625*x2**2 + 2*x3-1],
            [20*x3 + math.e**(-x1*x2) +9]]

def BolzenoExp(Param):
    x=Param[0]
    return 20*x-3*x**2 -x**4

def BolzenoExpDeriv(Param):
    x=Param[0]
    return 20-6*x -4*x**3

def BolzenoDerivX1(Param):
    x1=Param[0]
    x2=Param[1]
    x3=Param[2]
    return 1-2*x1, 0

def BolzenoDerivX2(Param):
    x1=Param[0]
    x2=Param[1]
    x3=Param[2]
    return x3-2*x2, 1

def BolzenoDerivX3(Param):
    x1=Param[0]
    x2=Param[1]
    x3=Param[2]
    return 2+x2-2*x3, 2

def BolzenoVizeDerivX1(Param):
    x1 = Param[0]
    x2 = Param[1]
    return 1 +x2 -2*x1, 0

def BolzenoVizeDerivX2(Param):
    x1 = Param[0]
    x2 = Param[1]
    return x1 -2*x2, 1


def GoldenExp(Param):
    x=Param[0]
    return 2*math.sin(x)-x**2/10
def GutterFunction(Param):
    l=Param[0]
    theta=Param[1]
    #return (6-2*l+l*math.cos(theta))*l*math.sin(theta)
    return l*math.sin(theta)*(6-2*l + l*math.cos(theta))

def OdevFonk(Param):
    x=Param[0]
    return 2*x -1.75*x**2 + 1.1*x**3-0.25*x**4

def OrnekFuncx2(Param):
    x=Param[0]
    return -x**2;

def bukin_function(x):
    return 100*math.sqrt(abs(x[1]-0.01*x[0]**2)) + 0.01*abs(x[0] + 10)

def OrnekProblemler_1(Param):
    return -4*Param[0]**3 +2;

def VizeFun(Param):
    x=Param[0]
    return x**4 + 6*x**2 + 12*x

def VizeFunDeriv(Param):
    x=Param[0]
    return 4*x**3 + 12*x + 12

def VizeFunSecondDeriv(Param):
    x=Param[0]
    return 12*x**2 + 12

def FluidDynamics(Param):
    m_dot_in=Param[0]
    P_in = 120663.00000000001 #Param[1]
    rho = 1025.0000000000000#Param[2]
    A_boru = 0.19642857142857142 #Param[3]
    g = 9.81 #Param[4] #
    D_boru = 0.5 # Param[5] #
    L_boru = 1 # Param[6] #
    V_out = 15.081929587972137 # Param[7] #
    mu = 10 ** -3 #Param[8] #
    epsi_mm = 0.26 #Param[9] #
    epsi = epsi_mm / 1000
    deltaT = 0.00001  #Param[10] #

#    [x,120663.0, 1025.0, 0.19642857142857142, 9.81, 0.5,1,15.081929587972137,0.26, 0.00001]

#    m_dot_in = m_dot_in - deltaT;
    V = (m_dot_in / (rho * A_boru))
    Re = (rho * V * D_boru / mu)
    f = ((1 / ((-1.8) * (math.log10((6.9 / Re) + (((epsi / D_boru) / 3.7)**1.11)))))**2)
    h_BS_boru = ((f * L_boru) / D_boru * (V**2) / (2 * g))
    P_loss = (h_BS_boru * rho * g)
    P_out=(P_in -  P_loss )
    func= P_in - P_out
    return -1*func

def FluidDynamicsDeriv(Param):
    x=Param[0]
    P_in = 120663.00000000001
    rho = 1025.0000000000000
    A_boru = 0.19642857142857142
    g = 9.81
    D_boru = 0.5
    L_boru = 1
    V_out = 15.081929587972137
    mu = 10 ** -3
    epsi_mm = 0.26
    epsi = epsi_mm / 1000
    deltaT = 0.00001
    v_in = ((2 * P_in / rho) ** 0.5)

    m_dot_in = rho * v_in * A_boru

    V = (m_dot_in / (rho * A_boru))
    # m_dot_out = A_boru * length / pieceNumber * rho
    P = P_in
    x = m_dot_in
    A = A_boru
    D = D_boru
    L = L_boru
    e = epsi
    delta = deltaT

    m_dot_in = x
    V = (m_dot_in / (rho * A_boru))
    Re = (rho * V * D_boru / mu)
    f = ((1 / ((-1.8) * (math.log10((6.9 / Re) + (((epsi / D_boru) / 3.7) ** 1.11))))) ** 2)
    h_BS_boru = ((f * L_boru) / D_boru * (V ** 2) / (2 * g))
    P_loss = (h_BS_boru * rho * g)
    P_out = (P_in - P_loss)
    fonk = P_in - P_out - P_loss - 10 * deltaT
    turevV = -2.12962962962963 * L * mu / (A * D ** 2 * rho * (6.9 * A * mu / (D * x) + 0.234043231705236 * (e / D) ** 1.11) * math.log10(6.9 * A * mu / (D * x) + 0.234043231705236 * (e / D) ** 1.11) ** 3) - 0.308641975308642 * L * x / (A ** 2 * D * rho * math.log10(6.9 * A * mu / (D * x) + 0.234043231705236 * (e / D) ** 1.11) ** 2)
    return turevV

def Valve(Param):
    K=4.1
    P_in=498100
    rho = 1000
    v_valf=Param[0]
    a= (2 * (P_in - K * ((v_valf ** 2) / 2) * rho)/ rho) ** 0.5
    xx=v_valf-a
    return ((2*(P_in-(K*((v_valf**2)/2)*rho))/rho)**0.5)-v_valf

def ValveDeriv(Param):
    K=4.1
    P_in=498100
    rho = 1000
    v_valf=Param[0]
    v_in = (2 * P_in / rho) ** 0.5
    return -4.1*v_valf*(4981/5 - 4.1*v_valf**2)**(-0.5) - 1

def BruteForceTest(Param):
    x=Param[0]
    return -2*x**2 +3*x-3


def BruteForceTest2(Param):
    x=Param[0]
    return -2*x**2


def BruteForceTest3(Param):
    x = Param[0]
    return 2 * x ** 2

def Dichotomous(Param):
    x=Param[0]
    return 24*x-4*x**2

def MultivarDict(Param):
    x1=Param[0]
    x2=Param[1]
    x3=Param[2]
    return x1 + 2*x3 + x2*x3 -x1**2-x2**2 -x3**2


def SimulatedAnnealingExmp(Param):
    x11 = Param[0]
    x12 = Param[1]
    x13 = Param[2]
    x14 = Param[3]
    x15 = Param[4]
    x21 = Param[5]
    x22 = Param[6]
    x23 = Param[7]
    x24 = Param[8]
    x25 = Param[9]
    x31 = Param[10]
    x32 = Param[11]
    x33 = Param[12]
    x34 = Param[13]
    x35 = Param[14]

    L1 = 5
    L2 = 6
    L3 = 7

    A1 = (0.5 * x11 + 0.5 * x21 + 0.3 * x31)
    A2 = (0.7 * x12 + 0.6 * x22 + 0.4 * x32)
    A3 = (0.3 * x13 + 0.3 * x23 + 0.4 * x33)
    A4 = (0.3 * x14 + 0.2 * x24 + 0.2 * x34)
    A5 = (0.1 * x15 + 0.1 * x25 + 0.1 * x35)

    x11 + x21 + x31 >= 0
    x12 + x22 + x32 >= 0
    x13 + x23 + x33 >= 0
    x14 + x24 + x34 >= 0
    x15 + x25 + x35 >= 0

    x11 + x12 + x13 + x14 + x15 == 1
    x21 + x22 + x23 + x24 + x25 == 1
    x31 + x32 + x33 + x34 + x35 == 1

    # return (10*A1 + 12*A2 + 13*A3 + 12*A4 + 15*A5 -
    # (L1* ( x11 + x12 + x13 + x14 + x15 -1)) -
    # (L2 * ( x21 + x22 + x23 + x24 + x25 -1)) -
    # (L3 * (x31 + x32 + x33 + x34 + x35 - 1)))

    # return 10*A1 + 12*A2 + 13*A3 + 12*A4 + 15*A5

    return 10 * A1 + 12 * A2 + 13 * A3 + 12 * A4 + 15 * A5

def Soru(Param):
    x=Param[0]
    return x**2 -4*x +3
print("Loaded.....")
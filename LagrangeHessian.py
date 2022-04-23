import sympy as sym


def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
        # return string
    return str1


def CreateLAgranfeFunction(goal, constraints):
    lagrangeF = goal
    for i in range(len(constraints)):
        lagrangeF += "-L" + (str(i + 1)) + "*(" + constraints[i] + ")"
        variables.insert(i, "L" + str(i + 1))
    print(lagrangeF.replace("L", "\u03BB"))
    return lagrangeF


def VariableDeclarations(Variables):
    v={}
    for i in range(len(variables)):
        v[variables[i]]="sym.Symbol(" + '''"'''+variables[i] + '''") '''
        eval(v[variables[i]])
    return v
'''     
    vardec = ""
    for i in range(len(variables)):
        vardec += variables[i] + ","
    
    list1 = []
    list1[:0] = vardec
    list1[len(vardec) - 1] = "=sym.symbols("
    vardec = listToString(list1)
    for i in range(len(variables)):
        vardec='''"'''+variables[i] + '''" '''
    vardec+=")"
    return vardec
'''


var=int(input("Değişken Sayısı : "))
variables=[]
for i in range(var):
    v=input("Değişken "+str(i+1)+" ")
    variables.append(v)

const=int(input("Kısıt Sayısı : "))

goal=input("Amaç Fonksiyonu : ")

constraints=[]
for i in range(const):
    cst=input("Kısıt "+str(i+1)+" : ")
    constraints.append(cst)

LF=CreateLAgranfeFunction(goal,constraints)

vars=VariableDeclarations(variables)

#Turev 1
firstDerivatives={}
for i in vars.keys():
    firstDerivatives[i]=sym.diff(LF, eval(vars[i]))
    print(i, "  ", firstDerivatives[i].doit())

#turev 2
secondDerivatives=[]
for i in firstDerivatives.keys():
    s=[]
    for j in vars.keys():
        s.append(sym.diff(firstDerivatives[i], eval(vars[j])))
    secondDerivatives.append(s)
j=-1
for i in secondDerivatives:
    j+=1
    varname=variables[j].replace("L", "\u03BB")
    print(varname, i)


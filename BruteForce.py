import Functions

def Sign(a):
    if (a<0):
        return -1
    elif (a>0):
        return 1
    else:
        return 0


def BruteForce(Deriv, interval,epsilon):
    a=interval[0]
    b=interval[1]
    iter=1
    oldrea=Deriv([a])
    oldreb=Deriv([b])
    while (True):
        rea=Deriv([a])
        reb=Deriv([b])
        if (rea<0):
            asign = -1
        else:
            asign=1
        if (reb<0):
            bsign=-1
        else:
            bsign =1

        if (Sign(rea)!=Sign(oldrea) ):
            print(iter, " ", round(oldrea,5), "  ", "[", round(a,5), ",", round(b,5), "] üst limitden ilerlenerek bulundu")
            print("*Çözüm ", a-epsilon, " iterasyon :", iter)
            break

        if (Sign(reb)!=Sign(oldreb) ):
            print(iter, " ", round(oldreb,5), "  ", "[", round(a,5), ",", round(b,5), "] üst limitden ilerlenerek bulundu")
            print("*Çözüm ", b+epsilon, " iterasyon :", iter)
            break

        print(iter, " f(a):", round(rea,5), "  f(b): ",round(reb,5), " [", round(a,5), ",", round(b,5), "] ")

        if (abs(b-a) <epsilon):
            print ("Çözüm bu aralıkta değil ")
            break
        a+=epsilon
        b-=epsilon
        iter +=1
        oldrea = rea
        oldreb = reb

BruteForce(Functions.BolzenoExp,[2,4], 0.00001)




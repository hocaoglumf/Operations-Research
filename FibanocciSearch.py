# Doç. Dr. M. Fatih Hocaoğlu
# İstanbul Medeniyet Üniversitesi
#
import math
import matplotlib.pyplot as plt
import Functions

class Fibonacci:
    def __init__(self, function, interval,epsilon):
        self.interval=interval
        self.function=function
        self.epsilon=epsilon
        self.fib=[0,1]
    def GetFibonacci(self,n):
        if n < 0:
            print("Yanlış Giriş")
            return -1
        elif (len(self.fib)>n):
            return self.fib[n]
        else:
            self.fib.append(self.GetFibonacci(n - 1) + self.GetFibonacci(n - 2))
            return self.fib[n]
    def FindFibonacci(self,n):
        index=0
        b=False
        for i in self.fib:
            if (i==n):
                b=True
                return index
            else:
                index+=1
        if (b ==False and self.fib[len(self.fib)-1]<n):
            self.GetFibonacci(len(self.fib)+10)
            return self.FindFibonacci(n)
        else:
            return -1

    def FindClosestFibonacciIndex(self,n):
        if (self.FindFibonacci(n)==-1):
            index=1
            for i in range(len(self.fib)-1):
                if (self.fib[i]<n and self.fib[i+1]>n):
                    return index #self.fib[i+1]
                else:
                    index+=1
        else:
            return self.FindFibonacciIndex(n)

    def FindClosestFibonacci(self,n):
        if (self.FindFibonacci(n)==-1):
            for i in range(len(self.fib)-1):
                if (self.fib[i]>n ):
                    return self.fib[i]
        else:
            return self.FindFibonacci(n)

    def Solve(self):
        b=self.interval[1]
        a=self. interval[0]
        cfb=self.FindClosestFibonacci(b - a)
        epsilon = (b - a) / cfb
        print("Fibonacci indeksi/", "Fibonacci Sayısı/", "Aralık/", "Fonksiyon Değerleri/","Fark (f1-f2)/", "Orta Nokta")
        for i in range(self.FindClosestFibonacciIndex(b - a), -1, -1):
            ff = self.GetFibonacci(i) * epsilon
            x1 = a + ff
            x2 = b - ff
            if (x1>=x2):
                x2,x1=x1,x2

            f1 = self.function([x1])
            f2 = self.function([x2])

            if (f1 <= f2):
                a = x1
            else:
                b = x2

            print(i, "  ",round(self.GetFibonacci(i),5), " [", round(a,5), ", ", round(b,3), "]    (", round(f1,3), " , ", round(f2,3), " ) ",round((f1-f2),3)," ", round((x2+x1)/2,3))
            if (i==0):
                opt=self.function([(a+b)/2])
                print("Optimum değer : x ",round((a+b)/2,5), " Fonksiyon değeri :", round(opt,5)  )
                return opt



#f=Fibonacci(Functions.MyFunc, [0,20], 1)
#f.Solve()

#p=Fibonacci(Functions.Parabol, [0,30],0.01)
#p.Solve()


#p=Fibonacci(Functions.FuncP, [0,30],0.001)
#p.Solve()

#print("Odev")
#p=Fibonacci(Functions.OdevFonk, [0,4],0.01)
#p.Solve()


p=Fibonacci(Functions.OrnekFuncx2, [-5,15],0.01)
p.Solve()

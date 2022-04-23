import random
def Function(x):
    return x**2 -4*x +3

interval=[0,5]
minimum =99999999999999

for i in range(100):
    x=random.randint(0,50)/10
    fnv = Function(x)
    if (fnv<minimum):
        minimum = fnv
        xfound =x

print("x : ", xfound)
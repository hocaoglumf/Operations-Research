import matplotlib.pyplot as plt
import math
x_Axis = []
y_Axis=[]
max=-50000
for x in range(-100,100):
    x_Axis.append(x)
    y_Axis.append(-x**2+2*x+300)
    if (max < -x**2+2*x+300):
        max =-x**2+2*x+300

plt.plot(x_Axis,y_Axis)

p=23
for x in range(-100,100,p):
    x2=x+p
    print(x,"   ",-x**2+2*x+300, "   ", x2, "   ", -x2**2+2*x2+300 )
    x1, y1 = [x, x2], [-x**2+2*x+300, -x2**2+2*x2+300]
    plt.plot(x1, y1, marker = '.')

print("max ", max)



plt.show()

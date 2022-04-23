import matplotlib.pyplot as plt
import math
x_Axis = []
y_Axis=[]
y_Axis2=[]
x=-10

while x<=10:
    x_Axis.append(x)
    y_Axis.append(10-x**2)
    y_Axis2.append(math.sin(x))
    x +=0.01
l=0.1
xs0=-10
xs1=10



plt.plot(x_Axis,y_Axis)
plt.plot(x_Axis,y_Axis2)

plt.show()

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')
#10x1 + 4x2 -2x1^2 -x2^2


fig = plt.figure()
ax = fig.gca(projection='3d')

xL1,xL2,yL,yDL=[],[],[],[]
for x1 in range(0,10):
    for x2 in range(0,10):
        y=10*x1 + 4*x2 -2*x1**2 -x2**2
        xL1.append(x1)
        xL2.append(x2)
        yL.append(y)
        yD=2*x1+x2
        yDL.append(yD)
xL1, xL2 = np.meshgrid(xL1, xL2)
surf=ax.plot_surface (xL1, xL2, yL, label='parametric curve')
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#ax.plot(xL1, xL2, yDL, label='parametric curve')
#ax.legend()

plt.show()

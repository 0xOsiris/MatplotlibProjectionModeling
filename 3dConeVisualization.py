from mpl_toolkits import mplot3d
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection = '3d')

# Make a mesh in the space of parameterisation variables u and v
u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
v = np.linspace(0, 1, endpoint=True, num=50)
u, v = np.meshgrid(u, v)


X=(1-v)*(0)+ v*(1+(.05*np.cos(u)))
Y=(1-v)*(0)+ v*(1+(.05*np.sin(u)))
Z=(1-v)*(1)+v*(-1)


# draw sphere
n, p = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
Xp = np.cos(n)*np.sin(p)
Yp = np.sin(n)*np.sin(p)
Zp = np.cos(p)
ax.plot_surface(Xp, Yp, Zp, cmap=cm.coolwarm)


ax.set_xlim3d(-1.5, 1.5)
ax.set_ylim3d(-1.5, 1.5)
ax.set_zlim3d(-1.5, 1.5)
ax.plot_surface(X, Y, Z, color ='b', rstride = 1, cstride = 1)

plt.show()

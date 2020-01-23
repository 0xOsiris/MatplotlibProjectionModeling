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

r=.5
Xnot=.5
Ynot=.5

X=(1-v)*(0)+ v*(Xnot+(r*np.cos(u)))
Y=(1-v)*(0)+ v*(Ynot+(r*np.sin(u)))
Z=(1-v)*(1)+v*(-1)

Xt=(4*Xnot+4*r*np.cos(u))/(2*r**2+2*Xnot*r*np.cos(u)+2*Ynot*r*np.sin(u)+1)
Yt=(4*Ynot+4*r*np.sin(u))/(2*r**2+2*Xnot*r*np.cos(u)+2*Ynot*r*np.sin(u)+1)
Zt=1-(8/((2*r**2+2*Xnot*r*np.cos(u)+2*Ynot*r*np.sin(u)+1)))


# draw sphere
n, p = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
Xp = np.cos(n)*np.sin(p)
Yp = np.sin(n)*np.sin(p)
Zp = np.cos(p)
ax.plot_surface(Xp, Yp, Zp, cmap=cm.coolwarm)

ax.plot_surface(Xt,Yt,Zt,cmap=cm.gray)

ax.set_xlim3d(-1.5, 1.5)
ax.set_ylim3d(-1.5, 1.5)
ax.set_zlim3d(-1.5, 1.5)
ax.plot_surface(X, Y, Z, color ='b', rstride = 1, cstride = 1)

plt.show()

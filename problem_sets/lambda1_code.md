```{code-cell} python3
---
mystnb:
  image:
    width: 80%
    align: center
tags:
  - hide-input
---

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

f = lambda x: (x[0])**3 - (x[1])**3
lb,ub = -1.5,1.5

x = y = np.linspace(lb,ub, 100)
X, Y = np.meshgrid(x, y)
zs = np.array([f((x,y)) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

a,b=1,1
# (x/a)^2 + (y/b)^2 = 1
theta = np.linspace(0, 2 * np.pi, 100)
X1 = a*np.cos(theta)
Y1 = b*np.sin(theta)
zs = np.array([f((x,y)) for x,y in zip(np.ravel(X1), np.ravel(Y1))])
Z1 = zs.reshape(X1.shape)

fig = plt.figure(dpi=160)
ax2 = fig.add_subplot(111)
ax2.set_aspect('equal', 'box')
ax2.contour(X, Y, Z, 50,
            cmap=cm.jet)
ax2.plot(X1, Y1)
plt.setp(ax2, xticks=[],yticks=[])

fig = plt.figure(dpi=160)
ax3 = fig.add_subplot(111, projection='3d')
ax3.plot_wireframe(X, Y, Z,
            rstride=2,
            cstride=2,
            alpha=0.7,
            linewidth=0.25)
f0 = f(np.zeros((2)))+0.1
ax3.plot(X1, Y1, Z1, c='red')
plt.setp(ax3,xticks=[],yticks=[],zticks=[])
ax3.view_init(elev=18, azim=154)

plt.show()

```
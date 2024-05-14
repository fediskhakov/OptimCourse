---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 🔬 Tutorial problems *lambda*

```{code-cell} python3
---
mystnb:
  image:
    width: 80%
    align: center
tags:
  - hide-cell
---

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from myst_nb import glue

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
glue("pic1", fig, display=False)

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
glue("pic2", fig, display=False)


f = lambda x: x[0]**3/3 - 3*x[1]**2 + 5*x[0] - 6*x[0]*x[1]
x = y = np.linspace(-10.0, 10.0, 100)
X, Y = np.meshgrid(x, y)
zs = np.array([f((x,y)) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)
a,b=4,8
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
glue("pic3", fig, display=False)

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
glue("pic4", fig, display=False)

```

## $\lambda$.1

::::::{tab-set}
:::::{tab-item} Formulation
:::{include} problem_sets/lambda1_formulation.md
:::::
:::::{tab-item} Hint
:::{include} problem_sets/lambda1_hint.md
:::

:::{glue:figure} pic1
:width: 50%
:align: center

Level curves of the criterion function and constraint curve.
:::
:::{glue:figure} pic2
:width: 50%
:align: center

3D plot of the criterion surface with the constraint curve projected to it.
:::

:::::
:::::{tab-item} Solution
:::{include} problem_sets/lambda1_solution.md
:::::
::::::


## $\lambda$.2

::::::{tab-set}
:::::{tab-item} Formulation
:::{include} problem_sets/lambda2_formulation.md
:::::
:::::{tab-item} Hint
:::{include} problem_sets/lambda2_hint.md
:::

:::{glue:figure} pic3
:width: 50%
:align: center

Level curves of the criterion function and constraint curve.
:::
:::{glue:figure} pic4
:width: 50%
:align: center

3D plot of the criterion surface with the constraint curve projected to it.
:::

:::::
:::::{tab-item} Solution
:::{include} problem_sets/lambda2_solution.md
:::::
::::::


## $\lambda$.3

::::::{tab-set}
:::::{tab-item} Formulation
:::{include} problem_sets/lambda3_formulation.md
:::::
:::::{tab-item} Hint
:::{include} problem_sets/lambda3_hint.md
:::
:::::
:::::{tab-item} Solution
:::{include} problem_sets/lambda3_solution.md
:::::
::::::


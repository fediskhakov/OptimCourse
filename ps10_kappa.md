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

# 🔬 Tutorial problems *kappa*

```{code-cell} python3
---
mystnb:
  image:
    width: 40%
    align: center
tags:
  - hide-cell
---

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from myst_nb import glue


f = lambda x: x[0]**3/3 - 3*x[1]**2 + 2*x[0]
gx = lambda y: y**3/4
gy = lambda x: (4*x)**(1/3)

x = y = np.linspace(-5.0, 5.0, 100)
X, Y = np.meshgrid(x, y)
zs = np.array([f((x,y)) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ymax = gy(5.0)
y = np.linspace(-ymax, ymax, 100)
X1,Y1 = gx(y),y
zs = np.array([f((x,y)) for x,y in zip(np.ravel(X1), np.ravel(Y1))])
Z1 = zs.reshape(X1.shape)

fig = plt.figure(dpi=160)
ax1 = fig.add_subplot(111)
ax1.set_aspect('equal', 'box')
ax1.contour(X, Y, Z, 50,
            cmap=cm.jet)
ax1.plot(X1, Y1)
plt.setp(ax1, xticks=[],yticks=[])
glue("pic1", fig, display=False)

fig = plt.figure(dpi=160)
ax2 = fig.add_subplot(111, projection='3d')
ax2.plot_wireframe(X, Y, Z,
            rstride=2,
            cstride=2,
            alpha=0.7,
            linewidth=0.25)
f0 = f(np.zeros((2)))+0.1
ax2.plot(X1, Y1, Z1, c='red')
plt.setp(ax2,xticks=[],yticks=[],zticks=[])
ax2.view_init(elev=18, azim=-160)
glue("pic2", fig, display=False)

```

## $\kappa$.1

::::::{tab-set}
:::::{tab-item} Formulation
:::{include} problem_sets/kappa1_formulation.md
:::::
:::::{tab-item} Hint
:::{include} problem_sets/kappa1_hint.md
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
:::{include} problem_sets/kappa1_solution.md
:::::
::::::

## $\kappa$.2

::::::{tab-set}
:::::{tab-item} Formulation
:::{include} problem_sets/kappa2_formulation.md
:::::
:::::{tab-item} Hint
:::{include} problem_sets/kappa2_hint.md
:::::
:::::{tab-item} Solution
:::{include} problem_sets/kappa2_solution.md
:::::
::::::

## $\kappa$.3

::::::{tab-set}
:::::{tab-item} Formulation
:::{include} problem_sets/kappa3_formulation.md
:::::
:::::{tab-item} Hint
:::{include} problem_sets/kappa3_hint.md
:::::
:::::{tab-item} Solution
:::{include} problem_sets/kappa3_solution.md
:::::
::::::

## $\kappa$.4

::::::{tab-set}
:::::{tab-item} Formulation
:::{include} problem_sets/kappa4_formulation.md
:::::
:::::{tab-item} Hint
:::{include} problem_sets/kappa4_hint.md
:::::
:::::{tab-item} Solution
:::{include} problem_sets/kappa4_solution.md
:::::
::::::

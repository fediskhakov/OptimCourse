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

# Problems bank

***Question A.2***

Let $f \colon \mathbb{R} \to \mathbb{R}$ be defined by $f(x) = \sin(x)$.
- Write down the set of stationary points of this function.
- Which of these, if any, are maximizers, and which are minimizers?

```{tip}
When we discussed these kinds of problems it was for functions of the form $f \colon [a, b] \to \mathbb{R}$.  Now the domain is all of $\mathbb{R}$.
However you can apply the same definitions and use similar reasoning.  Also, feel free to look up and use any helpful facts on trigonometric functions.
```


***Question A.4***

1. Find all stationary points of the function 
$f(x, y) = \frac{\cos(x^2 + y^2)}{1 + x^2 + y^2}$.

2. Find all maximizers and minimizers of this function on $\mathbb{R}^2$.

```{hint}
Is there a convenient change of variable to convert the problem to a univariate one.
```

```{code-cell} python
:tags: [hide-cell]

from myst_nb import glue
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
import scipy as sp
from matplotlib import cm
f = lambda x, y: np.cos(x**2 + y**2) / (1 + x**2 + y**2)
xgrid = np.linspace(-3, 3, 50)
ygrid = xgrid
x, y = np.meshgrid(xgrid, ygrid)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,
                y,
                f(x, y),
                rstride=2, cstride=2,
                cmap=cm.jet,
                alpha=0.7,
                linewidth=0.25)
ax.set_zlim(-0.5, 1.0)
glue("fig_3d", fig, display=False)

g = lambda t: np.cos(t) / (1+t)
gp = lambda t: t * np.sin(t) + np.sin(t) + np.cos(t)
xgrid = np.linspace(0, 10, 200)
fig = plt.figure(figsize=(8, 6))
plt.plot(xgrid, gp(xgrid))
plt.hlines(y=0, xmin=0, xmax=10)
glue("fig_2d", fig, display=False)

res = sp.optimize.root_scalar(gp, bracket=[2, 4], method='brentq')
glue("res_text_1", f"The smallest stationary point is tm={res.root}")
glue("res_text_2", f"The minimum is {g(res.root)}")
```

````{admonition} Solutions
:class: success


***Question A.2***

The set $S$ of stationary points of $f$ are the points $x \in \mathbb{R}$ such
that $f'(x) = \cos(x) = 0$. By the definition of the cosine function this
is the set
%
$$
S := \{ x \in \mathbb{R} : x = \pi/2 + k \pi \text{ for } k \in \mathbb{Z} \}
$$
%
Every point in the domain $\mathbb{R}$ is interior (i.e, not an end point) and
the function $f$ is differentiable, so the set of maximizers will be
contained in the set of stationary points. The same is true of the set of
minimizers. From the definition of the sine function, we have
%
$$
f(\pi/2 + k \pi) =
\begin{cases}
    1 & \text{ if $k$ is even} \\
    -1 & \text{ if $k$ is odd} \\
\end{cases}
$$
%
Hence the set of maximizers is
%
$$
M^* := \{ x \in \mathbb{R} : x = \pi/2 + k \pi \text{ for  } k \text{ an
even integer}\}
$$
%
The set of minimizers is
%
$$
M_* := \{ x \in \mathbb{R} : x = \pi/2 + k \pi \text{ for  } k \text{ an
odd integer}\}
$$
%


***Question A.4***

The graph of $f(x,y)$ is

```{glue:figure} fig_3d
:width: 80%
:align: center
```

Let $t = x^2+y^2 \geq 0$.
The function becomes 
%
$$
f(x,y) = \frac{\cos(x^2+y^2)}{1 + x^2+y^2} = \frac{\cos(t)}{1 + t} =: g(t)  \quad (t \geq 0).
$$
%

First note that since $t \geq 0$ and $\cos(t) \leq 1$, we have $g(t)\leq 1$ and $g(0)=1$.
Hence, $t=0$ is a maximizer for $g$, or $(x,y)=(0,0)$ is the maximizer for $f$.
It is a unique maximizer, since if $g(t) < 1$ for $t >0$.

Next, we find the stationary points of $f$ by finding the stationary points of $g$.
The FOC is
%
$$
g'(t) = \frac{-\sin(t)(1+t) - \cos(t)}{(1+t)^2} = 0.
$$
%
Since $(1+t)^2>0$, it must be
%
$$
-\sin(t)(1+t) - \cos(t) = 0 ⇔ t\sin(t) + \sin(t) + \cos(t)=0.
$$
%
The numerical solutions for the smallest stationary point $t_m$ such that $\cos(t_m)<0$ are


```{glue:figure} fig_2d
:width: 80%
:align: center
```

{glue:}`res_text_1`

{glue:}`res_text_2`

The minimizers are $\{(x,y)\in\mathbb{R}: x^2+y^2 = t_m\}$.
To verify that $t_m$ is the unique minimizer for $g$, since $\cos^2(t) + \sin^2(t)=1$, we rewrite FOC to get
%
$$
t\sin(t) + \sin(t) = \pm \sqrt{1-\sin^2(t)} \\
⇔ \sin^2(t) = \frac{1}{2 + 2t + t^2} \\
⇔ \cos^2(t) = 1 - \frac{1}{2+2t + t^2}=\frac{(1+t)^2}{2+2t + t^2}\\
⇒ g(t) = \frac{\cos(t)}{1+t} = \pm \frac{1}{\sqrt{2+2t +t^2}}  \qquad (\text{$t$ is stationary point}).
$$
%
Therefore, the smallest stationary point such that $\cos(t) < 0$ will be the unique minimizer for $g$.

````


## Question B.6

```{admonition} Fact: the sufficient conditions for concavity/convexity in 2D

Let $z = f(x,y)$ be a twice continuously differentiable function defined for all
$(x, y) \in R^2$.

Then it holds:

- $f \text{ is convex } \iff f''_{1,1} \ge 0, \; f''_{2,2} \ge 0 , \text{ and } f''_{1,1} f''_{2,2} − (f''_{1,2})^2 \ge 0$

- $f \text{ is concave } \iff f''_{1,1} \le 0, \; f''_{2,2} \le 0 , \text{ and } f''_{1,1} f''_{2,2} − (f''_{1,2})^2 \ge 0$

- $f''_{1,1} > 0 \text{ and } f''_{1,1} f''_{2,2} \implies f \text{ is strictly convex}$

- $f''_{1,1} < 0 \text{ and } f''_{1,1} f''_{2,2} \implies f \text{ is strictly concave}$

```

1. Find the largest domain $S$ on which 
$f(x, y) = x^2 − y^2 − xy − x^3$ is concave.
2. How about strictly concave?


````{admonition} Solutions
:class: caution

***Question B.6***

1. $f^{\prime}_{1}(x, y) = 2x - y -3x^2$

   $f^{\prime}_{2}(x, y) = -2y - x$

   $f^{\prime\prime}_{1, 1}(x, y) = 2 - 6x$

   $f^{\prime\prime}_{2, 2}(x, y) = -2$

   $f^{\prime\prime}_{1, 2}(x, y) = -1$

   %
   $$
   f(x, y) \text{ is concave } \iff
   \begin{cases}
    f^{\prime\prime}_{1, 1}(x, y) = 2 - 6x \leq 0 \\
    f^{\prime\prime}_{2, 2}(x, y) = -2 \leq 0 \\
    f^{\prime\prime}_{1, 1}(x, y) f^{\prime\prime}_{2, 2}(x, y) - f^{\prime\prime}_{1, 2}(x, y)^2 = (2 - 6x)(-2) - (-1)^2 = 12x - 5 \geq 0 \\
   \end{cases} \\
   \iff x \geq \frac{5}{12}\\
   $$
   %
   Thus, $S = \{(x, y) \in \mathbb{R^2}: x \geq \frac{5}{12}\}= [\frac{5}{12}, +\infty) \times \mathbb{R}$.

2. We just replace all the inequality in question 1 to strict inequality, and we get $S = \{(x, y) \in \mathbb{R^2}: x > \frac{5}{12}\}= (\frac{5}{12}, +\infty) \times \mathbb{R}$.


````
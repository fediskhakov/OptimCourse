---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Exercise set H

Following the invited lecture (which will not appear in the final exam) this week's tutorial focuses again on the type of problems that will likely appear in the final exam.

## Question H.1

Find the maxima and minima of the function $f(x,y) = xy$ subject to $x^2+y^2=2a^2$, where $a>0$.

```{hint}
Checking both first _and_ second order conditions if necessary for the top grade at the exam
```

## Question H.2

Find the maxima and minima of the function $f(x,y) = \tfrac{1}{x} + \tfrac{1}{y}$ subject to $(\tfrac{1}{x})^2+(\tfrac{1}{y})^2=(\tfrac{1}{a})^2$, where $a>0$.

## Question H.3

Solve the following maximization problem
%
%
$$
%
xy^{\tfrac{1}{2}}z^{\tfrac{1}{3}} \longrightarrow max_{x,y,z}
\\
\text{ subject to }\quad\quad\\
x \ge 0, y \ge 0 ,z \ge 0,\\
3x + 2y + z \le 10\\
%
$$
%
%
```{hint}
If you don't know how to compute a higher order determinant, you may skip it, but explain the decision process which involves these determinants
```




**Question H.1**

We first wite down the Lagrangian:
%
$$
%
\mathcal{L}(x, y, \lambda)
= xy - \lambda(x^2 + y^2 - 2a^2).
%
$$
%
We have:
%
$$
%
\nabla \mathcal{L}(\lambda, x, y) = \left( \begin{array}{ccc}
-(x^2 + y^2 - 2a^2), & y - 2\lambda x, & x - 2\lambda y
\end{array}
\right).
%
$$
%
F.O.C.s are $\nabla \mathcal{L}(\lambda, x, y) = 0$.

If $\lambda = 0$, then $x=y=0$, which contradicts with $x^2 + y^2 - 2a^2 = 0$ because $a>0$. Thus, $\lambda \neq 0$.

If $x=0$, then $\lambda = y = 0$, which contradicts with $\lambda \neq 0$. Thus, $x \neq 0$.

Similarly, we can prove $y \neq 0$.

Thus, we have $y = 2 \lambda x$, $x = 2 \lambda y$ and $x,y,\lambda \ne 0$. Combining the two equation we have $y = 4 \lambda^2 y$ and $\lambda^2 = 1/4$.
Consider the two cases one by one: for $\lambda = 1/2$ we have $x=y$, and for $\lambda = -1/2$ we have $x=-y$.  Taking into account the constraint, each of the two cases leads to two each, namely $x=\pm a$ and $y= \pm a$.

Altogether we get four critical points:

1. $x=a, y=a, \lambda = \frac{1}{2}$,
2. $x=a, y=-a, \lambda = -\frac{1}{2}$,
3. $x=-a, y=a, \lambda = -\frac{1}{2}$,
4. $x=-a, y=-a, \lambda = \frac{1}{2}$.

The bordered Hessian:
%
$$
%
H\mathcal{L}(\lambda, x, y)
= 
\left[
\begin{array}{ccc}
0 & -2x & -2y \\ 
-2x & -2\lambda & 1 \\ 
-2y & 1 & -2\lambda \\
\end{array}
\right]
%
$$
%

Since there are two variables, one constraint, we only
need to check the sign of the determinant of the bordered Hessian (the last leading principal minor):
%
$$
%
\det(H\mathcal{L}(\lambda, x, y)) = 8\big(xy + \lambda (x^2 + y^2)\big).
%
$$
%


Notice that:
%
$$
%
\begin{align*}
& \det(H\mathcal{L}(1/2, a, a)) = \det(H\mathcal{L}(1/2, -a, -a)) = 16a^2 > 0, \\
& \det(H\mathcal{L}(-1/2, -a, a)) = \det(H\mathcal{L}(-1/2, a, -a)) = -16a^2 < 0.
\end{align*}
%
$$
%

Thus, we know that the critical points $(a, a)$ and $(-a, -a)$ are local maximizers, and the critical points $(a, -a)$ and $(-a, a)$ are local minimizers.

In this question, the gloabl maximizer/minimizer exists by Weierstrass theorem and must be some local maximizer/minimizer. 
From $f(a, a) = f(-a, -a) = a^2, f(-a, a) = f(a, -a) = -a^2$, we know the maxima is $a^2$ and the minima is $-a^2$.

**Question H.2**

We first wite down the Lagrangian:
%
$$
%
\mathcal{L}(x, y, \lambda)
= \frac{1}{x} + \frac{1}{y}
- \lambda (\frac{1}{x^2} + \frac{1}{y^2} - \frac{1}{a^2}).
%
$$
%
The F.O.C.s are:
%
$$
%
\nabla \mathcal{L}(\lambda, x, y)
= 
[\begin{array}{ccc}
-(\frac{1}{x^2} + \frac{1}{y^2} - \frac{1}{a^2}), & -\frac{1}{x^2}  + \frac{2\lambda}{x^3}, 
& -\frac{1}{y^2} + \frac{2\lambda}{y^3} \\
\end{array}]
= 0.
%
$$
%
Solving F.O.C.s, we get two solutions:

(1). $x=y=\sqrt{2}a, \lambda = \frac{\sqrt{2}}{2}a.$

(2). $x=y=-\sqrt{2}a, \lambda = -\frac{\sqrt{2}}{2}a.$

The bordered Hessian:
%
$$
%
H\mathcal{L}(\lambda, x, y)
=
\left[
\begin{array}{ccc}
0 & 2/x^3 & 2/y^3 \\ 
2/x^3 & 2/x^3 - 6\lambda/x^4 & 0 \\ 
2/y^3 & 0 & 2/y^3 - 6\lambda/y^4 \\
\end{array}
\right] 
%
$$
%

Since there are two variables, one constraint, we only
need to check the sign of the determinant of the bordered Hessian (the last leading principal minor):
%
$$
%
\det(H\mathcal{L}(\lambda, x, y))
= -8 \Big( 
\frac{y-3\lambda}{x^6y^4} + \frac{x-3\lambda}{x^4y^6}
\Big).
%
$$
%

Since for both critical points, we have $x=y=2\lambda$, 
we only need to consider 
$\det(H\mathcal{L}(x/2, x, x)) = 8/x^9$.

Notice that:
%
$$
%
\begin{align*}
&\det(H\mathcal{L}(\frac{\sqrt{2}}{2}a, \sqrt{2}a, \sqrt{2}a)) = \frac{8}{{(\sqrt{2}a)}^9} > 0.
\\
&\det(H\mathcal{L}(-\frac{\sqrt{2}}{2}a, -\sqrt{2}a, -\sqrt{2}a)) = \frac{8}{{(-\sqrt{2}a)}^9} < 0.
\end{align*}
%
$$
%
Thus, we know that the critical point $(\sqrt{2}a, \sqrt{2}a)$ is local maximizer, and the critical points $(-\sqrt{2}a, -\sqrt{2}a)$ are local minimizers.

In this question, the gloabl maximizer/minimizer exists by Weierstrass theorem and must be some local maximizer/minimizer. 
We know the maxima is $f(\sqrt{2}a, \sqrt{2}a) = \frac{\sqrt{2}}{a}$ and the minima is $f(-\sqrt{2}a, -\sqrt{2}a) = -\frac{\sqrt{2}}{a}$.

**Question H.3**

First, notice that if $x=0$, $f(0, y,z) = 0 < f(1, 1, 1)=1$, thus, $x>0$. Similarly, we can prove $y > 0$ and $z > 0$.

Second, notice that if $x + 2y + z < 10$, we can set $x^{\prime} = 10 - 2y - z$, which implies $x^{\prime} > x$
and $f(x^{\prime}, y, z) > f(x, y, z)$.

Thus, the only binding constraint is $x + 2y + z = 10$.

The Lagrangian is:
%
$$
%
\mathcal{L}(x, y, z, \lambda)
= x y^{1/2}z^{1/3} - \lambda (3x + 2y + z -10).
%
$$
%

The gradient of the Lagrangian w.r.t. $(\lambda, x, y, z)$ is:
%
$$
%
\nabla \mathcal{L}(\lambda, x, y, z)
= 
\begin{pmatrix}
-(3x + 2y + z -10)\\
  y^{1/2}z^{1/3} - 3\lambda\\
  \frac{1}{2}x y^{-1/2}z^{1/3} - 2\lambda\\
  \frac{1}{3}x y^{1/2}z^{-2/3} - \lambda \\
\end{pmatrix}.
%
$$
%

Solve $\nabla \mathcal{L}(\lambda, x, y, z) = 0$, we get $x = z = \frac{4}{3}y = \frac{20}{11}$.

The bordered Hessian:
%
$$
%
H\mathcal{L}(\lambda, x, y, z)
= 
\begin{bmatrix}
0 & -3 & -2 & -1 \\
-3 & 0 & \frac{1}{2}y^{-1/2}z^{1/3} & \frac{1}{3}y^{1/2}z^{-2/3} \\
-2 & \frac{1}{2}y^{-1/2}z^{1/3} & -\frac{1}{4}xy^{-3/2}z^{1/3} & \frac{1}{6}xy^{-1/2}z^{-2/3} \\
-1 & \frac{1}{3}y^{1/2}z^{-2/3} & \frac{1}{6}xy^{-1/2}z^{-2/3} & -\frac{2}{9}xy^{1/2}z^{-5/3} \\
\end{bmatrix}.
%
$$
%

Since there are three variables, one constraint, we need to check the determinant of the bordered Hessian and the last but one
leading principal minor (Let us denote the matrix composed of the intersection of first three rows and first three columns of $H\mathcal{L}$ by $M(\lambda, x, y, z)$).

We can simplify $H\mathcal{L}$ by using
$x = z = \frac{4}{3}y$ at the critical point:

%
$$
%
H\mathcal{L}(\lambda, z, \frac{3}{4}z, z)
= 
\begin{bmatrix}
0 & -3 & -2 & -1 \\
-3 & 0 & \frac{\sqrt{3}}{3}z^{-1/6} & \frac{\sqrt{3}}{6}z^{-1/6} \\
-2 & \frac{\sqrt{3}}{3}z^{-1/6} & -\frac{2\sqrt{3}}{9}z^{-1/6} & \frac{\sqrt{3}}{9}z^{-1/6} \\
-1 & \frac{\sqrt{3}}{6}z^{-1/6} & \frac{\sqrt{3}}{9}z^{-1/6} & -\frac{\sqrt{3}}{9}z^{-1/6}\\
\end{bmatrix}.
%
$$
%

The determinants are:
%
$$
%
\det(H\mathcal{L}(\lambda, z, \frac{3}{4}z, z))
= -\frac{11}{3}z^{-1/3} < 0%
$$
%
and 
%
$$
%
\det(M(\lambda, z, \frac{3}{4}z, z)) = 6\sqrt{3}z^{-1/6} > 0
%
$$
%
since $z = 20/11$ at the critical point.

Thus, the sign of the last leading principal minor is negative, and the sign of the determinant of the last but one leading principal minor is positive (recall there are three variables, and we need to confirm 
$H_{(x, y, z)}\mathcal{L}(\lambda, x, y, z)$ is 
negative definite on the constraint set). Thus, the critical point is a local maximizer.

By Weierstrass theorem, we know the unique local maximizer must be the global maximizer.
The maxima is $f(20/11, 15/11, 20/11) = (\frac{20}{11})^{4/3} (\frac{15}{11})^{1/2}$.


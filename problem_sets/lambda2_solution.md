The Lagrangian function is

$$
\mathcal{L}(\lambda,x,y) = -x^2 - \lambda (-x^2 + y^2 +2xy + 2)
$$

KKT conditions are

$$
\left\{
\begin{array}{rl}
\frac{\partial \mathcal{L}}{\partial x} &= 
-2x + 2\lambda x - 2\lambda y = 0,\\
\frac{\partial \mathcal{L}}{\partial y} &=
- 2\lambda y - 2\lambda x = 0,\\
& -x^2 + y^2 +2xy + 2 \le 0,\\
& \lambda \ge 0,\\
& \lambda (-x^2 + y^2 +2xy + 2) = 0.
\end{array}
\right.
$$

**Case 1:** $\lambda = 0$

This is the unconstrained case with the number of variables $N=2$.
KKT conditions simplify to

$$
\left\{
\begin{array}{l}
-2x = 0,\\
-x^2 + y^2 +2xy + 2 \le 0
\end{array}
\right.
$$

Thus, $x=0$, but then $y^2+2>0$ for any $y$, and therefore the inequality is violated.
We conclude that $\lambda=0$ is not a solution.


**Case 2:** $\lambda > 0$

This is a constrained case with the number of variables $N=2$ and number of *binding* constraints equal $K=1$.
KKT conditions simplify to

$$
\left\{
\begin{array}{l}
-2x + 2\lambda x - 2\lambda y = 0,\\
- 2\lambda y - 2\lambda x = 0,\\
-x^2 + y^2 +2xy + 2 = 0.
\end{array}
\right.
$$

$$
\left\{
\begin{array}{l}
x -\lambda x +\lambda y = 0,\\
y + x = 0,\\
x^2 - y^2 -2xy - 2 = 0.
\end{array}
\right.
$$

The last equation simplifies to 
$(x - y)(x+y) -2xy - 2 = -2(xy+1) = 0$, and thus $xy+1=0$.
Combining the last equation with $y + x = 0$, we have

$$
\begin{array}{l}
x-\frac{1}{x}=0 \\
x^2-1=0 \\
(x-1)(x+1)=0\\
x = \pm 1
\end{array}
$$

Then, the two stationary points are $(x,y) = (1,-1)$ and $(x,y) = (-1,1)$, with $\lambda = x/(x-y) = 1/2$ for both points.

Let's check the second-order conditions for each of these points:

1. $(x,y) = (1,-1)$, $\lambda=1/2$

The boarded Hessian is

$$
H\mathcal{L} = 
\begin{pmatrix}
0 & -2x+2y & 2y+2x \\
-2x+2y & -2 +2\lambda & -2\lambda \\
2y+2x & -2\lambda & -2\lambda
\end{pmatrix}
=
\begin{pmatrix}
0 & -4 & 0 \\
-4 & -1 & -1 \\
0 & -1 & -1
\end{pmatrix}
$$

We first have to check $N-K=1$ determinant of the bordered Hessian, no rows/columns to be removed:

$$
\det
\begin{pmatrix}
0 & -4 & 0 \\
-4 & -1 & -1 \\
0 & -1 & -1
\end{pmatrix}
= 4 \det
\begin{pmatrix}
-4 & 0 \\
-1 & -1
\end{pmatrix}
=16 >0
$$

The sign of the full determinant is the same as $(-1)^N$, the alternation sequence of one element is satisfied trivially, thus we conclude that the relevant quadratic form is negative definite, and thus point $(1,-1)$ is a *local maximizer*.

1. $(x,y) = (-1,1)$, $\lambda=1/2$

The boarded Hessian is

$$
H\mathcal{L} = 
\begin{pmatrix}
0 & 4 & 0 \\
4 & -1 & -1 \\
0 & -1 & -1
\end{pmatrix}
$$

Similar to the previous point, we have 

$$
\det
\begin{pmatrix}
0 & 4 & 0 \\
4 & -1 & -1 \\
0 & -1 & -1
\end{pmatrix}
= -4 \det
\begin{pmatrix}
4 & 0 \\
-1 & -1
\end{pmatrix}
= (-4)(-4) = 16 >0
$$

Again, we conclude that at point $(-1,1)$ the objective function attains a *local maximum*.


Finally, to find the global maximum, we can compare the values of the objective function at the stationary points:

- $f(1,-1) = - 1^2 = -1$
- $f(-1,1) = - (-1)^2 = -1$

Thus, the problem has two global maximizers which coincide with the two found local constrained maximizers $(1,-1)$ and $(-1,1)$.



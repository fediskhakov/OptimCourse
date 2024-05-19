We first wite down the Lagrangian:

$$
\mathcal{L}(x, y, \lambda)
= xy - \lambda(x^2 + y^2 - 2a^2).
$$

We have:

$$
\nabla \mathcal{L}(\lambda, x, y) = \left( \begin{array}{ccc}
-(x^2 + y^2 - 2a^2), & y - 2\lambda x, & x - 2\lambda y
\end{array}
\right).
$$

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

$$
H\mathcal{L}(\lambda, x, y)
= 
\left[
\begin{array}{ccc}
0 & -2x & -2y \\ 
-2x & -2\lambda & 1 \\ 
-2y & 1 & -2\lambda \\
\end{array}
\right]
$$

Since there are two variables, one constraint ($N=2$, $K=1$, $N-K=1$), we only need to check the sign of the determinant of the bordered Hessian (the last leading principal minor):

$$
\det(H\mathcal{L}(\lambda, x, y)) = 8\big(xy + \lambda (x^2 + y^2)\big).
$$

Notice that:

$$
\begin{array}{rl}
& \det(H\mathcal{L}(1/2, a, a)) = \det(H\mathcal{L}(1/2, -a, -a)) = 16a^2 > 0, \\
& \det(H\mathcal{L}(-1/2, -a, a)) = \det(H\mathcal{L}(-1/2, a, -a)) = -16a^2 < 0.
\end{array}
$$

Since $(-1)^K=-1$, we conclude that the critical points $(a, a)$ and $(-a, -a)$ satisfy the pattern for negative definiteness, and the critical points $(-a, a)$ and $(a, -a)$ satisfy the pattern for positive definiteness. 
Thus, the critical points $(a, a)$ and $(-a, -a)$
are local maximizers, and the critical points $(a, -a)$ and $(-a, a)$ are local minimizers.

In this question, the gloabl maximizer/minimizer exists by Weierstrass theorem and must be some local maximizer/minimizer. 
From $f(a, a) = f(-a, -a) = a^2, f(-a, a) = f(a, -a) = -a^2$, we know the maxima is $a^2$ and the minima is $-a^2$.

We first wite down the Lagrangian:

$$
\mathcal{L}(x, y, \lambda)
= \frac{1}{x} + \frac{1}{y}
- \lambda (\frac{1}{x^2} + \frac{1}{y^2} - \frac{1}{a^2}).
$$

The F.O.C.s are:

$$
\nabla \mathcal{L}(\lambda, x, y)
= 
[\begin{array}{ccc}
-(\frac{1}{x^2} + \frac{1}{y^2} - \frac{1}{a^2}), & -\frac{1}{x^2}  + \frac{2\lambda}{x^3}, 
& -\frac{1}{y^2} + \frac{2\lambda}{y^3} \\
\end{array}]
= 0.
$$

Solving F.O.C.s, we get two solutions:

1. $x=y=\sqrt{2}a, \lambda = \frac{\sqrt{2}}{2}a.$
2. $x=y=-\sqrt{2}a, \lambda = -\frac{\sqrt{2}}{2}a.$

The bordered Hessian:

$$
H\mathcal{L}(\lambda, x, y)
=
\left[
\begin{array}{ccc}
0 & 2/x^3 & 2/y^3 \\ 
2/x^3 & 2/x^3 - 6\lambda/x^4 & 0 \\ 
2/y^3 & 0 & 2/y^3 - 6\lambda/y^4 \\
\end{array}
\right] 
$$

Since there are two variables, one constraint ($N=2$, $K=1$, $N-K=1$), we only need to check the sign of the determinant of the bordered Hessian (the last leading principal minor):

$$
\det(H\mathcal{L}(\lambda, x, y))
= -8 \Big( 
\frac{y-3\lambda}{x^6y^4} + \frac{x-3\lambda}{x^4y^6}
\Big).
$$

Since for both critical points, we have $x=y=2\lambda$, 
we only need to consider 
$\det(H\mathcal{L}(x/2, x, x)) = 8/x^9$.

Notice that:

$$
\begin{array}{rl}
&\det(H\mathcal{L}(\frac{\sqrt{2}}{2}a, \sqrt{2}a, \sqrt{2}a)) = \frac{8}{{(\sqrt{2}a)}^9} > 0.
\\
&\det(H\mathcal{L}(-\frac{\sqrt{2}}{2}a, -\sqrt{2}a, -\sqrt{2}a)) = \frac{8}{{(-\sqrt{2}a)}^9} < 0.
\end{array}
$$

Thus, we know that the critical point $(\sqrt{2}a, \sqrt{2}a)$ is local maximizer, and the critical points $(-\sqrt{2}a, -\sqrt{2}a)$ are local minimizers.

In this question, the gloabl maximizer/minimizer exists by Weierstrass theorem and must be some local maximizer/minimizer. 
We know the maxima is $f(\sqrt{2}a, \sqrt{2}a) = \frac{\sqrt{2}}{a}$ and the minima is $f(-\sqrt{2}a, -\sqrt{2}a) = -\frac{\sqrt{2}}{a}$.

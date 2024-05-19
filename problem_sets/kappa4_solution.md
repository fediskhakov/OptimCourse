First, notice that if $x=0$, $f(0, y,z) = 0 < f(1, 1, 1)=1$, thus, $x>0$. 
Similarly, we can prove $y > 0$ and $z > 0$.

Second, notice that if $x + 2y + z < 10$, we can set $x^{\prime} = 10 - 2y - z$, which implies $x^{\prime} > x$ and $f(x^{\prime}, y, z) > f(x, y, z)$.

Thus, the only binding constraint is $x + 2y + z = 10$.

The Lagrangian is:

$$
\mathcal{L}(x, y, z, \lambda)
= x y^{1/2}z^{1/3} - \lambda (3x + 2y + z -10).
$$

The gradient of the Lagrangian w.r.t. $(\lambda, x, y, z)$ is:

$$
\nabla \mathcal{L}(\lambda, x, y, z)
= 
\begin{pmatrix}
-(3x + 2y + z -10)\\
  y^{1/2}z^{1/3} - 3\lambda\\
  \frac{1}{2}x y^{-1/2}z^{1/3} - 2\lambda\\
  \frac{1}{3}x y^{1/2}z^{-2/3} - \lambda \\
\end{pmatrix}.
$$

Solve $\nabla \mathcal{L}(\lambda, x, y, z) = 0$, we get $x = z = \frac{20}{11}$, $y = \frac{15}{11}$.

The bordered Hessian:

$$
H\mathcal{L}(\lambda, x, y, z)
= 
\begin{bmatrix}
0 & -3 & -2 & -1 \\
-3 & 0 & \frac{1}{2}y^{-1/2}z^{1/3} & \frac{1}{3}y^{1/2}z^{-2/3} \\
-2 & \frac{1}{2}y^{-1/2}z^{1/3} & -\frac{1}{4}xy^{-3/2}z^{1/3} & \frac{1}{6}xy^{-1/2}z^{-2/3} \\
-1 & \frac{1}{3}y^{1/2}z^{-2/3} & \frac{1}{6}xy^{-1/2}z^{-2/3} & -\frac{2}{9}xy^{1/2}z^{-5/3} \\
\end{bmatrix}.
$$

Since there are three variables, one constraint ($N=3$, $K=1$, $N-K=2$), we need to check 
two last leading principal minors of $H\mathcal{L}$, that is the determinant of the bordered Hessian and the determinant of the $H\mathcal{L}$ where last column and last row are removed.
Denote the matrix composed of the intersection of first three rows and first three columns of $H\mathcal{L}$ by $M(\lambda, x, y, z)$.

We can simplify $H\mathcal{L}$ by using
$x = z = \frac{4}{3}y$ at the critical point:

$$
H\mathcal{L}(\lambda, z, \frac{3}{4}z, z)
= 
\begin{bmatrix}
0 & -3 & -2 & -1 \\
-3 & 0 & \frac{\sqrt{3}}{3}z^{-1/6} & \frac{\sqrt{3}}{6}z^{-1/6} \\
-2 & \frac{\sqrt{3}}{3}z^{-1/6} & -\frac{2\sqrt{3}}{9}z^{-1/6} & \frac{\sqrt{3}}{9}z^{-1/6} \\
-1 & \frac{\sqrt{3}}{6}z^{-1/6} & \frac{\sqrt{3}}{9}z^{-1/6} & -\frac{\sqrt{3}}{9}z^{-1/6}\\
\end{bmatrix}.
$$

The determinants are:

$$
\det(H\mathcal{L}(\lambda, z, \frac{3}{4}z, z))
= -\frac{11}{3}z^{-1/3} < 0
$$

and 

$$
\det(M(\lambda, z, \frac{3}{4}z, z)) = 6\sqrt{3}z^{-1/6} > 0
$$

since $z = 20/11$ at the critical point.

Thus, the sign of the last leading principal minor is negative, and the sign of the determinant of the last but one leading principal minor is positive (recall there are three variables, and we need to confirm 
$H_{(x, y, z)}\mathcal{L}(\lambda, x, y, z)$ is 
negative definite on the constraint set). Thus, the critical point is a local maximizer.

By Weierstrass theorem, we know the unique local maximizer must be the global maximizer.
The maxima is 
$f(20/11, 15/11, 20/11) = (\frac{20}{11})^{4/3} (\frac{15}{11})^{1/2}$.

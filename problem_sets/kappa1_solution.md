Let $f(x,y)= x^3/3 - 3y^2 + 2x$ and $g(x,y)=4x-y^3$ for all $x,y \in \mathbb{R}$.
The constraint set is $\{(x,y): g(x,y)=0\}$.
The Lagrangian function is

$$
\mathcal{L}(x,y,\lambda) = f(x,y) - \lambda g(x,y) = f(x,y)= x^3/3 - 3y^2 + 2x - \lambda(4x-y^3)
$$

The first order partial derivatives are

$$
\frac{\partial \mathcal{L}}{\partial x}= x^2 + 2 - 4 \lambda, \quad \\
\frac{\partial \mathcal{L}}{\partial y}= -6y + 3\lambda y^2, \quad \\
\frac{\partial \mathcal{L}}{\partial \lambda}= -(4x -y^3).
$$

The bordered Hessian matrix is

$$
H \mathcal{L}(x,y,\lambda)) =
\begin{pmatrix}
0 & \frac{\partial^2 \mathcal{L}}{\partial \lambda \partial x} & \frac{\partial^2 \mathcal{L}}{\partial \lambda \partial y}\\
\frac{\partial^2 \mathcal{L}}{\partial \lambda \partial x}& \frac{\partial^2 \mathcal{L}}{\partial x^2} & \frac{\partial^2 \mathcal{L}}{\partial x \partial y} \\
\frac{\partial^2 \mathcal{L}}{\partial \lambda \partial y}& \frac{\partial^2 \mathcal{L}}{\partial y \partial x} & \frac{\partial^2 \mathcal{L}}{\partial y^2}
\end{pmatrix} =
\begin{pmatrix}
0& -4& 3y^2 \\
-4& 2x & 0\\
3y^2& 0&-6 + 6 \lambda y
\end{pmatrix}.
$$

Observe that $\mathrm{rank}(Dg)) = \mathrm{rank}((-4, 3 y^2)) = 1$ for all $x,y \in \mathbb{R}$.
That is, the constrained qualification holds for all points on the constraint.

The first order conditions are

$$
\frac{\partial \mathcal{L}}{\partial x}= x^2 + 2 - 4 \lambda =0, \quad \\
\frac{\partial \mathcal{L}}{\partial y}= -6y + 3\lambda y^2 =0, \quad \\
\frac{\partial \mathcal{L}}{\partial \lambda}= -(4x -y^3)=0.
$$

Observe that if $\lambda=0$, then the FOCs imply $x^2+2-4\lambda = x^2+2 = 0$, which is a contradiction since $x^2+2 \ge 2$.
It must be that $\lambda \ne 0$.
Next, from the equation $-6y+3\lambda y^2 = 3y(\lambda y -2)=0$, it is either $y=0$ or $y = \lambda/2$.

Case 1: Suppose that $y=0$.
Then, from the constraint $4x=y^3$ we get $x=0$. Also, the FOC yields $x^2+2 - 4\lambda = 0+2-4\lambda=0$ so that $\lambda=1/2$.
Hence, the optimizer is $(x^*, y^*, \lambda^*)=(0,0,1/2)$.
The corresponding bordered Hessian matrix is

$$
H\mathcal{L}(0,0,1/2)=
\begin{pmatrix}
0 &-4 & 0\\ -4& 0&0\\ 0 &0& -6
\end{pmatrix}
$$

Since there are two variables $N=2$ and one constraint $K=1$, it suffices to check the last ($N-K=1$) leading principal minor, i.e., the determinant of the full bordered Hessian matrix.
The determinant follows

$$
\det (H\mathcal{L})=0 - (-4)\begin{vmatrix}-4&0 \\ 0& -6 \end{vmatrix} = 96 >0.
$$

It has the same sign as $(-1)^N=(-1)^2$.
Therefore, the bordered Hessian matrix is negative definite and $(x^*, y^*, \lambda^*)=(0,0,1/2)$ is a local maximizer on the constraint set.

Case 2: Suppose that $y=2/\lambda$.
Then, by $\lambda = 2/y$ and $x = y^3/4$, the FOCs yield

$$
x^2 + 2 - 4 \lambda = y^6/16 + 2 - 8/y = 0 \\
\Rightarrow y^7 + 32 y - 128=0
$$

Let $h(y)=y^7 + 32 y - 128$. Since $h'(y)=7 y^6+32 >0$, function $h$ is strictly increasing.
Note that the solution for $h(y)=0$ is strictly positive since $y^7$ and $y$ have the same sign.
We can verify that $y^* \approx 1.8325$ solves $h(y)=0$.
The optimizer is $(x^*, y^*,\lambda^*)=(\bar{y}^{3}/4, \bar{y}, 2/\bar{y})$ where $\bar{y}$ satisfies $h(\bar{y})=0$.
The corresponding bordered Hessian is

$$
H\mathcal{L}(\bar{y}^{3}/4, \bar{y}, 2/\bar{y})=
\begin{pmatrix}
0& -4& 3 \bar{y}^{2} \\
-4& 2(\bar{y}^{3}/4) & 0\\
3y^2& 0&-6 + 6 (2/\bar{y}) \bar{y}
\end{pmatrix} =
\begin{pmatrix}
0& -4& 3 \bar{y}^{2} \\
-4& \bar{y}^{3}/2 & 0\\
3y^2& 0&6
\end{pmatrix}.
$$

The determinant is

$$
\det (H\mathcal{L})= - (-4)\begin{vmatrix}-4& 3\bar{y}^2 \\ 0& 6 \end{vmatrix}
+3 \bar{y}^2 \begin{vmatrix}-4& 3\bar{y}^2 \\ \bar{y}^3/2& 0 \end{vmatrix} =
-\frac{9}{2}\bar{y}^7 - 96 <0,
$$

where the last inequality holds since $\bar{y}$ is positive.
Therefore, $H\mathcal{L}$ has the same sign as $(-1)^K= -1$ so that it is positive definite.
Hence, $(x^*, y^*,\lambda^*)=(\bar{y}^{3}/4, \bar{y}, 2/\bar{y})$ is a local minimizer on the constraint set.

Finally, since $f(x,y) = x^3/3-3y^2+2x = x^3-3(4x)^{1/3}+2x \rightarrow \infty$ as $x \rightarrow \infty$, there is no global maximizer.
The local maximizer on the constraint is $(x,y)=(0,0)$.


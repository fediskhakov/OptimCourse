The constraint is $g(x,y) := x^2-y^2 - 1 \le 0$.
The Lagrangian function is

$$
\mathcal{L}(x,y,\lambda) = x^3-y^3- \lambda (x^2 + y^2-1)
$$

The necessary KKT conditions are given by the following system of equations and inequalities

$$
\begin{array}{rl}
\frac{\partial \mathcal{L}}{\partial x} =& 3x^2  - 2 \lambda x=0\\
\frac{\partial \mathcal{L}}{\partial y} =& -3 y^2 -2 \lambda y=0 \\
& x^2- y^2-1 \le 0 \\
& \lambda \ge 0 \\
& \lambda g(x,y) = \lambda (x^2- y^2-1) = 0
\end{array}
$$

To solve this system, we start from checking the two possible cases: $\lambda=0$ and $\lambda>0$.

*Case 1.* $\lambda=0$: the constraint could not be binding.
Then, the FOCs imply $x=y=0$.
The unconstrained Hessian matrix is

$$
Hf(0,0) = \begin{pmatrix}
\frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\
\frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2}
\end{pmatrix}_{(x,y)=(0,0)}
= \begin{pmatrix}
6x & 0\\ 0 & -6y
\end{pmatrix}_{(x,y)=(0,0)}
= \begin{pmatrix}
0 & 0\\ 0 & 0
\end{pmatrix}_{(x,y)=(0,0)}
$$

We have $\det(H)=0$ and $trace(H)=0$ so that there is no sufficient information to conclude the property of the stationary point.

*Case 2.* $\lambda>0$: the constraint is binding.
Then, the problem is the optimization with equality constraint, given two control variables $N=2$ and one constraint $K=1$.
From the FOCs, we have

$$
\begin{array}{l}
0=3x^2  - 2 \lambda x= x(3x -2\lambda) \Longrightarrow x=0, \text{ or  } x = \frac{2}{3}\lambda\\
0=-3 y^2 -2 \lambda y= y(-3y-2\lambda) \Longrightarrow y=0, \text{ or  } y = -\frac{2}{3}\lambda
\end{array}
$$

Since further we have the constraint $x^2+y^2=1$, there are three cases: "$x=0, y<0$", "$x>0, y=0$" or "$x>0, y<0$".

**(i)** If $x>0, y<0$, then it follows from the above conditions that

$$
\frac{3}{2}x =\lambda = -\frac{3}{2}y \\
\implies y=-x.
$$

Since $x^2+y^2=1$ and $x>0, y<0$, we have $x=1/\sqrt{2}, y=-1/\sqrt{2}$ and then $\lambda= 3/(2\sqrt{2})$.

Observe that $\mathrm{rank}(Dg)) = \mathrm{rank}((2x, 2y)) = 1$ for $x \ne 0$ or $y\neq0$, so the constrained qualification holds for any point on the boundary.

The bordered Hessian matrix is

$$
H \mathcal{L}(x,y,\lambda)) =
\begin{pmatrix}
0 & \frac{\partial^2 \mathcal{L}}{\partial \lambda \partial x} & \frac{\partial^2 \mathcal{L}}{\partial \lambda \partial y}\\
\frac{\partial^2 \mathcal{L}}{\partial \lambda \partial x}& \frac{\partial^2 \mathcal{L}}{\partial x^2} & \frac{\partial^2 \mathcal{L}}{\partial y \partial x} \\
\frac{\partial^2 \mathcal{L}}{\partial \lambda \partial y}& \frac{\partial^2 \mathcal{L}}{\partial x \partial y} & \frac{\partial^2 \mathcal{L}}{\partial y^2}
\end{pmatrix} =
\begin{pmatrix}
0& -2x& -2y \\
-2x& 6x -2\lambda & 0\\
-2y& 0&-6y -2\lambda
\end{pmatrix}.
$$

Now, the bordered Hessian at $(x,y,\lambda) = (1/\sqrt{2}, -1/\sqrt{2}, 3/(2\sqrt{2}))$ is

$$
H \mathcal{L} (1/\sqrt{2}, -1/\sqrt{2}, 3/(2\sqrt{2}))=
\begin{pmatrix}
0& -\sqrt{2}& \sqrt{2} \\
-\sqrt{2}& 3\sqrt{2} -3/\sqrt{2} & 0\\
\sqrt{2}& 0& 3\sqrt{2} -3/\sqrt{2}
\end{pmatrix}.
$$

It suffices to check the last leading principal minor.
The determinant is

$$
\det (H \mathcal{L} (1/\sqrt{2}, -1/\sqrt{2}, 3/(2\sqrt{2})) 
= -(-\sqrt{2})\begin{vmatrix}
-\sqrt{2}& \sqrt{2} \\ 0& 3\sqrt{2} -3/\sqrt{2}
\end{vmatrix} + \sqrt{2}\begin{vmatrix}
-\sqrt{2}& \sqrt{2} \\ 3\sqrt{2} -3/\sqrt{2} & 0
\end{vmatrix}\\
= -6\sqrt{2} < 0,
$$

which has the same sign as $(-1)^K=(-1)$.
Therefore, it is positive definite and we have a local minimum on the boundary.

**(ii)** If $x=0, y<0$, then from $x^2+y^2=1$, we have $y=-1$.
Also, $\lambda=-3y/2 = 3/2$. The border Hessian is

$$
H \mathcal{L}(0,-1,\frac{3}{2})) =
\begin{pmatrix}
0& -2x& -2y \\
-2x& 6x -2\lambda & 0\\
-2y& 0&-6y -2\lambda
\end{pmatrix} = \begin{pmatrix}
0&0& 2\\
0& -3 &0\\
2&0 & 3
\end{pmatrix}.
$$

The determinant is $\det (H\mathcal{L})=12 >0$, which has the same sign as $(-1)^2$ and then the Hessian matrix is negative definite.
Therefore, $(0, -1)$ is a local maximum.

**(iii)** If $x>0, y=0$, then from $x^2+y^2=1$, we have $x=1$.
Also, $\lambda=3x/2 = 3/2$. The border Hessian is

$$
H \mathcal{L}(1,0,\frac{3}{2})) =
\begin{pmatrix}
0& -2x& -2y \\
-2x& 6x -2\lambda & 0\\
-2y& 0&-6y -2\lambda
\end{pmatrix} = \begin{pmatrix}
0&-2& 0\\
-2& 3 &0\\
0&0 & -3
\end{pmatrix}.
$$

The determinant is $\det (H\mathcal{L})=12 >0$, which has the same sign as $(-1)^2$ and then the Hessian matrix is negative definite.
Therefore, $(1, 0)$ is a local maximum.

Finally, the objective values for the local maximums are $f(1,0)=f(0,-1)=1$ and note that the constrained set is compact.
Therefore, these two local maximizers are also global maximizers.



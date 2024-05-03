## $T_1$

**1.**

To find eigenvalues solve

$$
\det
\begin{pmatrix}
4/3-\lambda & -2/3 & 0 \\
-1/3 & 5/3-\lambda & 0 \\
0 & 0 & -1-\lambda
\end{pmatrix}
=
-(1+\lambda)
\begin{pmatrix}
4/3-\lambda & -2/3 \\
-1/3 & 5/3-\lambda
\end{pmatrix}
=
$$

$$
=
-(1+\lambda)
\left[\left(\frac{4}{3}-\lambda \right)\left(\frac{5}{3}-\lambda \right)-\frac{2}{3\cdot3}\right]
=
-(1+\lambda)
(\lambda^2-3\lambda+\frac{4\cdot 5}{9}-\frac{2}{9})
=
$$

$$
= -(1+\lambda)(\lambda^2-3\lambda+2)
= -(1+\lambda)(\lambda-1)(\lambda-2)
$$

Therefore the eigenvalues are $\lambda_1=-1$, $\lambda_2=1$ and $\lambda_3=2$


**2.**

To find eigenvectors plug the eigenvalues one by one to $T_1-\lambda I$ and investigate the implications of the resulting system of equations. We should expect to find *multiple* eigenvectors for each eigenvalue, and therefore are looking for a formula rather than a usual answer.

$$
T_1 - \lambda_1 I=0 \iff
\begin{pmatrix}
7/3 & -2/3 & 0 \\
-1/3 & 8/3 & 0 \\
0 & 0 & 0
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}
=
\begin{pmatrix}
0 \\ 0 \\ 0
\end{pmatrix}
$$

Thus, any value of $z$ will do, for example $z=1$. To find $x$ and $y$ we can use the first two equations (multiplied by 3 right away):

$$
\left\{
\begin{array}{rcl}
7x - 2y &=& 0 \\
-x + 8y &=& 0
\end{array}
\right.
\implies
\left\{
\begin{array}{l}
x = 0 \\
y = 0
\end{array}
\right.
$$

Therefore, the vector $v_1 = (0,0,1)$ is an eigenvector for $\lambda_1=-1$.

$$
T_1 - \lambda_2 I=0 \iff
\begin{pmatrix}
1/3 & -2/3 & 0 \\
-1/3 & 2/3 & 0 \\
0 & 0 & -1
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}
=
\begin{pmatrix}
0 \\ 0 \\ 0
\end{pmatrix}
\iff
$$

$$
\iff
\begin{pmatrix}
1 & -2 & 0 \\
1 & -2 & 0 \\
0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}
=
\begin{pmatrix}
0 \\ 0 \\ 0
\end{pmatrix}
$$

Obviously, all vectors of the form $(2a,a,0)$ are eigenvectors for $\lambda_2=1$.
In particular, $v_2 = (2/\sqrt{5},1/\sqrt{5},0)$ has a norm of 1.

$$
T_1 - \lambda_3 I=0 \iff
\begin{pmatrix}
-2/3 & -2/3 & 0 \\
-1/3 & -1/3 & 0 \\
0 & 0 & -1
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}
=
\begin{pmatrix}
0 \\ 0 \\ 0
\end{pmatrix}
\iff
$$

$$
\iff
\begin{pmatrix}
1 & 1 & 0 \\
1 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}
=
\begin{pmatrix}
0 \\ 0 \\ 0
\end{pmatrix}
$$

Now, all vectors of the form $(a,-a,0)$ are eigenvectors for $\lambda_3=2$.
In particular, $v_3 = (1/\sqrt{2},-1/\sqrt{2},0)$ has a norm of 1.

**3.**

We have chosen the eigenvectors in such a way that they are already normalized, i.e. have length of 1. To verify, observe

$$
\begin{array}{l}
\|v_1\| = \sqrt{0^2+0^2+1^2} = 1 \\
\|v_2\| = \sqrt{(2/\sqrt{5})^2+(1/\sqrt{5})^2+0^2} = 1 \\
\|v_2\| = \sqrt{(1/\sqrt{2})^2+(-1/\sqrt{2})^2+0^2} = 1
\end{array}
$$

It's easy to verify that vectors $v_1, v_2, v_3$ are linearly independent, and therefore the set 

$$
\{v_1, v_2, v_3\} =
\left\{
\begin{pmatrix}
0 \\ 0 \\ 1
\end{pmatrix},
\begin{pmatrix}
2/\sqrt{5} \\ 1/\sqrt{5} \\ 0
\end{pmatrix},
\begin{pmatrix}
1/\sqrt{2} \\ -1/\sqrt{2} \\ 0
\end{pmatrix}
\right\}
$$

forms a normalized basis in $\mathbb{R}^3$

**4.**

The transformation matrix is a matrix with columns formed from the vectors of the new basis expressed in coordinates (``the language'') of the old basis.

$$
P = 
\begin{pmatrix}
0 & 2/\sqrt{5} & 1/\sqrt{2} \\ 
0 & 1/\sqrt{5} & -1/\sqrt{2} \\ 
1 & 0 & 0
\end{pmatrix}
$$

**5.**

The matrix $T$ and the matrix $T'$ in the new basis are related as

$$
T = P T' P^{-1} \quad \iff \quad T' = P^{-1} T P
$$

In any case, we need $P^{-1}$.
In order to find the inverse of the $P$ matrix, we make the following argument.
By definition, $PP^{-1} = I$, and therefore the columns of the unknown matrix $P^{-1}$ (denoted below $p'_i$, $i=1,2,3$) are solutions of the following three systems of equations:

$$
P p'_1 =
\begin{pmatrix}
1 \\ 0 \\ 0
\end{pmatrix}
\quad
P p'_2 =
\begin{pmatrix}
0 \\ 1 \\ 0
\end{pmatrix}
\quad
P p'_3 =
\begin{pmatrix}
0 \\ 0 \\ 1
\end{pmatrix}
$$

We can find the solutions of all three systems by [Gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination) performing [elementary row operations](https://en.wikipedia.org/wiki/Elementary_matrix#Operations) on an ``extra'' augmented matrix with three columns in place of the right-hand side.

$$
\left(\begin{array}{ccc|ccc}
0 & 2/\sqrt{5} & 1/\sqrt{2} &
1 & 0 & 0 \\
0 & 1/\sqrt{5} & -1/\sqrt{2} &
0 & 1 & 0 \\
1 & 0 & 0 & 
0 & 0 & 1
\end{array}\right)
\longrightarrow
$$

$$
\left(\begin{array}{ccc|ccc}
1 & 0 & 0 & 
0 & 0 & 1 \\
0 & 1 & -\sqrt{5}/\sqrt{2} &
0 & \sqrt{5} & 0 \\
0 & 2/\sqrt{5} & 1/\sqrt{2} &
1 & 0 & 0
\end{array}\right)
\longrightarrow
$$

$$
\frac{1}{\sqrt{2}} + \left(-\frac{\sqrt{5}}{\sqrt{2}}\right)\left(-\frac{2}{\sqrt{5}}\right) = 
\frac{1}{\sqrt{2}} + \frac{2}{\sqrt{2}} =
\frac{3}{\sqrt{2}}
$$

$$
\left(\begin{array}{ccc|ccc}
1 & 0 & 0 & 
0 & 0 & 1 \\
0 & 1 & -\sqrt{5}/\sqrt{2} &
0 & \sqrt{5} & 0 \\
0 & 0 & 3/\sqrt{2} &
1 & -2 & 0
\end{array}\right)
\longrightarrow
$$

$$
\left(\begin{array}{ccc|ccc}
1 & 0 & 0 & 
0 & 0 & 1 \\
0 & 1 & -\sqrt{5}/\sqrt{2} &
0 & \sqrt{5} & 0 \\
0 & 0 & 1 &
\sqrt{2}/3 & -2\sqrt{2}/3 & 0
\end{array}\right)
\longrightarrow
$$

$$
\sqrt{5} + \frac{\sqrt{5}}{\sqrt{2}} \left(-\frac{2 \sqrt{2}}{3} \right) =
\frac{\sqrt{5}}{3}
$$

$$
\left(\begin{array}{ccc|ccc}
1 & 0 & 0 & 
0 & 0 & 1 \\
0 & 1 & 0 &
\sqrt{5}/3 & \sqrt{5}/3 & 0 \\
0 & 0 & 1 &
\sqrt{2}/3 & -2\sqrt{2}/3 & 0
\end{array}\right)
\longrightarrow
$$

Therefore, the inverse of the $P$ matrix is given by

$$
P^{-1} =
\begin{pmatrix}
0 & 0 & 1 \\
\sqrt{5}/3 & \sqrt{5}/3 & 0 \\
\sqrt{2}/3 & -2\sqrt{2}/3 & 0
\end{pmatrix}
$$

**Additional exercise:** verify that $PP^{-1} = I$.

Now we can compute $P^{-1} T_1 P$:

$$
\begin{pmatrix}
0 & 0 & 1 \\
\sqrt{5}/3 & \sqrt{5}/3 & 0 \\
\sqrt{2}/3 & -2\sqrt{2}/3 & 0
\end{pmatrix}
\begin{pmatrix}
4/3 & -2/3 & 0 \\
-1/3 & 5/3 & 0 \\
0 & 0 & -1
\end{pmatrix}
\begin{pmatrix}
0 & 2/\sqrt{5} & 1/\sqrt{2} \\ 
0 & 1/\sqrt{5} & -1/\sqrt{2} \\ 
1 & 0 & 0
\end{pmatrix}
=
$$

$$
\begin{pmatrix}
0 & 0 & -1 \\
\frac{4\sqrt{5}}{9}-\frac{\sqrt{5}}{9} &
\frac{-2\sqrt{5}}{9}+\frac{5\sqrt{5}}{9} &
0 \\
\frac{4\sqrt{2}}{9}+\frac{2\sqrt{2}}{9} &
\frac{-2\sqrt{2}}{9}-\frac{10\sqrt{2}}{9} &
0 
\end{pmatrix}
\begin{pmatrix}
0 & 2/\sqrt{5} & 1/\sqrt{2} \\ 
0 & 1/\sqrt{5} & -1/\sqrt{2} \\ 
1 & 0 & 0
\end{pmatrix}
=
$$

$$
\begin{pmatrix}
0 & 0 & -1 \\
\frac{\sqrt{5}}{3} & \frac{\sqrt{5}}{3} & 0 \\
\frac{2\sqrt{2}}{3} & \frac{-4\sqrt{2}}{3} & 0 
\end{pmatrix}
\begin{pmatrix}
0 & 2/\sqrt{5} & 1/\sqrt{2} \\ 
0 & 1/\sqrt{5} & -1/\sqrt{2} \\ 
1 & 0 & 0
\end{pmatrix}
=
$$

$$
\begin{pmatrix}
-1 & 0 & 0 \\
0 & \frac{2}{3} + \frac{1}{3} & 
\frac{\sqrt{5}}{3\sqrt{2}} - \frac{\sqrt{5}}{3\sqrt{2}} \\
0 & \frac{4\sqrt{2}}{3\sqrt{5}} - \frac{-4\sqrt{2}}{3\sqrt{5}} &
\frac{2}{3} + \frac{4}{3}
\end{pmatrix}
=
\begin{pmatrix}
-1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 2
\end{pmatrix}
$$

$P^{-1} T_1 P$ is diagonal with eigenvalues on the main diagonal!


## $T_2$

**1.**

To find eigenvalues solve

$$
\det
\begin{pmatrix}
4-\lambda & 0 & 1 \\
-2 & 1-\lambda & 0 \\
-2 & 0 & 1-\lambda
\end{pmatrix}
=
$$

(expanding along the top row)

$$
=(4-\lambda)(1-\lambda)^1 + 2(1-\lambda) = \\
(1-\lambda)(\lambda^2-5\lambda+6) = \\
(1-\lambda)(\lambda-2)(\lambda-3)
$$

Therefore the eigenvalues are $\lambda_1=1$, $\lambda_2=2$ and $\lambda_3=3$

**2.**

To find eigenvectors plug the eigenvalues one by one to $T_2-\lambda I$ and investigate the implications of the resulting system of equations. We should expect to find *multiple* eigenvectors for each eigenvalue, and therefore are looking for a formula rather than a usual answer.

$$
T_2 - \lambda_1 I=0 \iff
\begin{pmatrix}
3 & 0 & 1 \\
-2 & 0 & 0 \\
-2 & 0 & 0
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}
=
\begin{pmatrix}
0 \\ 0 \\ 0
\end{pmatrix}
$$

Doing Gaussian-Jordan elimination we have

$$
\left(\begin{array}{ccc|c}
3 & 0 & 1 & 0 \\
-2 & 0 & 0 & 0 \\
-2 & 0 & 0 & 0
\end{array}\right)
\rightarrow
\left(\begin{array}{ccc|c}
1 & 0 & \frac{1}{3} & 0 \\
0 & 0 & \frac{2}{3} & 0 \\
0 & 0 & 0 & 0
\end{array}\right)
\rightarrow
$$

$$
\left(\begin{array}{ccc|c}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0
\end{array}\right)
\iff
\left\{
\begin{array}{l}
x = 0 \\
y \text{ is free} \\
z = 0
\end{array}
\right.
$$

In other words, eigenvector $v_1$ is of the form $(0,p,0)$ where $p\in\mathbb{R}$.
Let us this time not impose the normalization and take $v_1 = (0,1,0)$ as the first eigenvector.



$$
T_2 - \lambda_2 I=0 \iff
\begin{pmatrix}
2 & 0 & 1 \\
-2 & -1 & 0 \\
-2 & 0 & -1
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}
=
\begin{pmatrix}
0 \\ 0 \\ 0
\end{pmatrix}
$$

$$
\left(\begin{array}{ccc|c}
2 & 0 & 1 & 0 \\
-2 & -1 & 0 & 0 \\
-2 & 0 & -1 & 0
\end{array}\right)
\rightarrow
\left(\begin{array}{ccc|c}
1 & 0 & \frac{1}{2} & 0 \\
0 & -1 & 1 & 0 \\
0 & 0 & 0 & 0
\end{array}\right)
\rightarrow
$$

$$
\left(\begin{array}{ccc|c}
1 & 0 & \frac{1}{2} & 0 \\
0 & 1 & -1 & 0 \\
0 & 0 & 0 & 0
\end{array}\right)
\iff
\left\{
\begin{array}{l}
x = -\frac{1}{2} z \\
y =z \\
z \text{ is free}
\end{array}
\right.
$$

In other words, eigenvector $v_2$ is of the form $(-\frac{1}{2}p,p,p)$ where $p\in\mathbb{R}$.
Again, let us not impose the normalization and take $v_2 = (-1,2,2)$ as the second eigenvector.


$$
T_2 - \lambda_3 I=0 \iff
\begin{pmatrix}
1 & 0 & 1 \\
-2 & -2 & 0 \\
-2 & 0 & -2
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}
=
\begin{pmatrix}
0 \\ 0 \\ 0
\end{pmatrix}
$$

$$
\left(\begin{array}{ccc|c}
1 & 0 & 1 & 0 \\
-2 & -2 & 0 & 0 \\
-2 & 0 & -2 & 0
\end{array}\right)
\rightarrow
\left(\begin{array}{ccc|c}
1 & 0 & 1 & 0 \\
0 & -2 & 2 & 0 \\
0 & 0 & 0 & 0
\end{array}\right)
\rightarrow
$$

$$
\left(\begin{array}{ccc|c}
1 & 0 & 1 & 0 \\
0 & 1 & -1 & 0 \\
0 & 0 & 0 & 0
\end{array}\right)
\iff
\left\{
\begin{array}{l}
x = -z \\
y =z \\
z \text{ is free}
\end{array}
\right.
$$

In other words, eigenvector $v_3$ is of the form $ (-p,p,p)$ where $p\in\mathbb{R}$.
Let us take $v_3 = (-\frac{1}{2},1,1)$ as the second eigenvector.


**3.**

We have chosen the eigenvectors in a way that they are not normalized, and let's try to see if this approach results in a diagonal matrix $T'$ in the new basis anyway.

$$
\{v_1, v_2, v_3\} =
\left\{
\begin{pmatrix}
0 \\ 1 \\ 0
\end{pmatrix},
\begin{pmatrix}
-1 \\ 2 \\ 2
\end{pmatrix},
\begin{pmatrix}
-1 \\ 1 \\ 1
\end{pmatrix}
\right\}
$$

forms a basis in $\mathbb{R}^3$

**4.**

The transformation matrix is a matrix with columns formed from the vectors of the new basis expressed in coordinates (``the language'') of the old basis.

$$
P = 
\begin{pmatrix}
0 & -1 & -1 \\ 
1 & 2 & 1 \\ 
0 & 2 & 1
\end{pmatrix}
$$


**5.**

Again, the matrix $T$ and the matrix $T'$ in the new basis are related as

$$
T = P T' P^{-1} \quad \iff \quad T' = P^{-1} T P
$$

We find $P^{-1}$ in the same way by going Gaussian-Jordan elimination


$$
\left(\begin{array}{ccc|ccc}
0 & -1 & -1 &
1 & 0 & 0 \\
1 & 2 & 1 &
0 & 1 & 0 \\
0 & 2 & 1 &
0 & 0 & 1
\end{array}\right)
\longrightarrow
$$

$$
\left(\begin{array}{ccc|ccc}
1 & 2 & 1 &
0 & 1 & 0 \\
0 & 1 & 1 &
-1 & 0 & 0 \\
0 & 0 & -1 &
2 & 0 & 1
\end{array}\right)
\longrightarrow
$$

$$
\left(\begin{array}{ccc|ccc}
1 & 0 & -1 &
2 & 1 & 0 \\
0 & 1 & 1 &
-1 & 0 & 0 \\
0 & 0 & 1 &
-2 & 0 & -1
\end{array}\right)
\longrightarrow
$$

$$
\left(\begin{array}{ccc|ccc}
1 & 0 & 0 &
0 & 1 & -1 \\
0 & 1 & 0 &
1 & 0 & 1 \\
0 & 0 & 1 &
-2 & 0 & -1
\end{array}\right)
\longrightarrow
$$

Therefore, the inverse of the $P$ matrix is given by

$$
P^{-1} =
\begin{pmatrix}
0 & 1 & -1 \\
1 & 0 & 1 \\
-2 & 0 & -1
\end{pmatrix}
$$

**Additional exercise:** verify that $PP^{-1} = I$.

Now we can compute $P^{-1} T_2 P$:

$$
\begin{pmatrix}
0 & 1 & -1 \\
1 & 0 & 1 \\
-2 & 0 & -1
\end{pmatrix}
\begin{pmatrix}
4 & 0 & 1 \\
-2 & 1 & 0 \\
-2 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
0 & -1 & -1 \\ 
1 & 2 & 1 \\ 
0 & 2 & 1
\end{pmatrix}
=
$$

$$
\begin{pmatrix}
0 & 1 & -1 \\
2 & 0 & 2 \\
-6 & 0 & -3
\end{pmatrix}
\begin{pmatrix}
0 & -1 & -1 \\ 
1 & 2 & 1 \\ 
0 & 2 & 1
\end{pmatrix}
=
\begin{pmatrix}
1 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 3
\end{pmatrix}
$$

$P^{-1} T_2 P$ is diagonal with eigenvalues on the main diagonal!



## $T_3$

**1.**

To find eigenvalues solve

$$
\det
\begin{pmatrix}
5-\lambda & 0 & 1 \\
1 & 1-\lambda & 0 \\
-7 & 1 & -\lambda
\end{pmatrix}
=
(5-\lambda)(1-\lambda)(-\lambda)+1+7(1-\lambda) = \\
=(1-\lambda)(\lambda^2-5\lambda+7) + 1 =
\lambda^2-5\lambda+7 - \lambda^3+5\lambda^2-7\lambda +1 =\\
=-\lambda^3+6\lambda^2-12\lambda+8 = -(\lambda-2)^3
$$

Therefore the only eigenvalue is $\lambda=2$, this root is repeated three times.

**2.**

To find eigenvectors plug the eigenvalues one by one to $T_3-\lambda I$ and investigate the implications of the resulting system of equations. 

Because the eigenvalue is repeated, we should expect difficulties finding enough eigenvectors to form a new basis --- we need at least three linearly independent eigenvectors in $\mathbb{R}^3$!

$$
T_3 - \lambda I=0 \iff
\begin{pmatrix}
3 & 0 & 1 \\
1 & -1 & 0 \\
-7 & 1 & -2
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}
=
\begin{pmatrix}
0 \\ 0 \\ 0
\end{pmatrix}
$$

Doing Gaussian-Jordan elimination we have

$$
\left(\begin{array}{ccc|c}
3 & 0 & 1 & 0 \\
1 & -1 & 0 & 0 \\
-7 & 1 & -2 & 0
\end{array}\right)
\rightarrow
\left(\begin{array}{ccc|c}
1 & 0 & \frac{1}{3} & 0 \\
0 & -1 & -\frac{1}{3} & 0 \\
0 & 1 & \frac{1}{3} & 0
\end{array}\right)
\rightarrow
$$

$$
\left(\begin{array}{ccc|c}
1 & 0 & \frac{1}{3} & 0 \\
0 & 1 & \frac{1}{3} & 0 \\
0 & 0 & 0 & 0
\end{array}\right)
\iff
\left\{
\begin{array}{l}
x = -\frac{1}{3}z \\
y = - \frac{1}{3}z \\
z = \text{ is free}
\end{array}
\right.
$$

In other words, all eigenvectors have the form $(-\frac{1}{3}p,-\frac{1}{3}p,p)$ where $p\in\mathbb{R}$.

In order to form a basis from eigenvectors, we need three linearly independent of them, which is *impossible in this case* because there is only one free parameter!
In other words, all eigenvectors we can come up with will lie within the same line (one degree of freedom), and thus we can not even have two linearly inpendent eigenvectors, let alone three.

**3.** - **5.**

$T_3$ is not diagonalizable through eigendecomposition.



## $T_4$

**1.**

First of all, note that $T_4$ is symmetric with real entries, therefore eigenvalue decomposition definitely be possible -- unlike the last case.
To find eigenvalues solve

$$
\det
\begin{pmatrix}
2-\lambda & 0 & 0 \\
0 & 3-\lambda & -1 \\
0 & -1 & 3-\lambda
\end{pmatrix}
=
(2-\lambda)\big((3-\lambda)^2-1\big) = \\
=(2-\lambda)(9-6\lambda+\lambda^2-1) = 
(2-\lambda)(\lambda^2-6\lambda+8) = \\
=(2-\lambda)(\lambda -2)(\lambda-4) =
-(\lambda-2)^2(\lambda-4)
$$

Therefore eigenvalues are $\lambda_1=4$ and a repeated one $\lambda_{2,3}=2$.
Yet, again, we should be able to diagonalize $T_4$ because it is symmetric!

**2.**

To find eigenvectors plug the eigenvalues one by one to $T_4-\lambda I$ and investigate the implications of the resulting system of equations. 

Because the eigenvalue is repeated, we should expect to do more work than usual, but the basis using eigenvectors should still be possible to find.

$$
T_4 - \lambda_1 I=0 \iff
\begin{pmatrix}
-2 & 0 & 0 \\
0 & -1 & -1 \\
0 & -1 & -1
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}
=
\begin{pmatrix}
0 \\ 0 \\ 0
\end{pmatrix}
$$

$$
\left(\begin{array}{ccc|c}
-2 & 0 & 0 & 0 \\
0 & -1 & -1 & 0 \\
0 & -1 & -1 & 0
\end{array}\right)
\rightarrow
\left(\begin{array}{ccc|c}
1 & 0 & 0 & 0 \\
0 & 1 & 1 & 0 \\
0 & 0 & 0 & 0
\end{array}\right)
\rightarrow
\iff
\left\{
\begin{array}{l}
x = 0 \\
y = -z \\
z = \text{ is free}
\end{array}
\right.
$$

In other words, the eigenvectors corresponding to $\lambda_1$ have the form $(0,-p,p)$ where $p\in\mathbb{R}$.

$$
T_4 - \lambda_{2,3} I=0 \iff
\begin{pmatrix}
0 & 0 & 0 \\
0 & 1 & -1 \\
0 & -1 & 1
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}
=
\begin{pmatrix}
0 \\ 0 \\ 0
\end{pmatrix}
$$

It is clear immediately, that the only restriction placed by this linear system of equations is that $y=z$.  In other words, there are no restrictions on two of the three variables, and we can express the eigenvectors corresponding to $\lambda_{2,3}$ as $(p,q,q)$ where $p, q\in\mathbb{R}$ are parameters.

**3.**

In order to form a basis from eigenvectors, we need three linearly independent of them. Fortunately, there is enough degrees of freedom in the parameters (one from the first eigenvalue and two from the second) to have three linearly independent eigenvectors. For example, $(0,-1,1)$, $(1,0,0)$ and $(0,1,1)$

**4.**

The transformation matrix is a matrix with columns formed from the vectors of the new basis expressed in coordinates (``the language'') of the old basis.

$$
P = 
\begin{pmatrix}
0 & 1 & 0 \\ 
-1 & 0 & 1 \\ 
1 & 0 & 1
\end{pmatrix}
$$


**5.**

Again, the matrix $T$ and the matrix $T'$ in the new basis are related as

$$
T = P T' P^{-1} \quad \iff \quad T' = P^{-1} T P
$$

We find $P^{-1}$ in the same way by going Gaussian-Jordan elimination

$$
\left(\begin{array}{ccc|ccc}
0 & 1 & 0 &
1 & 0 & 0 \\
-1 & 0 & 1 &
0 & 1 & 0 \\
1 & 0 & 1 &
0 & 0 & 1
\end{array}\right)
\longrightarrow
$$

$$
\left(\begin{array}{ccc|ccc}
1 & 0 & 1 &
0 & 0 & 1 \\
0 & 1 & 0 &
1 & 0 & 0 \\
0 & 0 & 2 &
0 & 1 & 1
\end{array}\right)
\longrightarrow
$$

$$
\left(\begin{array}{ccc|ccc}
1 & 0 & 1 &
0 & 0 & 1 \\
0 & 1 & 0 &
1 & 0 & 0 \\
0 & 0 & 1 &
0 & \frac{1}{2} & \frac{1}{2}
\end{array}\right)
\longrightarrow
$$

$$
\left(\begin{array}{ccc|ccc}
1 & 0 & 0 &
0 & -\frac{1}{2} & \frac{1}{2} \\
0 & 1 & 0 &
1 & 0 & 0 \\
0 & 0 & 1 &
0 & \frac{1}{2} & \frac{1}{2}
\end{array}\right)
\longrightarrow
$$

$$
P^{-1} = 
\begin{pmatrix}
0 & -\frac{1}{2} & \frac{1}{2} \\
1 & 0 & 0 \\
0 & \frac{1}{2} & \frac{1}{2}
\end{pmatrix}
$$


**Additional exercise:** verify that $PP^{-1} = I$.

Now we can compute $P^{-1} T_2 P$:

$$
\begin{pmatrix}
0 & -\frac{1}{2} & \frac{1}{2} \\
1 & 0 & 0 \\
0 & \frac{1}{2} & \frac{1}{2}
\end{pmatrix}
\begin{pmatrix}
2 & 0 & 0 \\
0 & 3 & -1 \\
0 & -1 & 3
\end{pmatrix}
\begin{pmatrix}
0 & 1 & 0 \\ 
-1 & 0 & 1 \\ 
1 & 0 & 1
\end{pmatrix}
=
$$

$$
\begin{pmatrix}
0 & -\frac{1}{2} & \frac{1}{2} \\
1 & 0 & 0 \\
0 & \frac{1}{2} & \frac{1}{2}
\end{pmatrix}
\begin{pmatrix}
0 & 2 & 0 \\
-4 & 0 & 2 \\
4 & 0 & 2
\end{pmatrix}
=
\begin{pmatrix}
4 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 2
\end{pmatrix}
$$

We see again that $P^{-1} T_4 P$ is diagonal with eigenvalues on the main diagonal, even though one of the eigenvalues is repeated twice.

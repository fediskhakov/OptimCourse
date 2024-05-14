## $A_1$

Matrix $A_1$ is not symmetric, we consider its symmetric part

$$
\frac{1}{2}(A_1+A_1^{T}) = 
\begin{pmatrix}
5 & \tfrac{1}{2} & -3 \\
\tfrac{1}{2} & 1 & \tfrac{1}{2} \\
-3 & \tfrac{1}{2} & 0
\end{pmatrix}
$$

Applying the Silvester's criterion, first we compute the leading principle minors:

$$
M_1 = \det(5) >0
$$

$$
M_2 = \det
\begin{pmatrix}
5 & \tfrac{1}{2} \\
\tfrac{1}{2} & 1
\end{pmatrix}
= 5 - \tfrac{1}{4} >0
$$

$$
M_2 = \det
\begin{pmatrix}
5 & \tfrac{1}{2} & -3 \\
\tfrac{1}{2} & 1 & \tfrac{1}{2} \\
-3 & \tfrac{1}{2} & 0
\end{pmatrix}
= 0-\tfrac{3}{4}-\tfrac{3}{4}-9-\tfrac{5}{4}
<0
$$

This pattern does not fit neither definite nor semi-definite patters of the Silvester's criterion, therefore $A_1$ is indefinite.

You can also [verify numerically](https://www.wolframalpha.com/input?i2d=true&i=%7B%7B1%2C0.5%2C-3%7D%2C%7B0.5%2C1%2C0.5%7D%2C%7B-3%2C0.5%2C0%7D%7D) that eigenvalues have varying signs.

## $A_2$

Matrix $A_2$ is not symmetric, we consider its symmetric part

$$
\frac{1}{2}(A_2+A_2^{T}) = 
\begin{pmatrix}
5 & -1 & \tfrac{3}{2} \\
-1 & 4 & -\tfrac{1}{2} \\
\tfrac{3}{2} & -\tfrac{1}{2} & 3
\end{pmatrix}
$$

Applying the Silvester's criterion, first we compute the leading principle minors:

$$
M_1 = \det(5) >0
$$

$$
M_2 = \det
\begin{pmatrix}
5 & -1 \\
-1 & 4
\end{pmatrix}
= 20 - 1 >0
$$

$$
M_2 = \det
\begin{pmatrix}
5 & -1 & \tfrac{3}{2} \\
-1 & 4 & -\tfrac{1}{2} \\
\tfrac{3}{2} & -\tfrac{1}{2} & 3
\end{pmatrix}
= 60 + \tfrac{3}{4} + \tfrac{3}{4} - 9 - 3 - \tfrac{5}{4}
>0
$$

Hence, by Silvester's criterion $A_2$ is positive definite.

You can also [verify numerically](https://www.wolframalpha.com/input?i2d=true&i=%7B%7B1%2C-1%2C1.5%7D%2C%7B-1%2C4%2C-0.5%7D%2C%7B1.5%2C-0.5%2C3%7D%7D) that all eigenvalues are strictly positive.

## $A_3$

Matrix $A_3$ is not symmetric, we consider its symmetric part

$$
\frac{1}{2}(A_3+A_3^{T}) = 
\begin{pmatrix}
1 & 1 & \tfrac{13}{2} \\
1 & -5 & 0 \\
\tfrac{13}{2} & 0 & 2
\end{pmatrix}
$$

Applying the Silvester's criterion, first we compute the leading principle minors:

$$
M_1 = \det(1) >0
$$

$$
M_2 = \det
\begin{pmatrix}
1 & 1 \\
1 & -5
\end{pmatrix}
= -5 - 1 < 0
$$

This pattern does not fit neither definite nor semi-definite patters of the Silvester's criterion, therefore $A_3$ is indefinite.

You can also [verify numerically](https://www.wolframalpha.com/input?i2d=true&i=%7B%7B1%2C1%2C6.5%7D%2C%7B1%2C-5%2C0%7D%2C%7B6.5%2C0%2C2%7D%7D) that eigenvalues have varying signs.


## $A_4$

Matrix $A_4$ is symmetric, let us assess definiteness after computing eigenvalues

$$
\det
\begin{pmatrix}
2-\lambda & 2 & 2 \\
2 & 2-\lambda & 2 \\
2 & 2 & 2-\lambda
\end{pmatrix}
=
\det
\begin{pmatrix}
-\lambda & 2 & 2 \\
\lambda & 2-\lambda & 2 \\
0 & 2 & 2-\lambda
\end{pmatrix}
=
$$

(subtracting second column from the first, see the [section on the properties of the determinants](https://optim.iskh.me/08.determinants_eigenpairs.html#properties-of-determinants))

$$
=
-\lambda \big( (2-\lambda)^2 -4 \big)
-\lambda(4 -2\lambda -4)
=
$$

$$
=
-\lambda \big(\lambda^2 - 4\lambda + 4-4 -2\lambda \big)
=
-\lambda^2 (\lambda - 6)
$$

Hence, the eigenvalues are $\{0,6\}$, therefore $A_4$ is positive semi-definite.

Silvester's criterion agrees with this conclusion:

- all principle minors of order 1 are positive, $\det(2)>0$
- all other principle minors are zero

This is consistent with the positive semi-definite definiteness pattern of the Silvester's criterion.

## $A_5$

Matrix $A_5$ is symmetric, let us again assess definiteness after computing eigenvalues

$$
\det
\begin{pmatrix}
-4-\lambda & 2 & -6 \\
2 & -1-\lambda & 3 \\
-6 & 3 & -9-\lambda
\end{pmatrix}
=
$$

$$
=
-(\lambda+4)(\lambda+1)(\lambda+9) -36 -36 +\\
+ 36(\lambda+1) + 4(\lambda+9) +9(\lambda+4)
=\\
= -\lambda^3 -14\lambda^2 - 49\lambda - 36 -72 +\\
+36\lambda + 36 + 4\lambda + 36 + 9\lambda + 36
=\\
= -\lambda^3 -14\lambda^2 = 
-\lambda^2(\lambda + 14)
$$

Eigenvalues are $\{0,-14\}$, hence the $A_5$ is negative semi-definite.

Silvester's criterion again agrees with this conclusion:

- all principle minors of order 1 are negative: 

$$
\det(-4)<0\\
\det(-1)<0\\
\det(-9)<0
$$

- all other principle minors are zero:

$$
\det
\begin{pmatrix}
-4 & 2 \\
2 & -1
\end{pmatrix}
=0\\
\det
\begin{pmatrix}
-4 & -6 \\
-6 & -9
\end{pmatrix}
=0\\
\det
\begin{pmatrix}
-1 & 3 \\
3 & -9
\end{pmatrix}
=0\\
\det
\begin{pmatrix}
-4 & 2 & -6 \\
2 & -1 & 3 \\
-6 & 3 & -9
\end{pmatrix}
=-36 \cdot 3 +36 \cdot 3 =0
$$

This is consistent with the negative semi-definite definiteness pattern of the Silvester's criterion.





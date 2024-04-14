A possible answer:

Represent the quadratic form as a dot product of two functions
$f(x) = x' A x = h(x) \cdot g(x)$, where
$h(x) = x$ and $g(x) = A x$.
Then $Dh(x) = I$ (identity matrix) and $Dg(x) = A$. 

The last Jacobian can be easity derived by representing matrix multiplication as a linear combination of columns. Differentiating with respect to each element of $x$ then yields a Jacobian composed of columns of matrix $A$, therefore equal to it.

$$
g(x) = A x = 
\left(
\begin{array}{ccc}
a_{11} & \cdots & a_{1N} \\
\vdots & \ddots & \vdots \\
a_{N1} & \cdots & a_{NN}
\end{array}
\right)
\left(
\begin{array}{c}
x_1 \\ \vdots \\ x_N
\end{array}
\right)
=
\left(
\begin{array}{c}
a_{11} \\ \vdots \\ a_{N1}
\end{array}
\right)
x_1 +
\cdots
\left(
\begin{array}{c}
a_{1N} \\ \vdots \\ a_{NN}
\end{array}
\right)
x_N
$$


Applying the dot product rule of differentiation we have

$$
D(h \cdot g)(x) = [h(x)]^T  Dg(x) + [g(x)]^T  Dh(x) = \\
= x^T A + [Ax]^T  I = x^T A + x^T  A = 2 x^T  A = 2 [A x]^T 
$$

The last transformation is transpose of a product + utilizing symmetry of $A$.

The final answer is the $1 \times N$ matrix (row vector) 

$$
Df(x) =  f(x) = 2 x^T  A = 2 [A x]^T
$$

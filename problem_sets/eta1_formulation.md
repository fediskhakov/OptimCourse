Consider an $(n \times n)$ **Vandermonde matrix** [this one can be named 🙂] of the form

$$
V =
\begin{bmatrix}
1 & 1 & \cdots & 1 \\
x_1 & x_2 & \cdots & x_n \\
x_1^2 & x_2^2 & \cdots & x_n^2 \\
\vdots & \vdots & \ddots & \vdots \\
x_1^{n-1} & x_2^{n-1} & \cdots & x_n^{n-1}
\end{bmatrix}
$$

Show that the determinant of $V$ is given by

$$
\det(V) = \Pi_{j<i \leqslant n}(x_i-x_j)
$$

for the cases $n=2$ and $n=3$

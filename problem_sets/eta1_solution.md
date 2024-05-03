Using the fact that the determinant is invariant to [Gaussian elementary row operations](https://en.wikipedia.org/wiki/Gaussian_elimination) we perform the following derivation:

$$
\det
\begin{pmatrix}
1 & 1 & \cdots & 1 \\
x_1 & x_2 & \cdots & x_n \\
x_1^2 & x_2^2 & \cdots & x_n^2 \\
\vdots & \vdots & \ddots & \vdots \\
x_1^{n-1} & x_2^{n-1} & \cdots & x_n^{n-1}
\end{pmatrix}
=
\det
\begin{pmatrix}
1 & 0 & \cdots & 0 \\
x_1 & x_2-x_1 & \cdots & x_n-x_1 \\
x_1^2 & x_2^2-x_1^2 & \cdots & x_n^2-x_1^2 \\
\vdots & \vdots & \ddots & \vdots \\
x_1^{n-1} & x_2^{n-1}-x_1^{n-1} & \cdots & x_n^{n-1}-x_1^{n-1}
\end{pmatrix}
=
$$

(expand along the first row)

$$
=
\det
\begin{pmatrix}
x_2-x_1 & x_3-x_1 & \cdots & x_n-x_1 \\
x_2^2-x_1^2 & x_3^2-x_1^2 & \cdots & x_n^2-x_1^2 \\
\vdots & \vdots & \ddots & \vdots \\
x_2^{n-1}-x_1^{n-1} & x_3^{n-1}-x_1^{n-1} & \cdots & x_n^{n-1}-x_1^{n-1}
\end{pmatrix}
=
$$

(take out common factor from each row)

$$
=
(x_2-x_1)(x_3-x_1)\dots(x_n-x_1)
\det
\begin{pmatrix}
1 & 1 & \cdots & 1 \\
\frac{x_2^2-x_1^2}{x_2-x_1} & \frac{x_3^2-x_1^2}{x_3-x_1} & \cdots & \frac{x_n^2-x_1^2}{x_n-x_1} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{x_2^{n-1}-x_1^{n-1}}{x_2-x_1} & \frac{x_3^{n-1}-x_1^{n-1}}{x_3-x_1} & \cdots & \frac{x_n^{n-1}-x_1^{n-1}}{x_n-x_1} \\
\end{pmatrix}
$$

It is not hard to show (by [long division of polynomials](https://en.wikipedia.org/wiki/Polynomial_long_division) and mathematical induction) that

$$
\frac{a^{k}-b^{k}}{a-b}
=a^{k-1}+a^{k-2}b + \dots + ab^{k-2} + b^{k-1}
=\sum_{i=1}^{k} a^{k-i}b^{i-1}
$$

Continuing the derivation:

$$
=
\prod_{i=2}^n (x_i-x_1)
\det
\begin{pmatrix}
1 & \cdots & 1 \\
x_2+x_1 & \cdots & x_n+x_1 \\
\vdots & \ddots & \vdots \\
\sum_{i=1}^{n-1} x_2^{n-1-i}x_1^{i-1} &
\cdots &
\sum_{i=1}^{n-1} x_n^{n-1-i}x_1^{i-1}
\end{pmatrix}
=
$$

We can then repeat the same procedure:
- subtract the first row from all other
- notice regularities in the polynomials
- expand the determinant along the first row
- take out common factors from each row

It is then obvious how to prove the main formula by mathematical induction.

**$n=2$**

$$
\det
\begin{pmatrix}
1 & 1 \\
x & y
\end{pmatrix}
=y-x
$$


**$n=3$**

$$
\det
\begin{pmatrix}
1 & 1 & 1 \\
x & y & z \\
x^2 & y^2 & z^2
\end{pmatrix}
=
\det
\begin{pmatrix}
1 & 0 & 0 \\
x & y-x & z-x \\
x^2 & y^2-x^2 & z^2-x^2
\end{pmatrix}
=
$$

$$
=
\det
\begin{pmatrix}
y-x & z-x \\
y^2-x^2 & z^2-x^2
\end{pmatrix}
=
$$

$$
=
(y-x)(z-x)
\det
\begin{pmatrix}
1 & 1 \\
x+y & x+z
\end{pmatrix}
=
$$

$$
=
(y-x)(z-x)(x+z-x-y)=(y-x)(z-x)(z-y)
$$

**$n=4$**

Follow the same scheme, using

- $x^2-y^2=(x-y)(x+y)$
- $x^3-y^3=(x-y)(x^2+xy+y^2)$

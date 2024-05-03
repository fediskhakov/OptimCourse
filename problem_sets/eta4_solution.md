First, note that completing the square with many variables is not too hard:

$$
\begin{array}{l}
(a+b)^2 = a^2 + 2ab + b^2 \\
(a+b+c)^2 = a^2 + 2ab + b^2 + 2c(a+b) + c^2 \\
(a+b+c+d)^2 = a^2 + b^2 + c^2 + d^2 + 2ab + 2ac + 2ad + 2bc + 2bd + 2cd\\
\left(\sum_{i=1}^N x_i\right)^2 = \sum_{i=1}^N x_i^2 + 2\sum_{i=1}^N\sum_{j=i+1}^N x_i x_j
\end{array}
$$

(It's a quadratic form with the matrix which elements are all 1!)

Now, let's try to complete the square for the given quadratic form:

$$
\begin{array}{rl}
Q(x) =& 
x_1^2 + x_2^2 + x_3^2 + 4x_4^2 + 2x_1x_2 - 2x_1x_3 + 4x_1x_4 + 6x_2x_4 - 4x_3x_4
=\\=& 
\big[x^2_1 + 2x_1x_2 - 2x_1x_3 + 4x_1x_4 \big] + x_2^2 + x_3^2 + 4x_4^2 + 6x_2x_4 - 4x_3x_4
=\\=& 
\big(x_1 + x_2 - x_3 + 2x_4 \big)^2 + 2x_2x_3 -4x_2x_4 + 4x_3x_4 + 6x_2x_4 - 4x_3x_4
=\\=&
\big(x_1 + x_2 - x_3 + 2x_4 \big)^2 +2x_2x_3 + 2x_2x_4
\end{array}
$$

Introduce the first change of variables:

$$
\begin{array}{l}
y_1 = x_1 + x_2 - x_3 + 2x_4 \\
y_i = x_i, i \in \{2,3,4\}
\end{array}
\quad \Rightarrow \quad
y =
\begin{pmatrix}
1 & 1 & -1 & 2 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
x
$$

After the change of variables from $x$ to $y$ the quadratic form becomes

$$
\begin{array}{rl}
Q(y) =& 
y_1^2 +2y_2y_3 + 2y_2y_4
=\\=& 
y_1^2 + [y^2_2 + y^2_3 + y^2_4 + 2y_2y_3 + 2y_2y_4 + 2y_3y_4 ] - y^2_2 - y^2_3 - y^2_4 - 2y_3y_4
=\\=&
y_1^2 + (y_2 + y_3 + y_4)^2 - y^2_2 - y^2_3 - y^2_4 - 2y_3y_4
=\\=&
y_1^2 + (y_2 + y_3 + y_4)^2 - y^2_2 - [y^2_3 + y^2_4 + 2y_3y_4]
=\\=&
y_1^2 + (y_2 + y_3 + y_4)^2 - y^2_2 - (y_3 + y_4)^2
\end{array}
$$

Introduce the second change of variables:

$$
\begin{array}{l}
t_1 = y_1 \\
t_2 = y_2 \\
t_3 = y_2 + y_3 + y_4 \\
t_4 = y_3 + y_4
\end{array}
\quad \Rightarrow \quad
t =
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 1 & 1 & 1 \\
0 & 0 & 1 & 1
\end{pmatrix}
y
$$

After the change of variables from $x$ to $y$ to $t$ the quadratic takes the canonical form

$$
Q(t) =
t_1^2 - t_2^2 + t_3^2  - t_4^2
$$

The complete change of variables from $x$ to $t$ can be thought of as a composite linear map

$$
t =
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 1 & 1 & 1 \\
0 & 0 & 1 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 1 & -1 & 2 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
x
=
\begin{pmatrix}
1 & 1 & -1 & 2 \\
0 & 1 & 0 & 0 \\
0 & 1 & 1 & 1 \\
0 & 0 & 1 & 1
\end{pmatrix}
x
$$

Quick check reveals that the determinant of this matrix is zero, and therefore, its inverse does not exists, but we can still use it to transform the variables to express the original quadratic form in the canonical form.


In matrix notation, the original quadratic form is written as

$$
Q(x) = x^T A x, \quad 
A =
\begin{pmatrix}
1 & 1 & -1 & 2 \\
1 & 1 & 0 & 3 \\
-1 & 0 & 1 & -2 \\
2 & 3 & -2 & 4
\end{pmatrix}
$$

In the diagonalized (canonical) form, it is

$$
Q(t) 
= t^T T^T 
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & -1
\end{pmatrix}
 T t
$$


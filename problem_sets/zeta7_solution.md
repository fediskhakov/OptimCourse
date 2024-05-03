The direct way to answer the question is to check whether the given vector is a linear combination of the other three. If this is the case, then by definition it is in the required span. To establish this, we have to solve a system of linear equations of the form

$$
\alpha_1
\begin{pmatrix}
-4 \\
0 \\
0
\end{pmatrix}
+
\alpha_2
\begin{pmatrix}
1 \\
2 \\
0
\end{pmatrix}
+
\alpha_3
\begin{pmatrix}
0 \\
1 \\
-1
\end{pmatrix}
=
\begin{pmatrix}
-3.98 \\
11.73 \\
-4.32
\end{pmatrix}
$$

But there is an easier way to do this!

We know that any linearly
independent set of 3 vectors in $\mathbb{R}^3$ will span $\mathbb{R}^3$. Since ${\bf z} \in \mathbb{R}^3$, this will include ${\bf z}$. So all we need to do is
show that $X$ is linearly independent. To this end, take any scalars
$\alpha_1, \alpha_2, \alpha_3$ with 
%
$$
\alpha_1
\begin{pmatrix}
-4 \\
0 \\
0
\end{pmatrix}
+
\alpha_2
\begin{pmatrix}
1 \\
2 \\
0
\end{pmatrix}
+
\alpha_3
\begin{pmatrix}
0 \\
1 \\
-1
\end{pmatrix}
=
{\bf 0}
:=
\begin{pmatrix}
0 \\
0 \\
0
\end{pmatrix}
$$
%
Write as a linear system of 3 equations and show that the only solution is $\alpha_1=\alpha_2=\alpha_3=0$.

In this case the set would be linearly independent.

Clearly, the second system is much easier to solve than the first.
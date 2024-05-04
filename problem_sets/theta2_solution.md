**Question F.3**

**1.** 

The optimization problem is:

$$
\max \limits_{\beta \in \mathbb{R}^2} \sum\limits_{i=1}^{n} l_i(\beta, x_1, x_2, z_i, y_i).
$$

- We can control $\beta = {[\beta_1, \beta_2]^{\prime}}$ (coefficients to be estimated).
- We treat $x_1, x_2, {(z_i, y_i)}_{i=1}^n$ as 
parameters (data).

**2.** 

We can try to apply Weierstrass theorem.

- The objective function is continuous. 

- But the domain is not compact ($\mathbb{R}^2$
is closed but unbounded). 

**3.** 

Denote $D_{\beta} l_i$ as the Jacobian of 
$l_i$ with respect to $\beta$, $H_{\beta} l_i$ 
as the Hessian of $l_i$ with respect to $\beta$.

Notice that $l_i(\beta) = l_i\Big(p_i\big(u_i(\beta)\big)\Big)$, then by the chain rule:

$$
D_{\beta}l_i  =D_{p_i}l_i ~D_{u_i}p_i 
~D_{\beta}u_i.
$$

We calculate the three terms on the r.h.s. one by one:

$$
\begin{array}{ll}
D_{p_i} l_i &= \left[\begin{array}{cc} y_i/p_{i1} & (1-y_i)/p_{i2}\\ \end{array}\right], \\
D_{u_i} p_i &= \left[\begin{array}{cc} 
p_{i1}p_{i2} & -p_{i1} p_{i2}\\ 
-p_{i1} p_{i2} & p_{i1}p_{i2}\\ 
\end{array}\right] 
=
p_{i1} p_{i2} \left[\begin{array}{cc} 
1 & -1\\ 
-1 & 1\\ 
\end{array}\right],
\\   
D_{\beta} u_i &= \left[\begin{array}{cc} 
x_1 & x_1 z_i\\ 
x_2 & x_2 z_i\\ 
\end{array}\right].
\end{array}
$$

Thus,

$$
\begin{array}{ll}
D_\beta l_i &= \left[\begin{array}{cc} y_i/p_{i1} & (1-y_i)/p_{i2}\\ \end{array}\right]
p_{i1} p_{i2}  \left[\begin{array}{cc} 
1 & -1\\ 
-1 & 1\\ 
\end{array}\right]
\left[\begin{array}{cc} 
x_1 & x_1 z_i\\ 
x_2 & x_2 z_i\\ 
\end{array}\right],\\
&= (x_1 -x_2) \cdot 
\left[\begin{array}{cc} 
y_i p_{i2} - (1-y_i)p_{i1}
& 
y_i p_{i2}z - (1-y_i)p_{i1} z\\ 
\end{array}\right].
\end{array}
$$

The Jacobian (gradient) of the MLE objective function is:

$$
D_\beta l = \sum\limits_{i=1}^{n}
D_\beta l_i = 
(x_1 -x_2) \cdot
\sum\limits_{i=1}^{n} 
  \left[\begin{array}{cc} 
    y_i p_{i2} - (1-y_i)p_{i1}
    & 
    y_i p_{i2}z - (1-y_i )p_{i1} z\\ 
    \end{array}\right]
$$

We set $h(\beta_i) \equiv (D_\beta l_i)^{\prime}$.
Then 
$h(\beta)= h\Big(p_i\big(u_i(\beta)\big)\Big)$ 
Thus, by applying the chain rule again,  Hessian of $l_i$ with respect to $\beta$ is:

$$
\begin{array}{ll}
H_\beta l_i &= D_{\beta} h(\beta)\\
&= D_{p_i} h(p_i) ~ D_{u_i} p_i ~ D_{\beta} u_i\\
&= (x_1 - x_2) 
\left[\begin{array}{cc}
-(1-y_i) & y_i \\ 
-(1-y_i)z_i & y_i z_i \\
\end{array}\right] 
p_{i1} p_{i2}
\left[\begin{array}{cc} 
1 & -1\\ 
-1 & 1\\ 
\end{array}\right]
\left[\begin{array}{cc} 
x_1 & x_1 z_i\\ 
x_2 & x_2 z_i\\ 
\end{array}\right] \\
& = 
(x_1 - x_2)^2
p_{i1} p_{i2} 
\left[\begin{array}{cc} 
-1 & -z_i\\ 
-z_i & -z_i^2\\ 
\end{array}\right]
\end{array}
$$

Thus, the Hessian of the MLE objective function is:

$$
\begin{array}{ll}
H_\beta l &= \sum\limits_{i=1}^{n} H_\beta l_i \\
&= (x_1 - x_2)^2 
\sum\limits_{i=1}^{n}
p_{i1} p_{i2} 
\left[\begin{array}{cc} 
x_1 & x_1 z_i\\ 
x_2 & x_2 z_i\\ 
\end{array}\right]\\ 
& = (x_1 - x_2)^2
\left[\begin{array}{cc}
- \sum\limits_{i=1}^{n} p_{i1} p_{i2} &
- \sum\limits_{i=1}^{n} p_{i1} p_{i2} z_i \\
- \sum\limits_{i=1}^{n} p_{i1} p_{i2} z_i &
- \sum\limits_{i=1}^{n} p_{i1} p_{i2} z_i^2 \\
\end{array}\right]
\end{array}
$$


**4.** 

Let us find the conditions under which the Hessian is negative definite.
Notice that $(x_1 - x_2)^2 > 0$ if and only if $x_1 \neq x_2$, and $p_{i1} p_{i2} > 0$ for all $i$. Thus, if $x_1 \neq x_2$, we only need to check the condition 
$det(H_\beta l) > 0$.
Notice that:

$$
\begin{array}{ll}
& \quad \quad \quad det(H_\beta l) > 0\\
&\iff 
(\sum_i p_{i1}p_{i2})(\sum_i p_{i1} p_{i2} z_i^2) - (\sum_i p_{i1} p_{i2} z_i)^2 > 0. \\
& \iff 
\sum_{i, j} p_{i1}p_{i2}p_{j1}p_{j2}z_j^2
- 
\sum_{i, j} p_{i1}p_{i2}p_{j1}p_{j2}z_i z_j > 0\\ 
& \iff 
\sum_{i > j} p_{i1}p_{i2}p_{j1}p_{j2}(z_i^2 + z_j^2) - \sum_{i > j} p_{i1}p_{i2}p_{j1}p_{j2}(2 z_i z_j) > 0\\
& \iff
\sum_{i > j} p_{i1}p_{i2}p_{j1}p_{j2}(z_i - z_j)^2 > 0.\\
& \iff 
z_i \neq z_j \text{ for some } i, j.
\end{array}
$$

Thus, we get a sufficient condition for the unique maximizer:
- $x_1 \neq x_2$,
- $z_i \neq z_j$ for some $i, j$.

It's easy to show this condition is also a necessary condition. Since if $x_1 = x_2$, 
$\beta_1$ has no impact on the likelihood function, and if $z_i = z_j$ for all $i, j$, 
we cannot distinguish $\beta_1$ from $\beta_2$ (this is called *strict multicollinearity* in econometrics).

Thus, the logit model has a unique ML estimator if and only if $x_1 \neq x_2$, and $z_i \neq z_j$ for some $i, j$.  

The intuition is that if the model can be estimated (*identifiable* in econometrics jargon), the two alternatives cannot be the same
($x_1 \neq x_2$), and at least two people in the data set should have different characteristics ($z_i \neq z_j$ for some $i, j$).

**5.**

If the Hessian $H_{\beta} l$ is negative      definite for all $\beta \in \mathbb{R}^2$, 
then $\det (H_{\beta} l)> 0$ always holds, we 
know there must be at least one solution to 
the first order conditions $D_{\beta} l = 0$ by 
the [Inverse function theorem](https://en.wikipedia.org/wiki/Inverse_function_theorem).

Moreover, if the Hessian is negative definite, 
then the MLE objective is strictly concave,
i.e., there is a unique maximizer of the log likelihood function, which is the unique solution to the first order conditions.

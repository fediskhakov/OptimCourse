---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Exercise set F

## Question F.3

This exercise takes you on a tour of a binary logit model and its properties.

Consider a model when a decision maker is making a choice between $J=2$ two alternatives, each of which has a scalar characteristic $x_j \in \mathbb{R}$, $j=1,2$. Econometrician observes data on these characteristics, the choice made by the decision maker $y_i \in \{0,1\}$ and an attribute of the decision maker, $z_i \in \mathbb{R}$. The positive value of $y_i$ denotes that the first alternative was chosen. The data is indexed with $i$ and has $N$ observations, i.e. $i \in \{1,\dots,N\}$.

To rationalize the data the econometrician assumes that the utility of each alternative is given by a scalar product of a vector of parameters $\beta \in \mathbb{R}^2$ and a vector function $h \colon \mathbb{R}^2 \to \mathbb{R}^2$ of alternative and decision maker attributes. Let 
%
$$
h \colon
\left(
\begin{array}{c}
x \\ z
\end{array}
\right)
\mapsto 
\left(
\begin{array}{l}
x \\ xz
\end{array}
\right)
$$

In line with the random utility model, the econometrician also assumes that the utility of each alternative contains the additively separable random component which has an appropriately centered type I extreme value distribution, such that the choice probabilities for the two alternatives are given by a vector function $p \colon \mathbb{R}^2 \to (0,1) \subset \mathbb{R}^2$
%
$$
p \colon
\left(
\begin{array}{c}
u_1 \\ u_2
\end{array}
\right)
\mapsto 
\left(
\begin{array}{c}
\frac{\exp(u_1)}{\exp(u_1) + \exp(u_2)}\\
\frac{\exp(u_2)}{\exp(u_1) + \exp(u_2)}
\end{array}
\right)
$$

In order to estimate the vector of parameters of the model $\beta$, the econometrician maximizes the likelihood of observing the data $D = \big(\{x_j\}_{j \in \{1,2\}},\{z_i,y_i\}_{i \in \{1,\dots,N\}}\big)$. The log-likelihood function $logL \colon \mathbb{R}^{2+J+2N} \to \mathbb{R}$ is given by
%
$$
logL(\beta,D) = \sum_{i=1}^N \ell_i(\beta,x_1,x_2,z_i,y_i),
$$
where the individual log-likelihood contribution is given by a scalar product function $\ell_i \colon \mathbb{R}^6 \to \mathbb{R}$
%
$$
\ell_i(\beta,x_1,x_2,z_i,y_i) = 
\left(
\begin{array}{l}
y_i \\
1-y_i
\end{array}
\right)
\cdot 
\log\left(p \left(
\begin{array}{l}
\beta \cdot h(x_1,z_i) \\
\beta \cdot h(x_2,z_i)
\end{array}
\right) \right)
$$
%

Assignments:

1. Write down the optimization problem the econometrician is solving. Explain the meaning of each part.
    - What are the variables the econometrician has control over in the estimation exercise? 
    - What variables should be treated as parameters of the optimization problem?

2. Elaborate on whether the solution can be guaranteed to exist.
    - What theorem should be applied?
    - What conditions of the theorem are met?
    - What conditions of the theorem are not met?

3. Derive the gradient and Hessian of the log-likelihood function. Make sure that all multiplied vectors and matrices are conformable.

4. Derive conditions under which the likelihood function has a unique maximizer (and thus the logit model has a unique maximum likelihood estimator).



```{admonition} Solution
:class: caution


See the last anwer in [this math stackexchange post](https://math.stackexchange.com/questions/307381/why-do-we-assume-that-a-matrix-in-quadratic-form-is-symmetric)

**Question F.2**

A possible answer:

Represent the quadratic form as a dot product of two functions
$f({\bf x}) = {\bf x}' A {\bf x} = h({\bf x}) \cdot g({\bf x})$, where
$h({\bf x}) = {\bf x}$ and $g({\bf x}) = A {\bf x}$.
Then $Dh({\bf x}) = I$ (identity matrix) and $Dg({\bf x}) = A$. 

The last Jacobian can be easity derived by representing matrix multiplication as a linear combination of columns. Differentiating with respect to each element of ${\bf x}$ then yields a Jacobian composed of columns of matrix $A$, therefore equal to it.
%
$$
g({\bf x}) = A {\bf x} = 
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
%

Applying the dot product rule of differentiation we have
%
$$
D(h \cdot g)({\bf x}) = [h({\bf x})]' Dg({\bf x}) + [g({\bf x})]' Dh({\bf x}) = \\
= {\bf x}'A + [A{\bf x}]' I = {\bf x}'A + {\bf x}' A = 2 {\bf x}' A = 2 [A {\bf x}]'
$$
% 
The last transformation is transpose of a product + utilizing symmetry of $A$.

The final answer is the $1 \times N$ matrix (row vector) $ Df({\bf x}) = \nabla f({\bf x}) = 2 {\bf x}' A = 2 [A {\bf x}]'$.

**Question F.3**

1. The optimization problem is:
%
$$
\max \limits_{\beta \in \mathbb{R}^2} \sum\limits_{i=1}^{n} l_i(\beta, x_1, x_2, z_i, y_i).
$$
%

- We can control $\beta = {[\beta_1, \beta_2]^{\prime}}$ (coefficients to be estimated).
- We treat $x_1, x_2, {(z_i, y_i)}_{i=1}^n$ as 
parameters (data).

2. We can try to apply Weierstrass theorem.

- The objective function is continuous. 

- But the domain is not compact ($\mathbb{R}^2$
is closed but unbounded). 

3. Denote $D_{\beta} l_i$ as the Jacobian of 
$l_i$ with respect to $\beta$, $H_{\beta} l_i$ 
as the Hessian of $l_i$ with respect to $\beta$.

Notice that $l_i(\beta) = l_i\Big(p_i\big(u_i(\beta)\big)\Big)$, then by the chain rule:
%
$$
D_{\beta}l_i  =D_{p_i}l_i ~D_{u_i}p_i 
~D_{\beta}u_i.
$$
%

We calculate the three terms on the r.h.s. one by one:
%
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
%
Thus,
%
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
%

The Jacobian (gradient) of the MLE objective function is:
%
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
%

We set $h(\beta_i) \equiv (D_\beta l_i)^{\prime}$.
Then 
$ h(\beta)= h\Big(p_i\big(u_i(\beta)\big)\Big)$ 
Thus, by applying the chain rule again,  Hessian of $l_i$ with respect to $\beta$ is:
%
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
%
Thus, the Hessian of the MLE objective function is:
%
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
%

4. If the Hessian $H_{\beta} l$ is negative      definite for all $\beta \in \mathbb{R}^2$, 
then $\det (H_{\beta} l)> 0$ always holds, we 
know there must be at least one solution to 
the first order conditions $D_{\beta} l = 0$ by 
the [Inverse function theorem](https://en.wikipedia.org/wiki/Inverse_function_theorem).
Moreover, if the Hessian is negative definite, 
then the MLE objective is strictly concave,
i.e., there is a unique maximizer of the log likelihood function, which is the unique solution to the first order conditions.

Let us find the conditions under which the Hessian is negative definite.
Notice that $(x_1 - x_2)^2 > 0$ if and only if $x_1 \neq x_2$, and $p_{i1} p_{i2} > 0$ for all $i$. Thus, if $x_1 \neq x_2$, we only need to check the condition 
$det(H_\beta l) > 0$.
Notice that:
%
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

```

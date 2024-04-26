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

4. Derive conditions under which the Hessian of the log-likelihood function is negative definite.

5. Derive conditions under which the likelihood function has a unique maximizer (and thus the logit model has a unique maximum likelihood estimator).



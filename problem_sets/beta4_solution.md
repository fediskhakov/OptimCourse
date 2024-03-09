1. The formulation is not correct. The revenue (after reincerting constant $A$) is $p A k^{\alpha} \ell^{\beta}$, the costs are $w \ell + r k$, and the choice variables are $k$ and $\ell$ ($w$ and $r$ are not chosen by the firm).  
   The constraint $\alpha + \beta < 1$ is irrelevant for the optimization problem, instead it is a constraint on the parameters for the problem to be well posed.
   Relevant constraints on the optimization problem are $k>0$ and $\ell>0$, they can be first ignored and checked after we solve the unconstrained version of the problem.

2. The correct formulation is ($A, p, \alpha, \beta, w, r$ are parameters and should be fixed/found out before the firm solves the optimization problem)

$$
p A k^{\alpha} \ell^{\beta} - w \ell - r k
\rightarrow \max_{k, \ell}
$$
$$
\quad \text{subject to} \quad
k \ge 0, \ell \ge 0
$$

3. See lecture notes
4. See lecture notes
5. Optimal strategy $k^*, \ell^*$ are given in the lecture notes. The maximizer is unique because the objective function is strictly concave when $\alpha+\beta < 1$.

***Proof:***

We check second order conditions for strict concavity.

What we need: for any $k, \ell > 0$

1. $\pi_{11}(k, \ell) < 0$
2. $\pi_{11}(k, \ell) \, \pi_{22}(k, \ell) >  \pi_{12}(k, \ell)^2$

The second order derivatives are

$$
\pi_{11}(k,\ell) = (\alpha-1)\alpha pA k^{\alpha-2} \ell^\beta
$$
$$
\pi_{22}(k,\ell) = (\beta-1)\beta pA k^{\alpha} \ell^{\beta-2}
$$
$$
\pi_{12}(k, \ell) = \alpha \beta pA k^{\alpha-1} \ell^{\beta-1}.
$$

Since $\alpha+\beta<1$ and $\alpha, \beta \geq 0$, we have $\alpha-1<0$, which implies $\pi_{11}(k,\ell)<0$ for all $k, \ell >0$.  
Moreover, the second order differentials imply

$$
\pi_{11}(k, \ell) \, \pi_{22}(k, \ell) = (\alpha-1)(\beta-1)\alpha \beta p^2 A^2 k^{2\alpha-2} \ell^{2\beta-2}
$$

$$
(\pi_{22}(k, \ell))^2 = \alpha^2 \beta^2 p^2 A^2 k^{2\alpha-2} \ell^{2\beta-2}.
$$

Assuming that all parameters and variables are positive.
Then, we obtain $\pi_{11}(k, \ell) \, \pi_{22}(k, \ell) >  \pi_{12}(k, \ell)^2$ if and only if $(\alpha-1)(\beta-1) > \alpha \beta$ if and only if $1 > \alpha + \beta$.

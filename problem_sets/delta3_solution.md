Let $(k, \ell)$ be any point in $A$, and let $\{(k_n, \ell_n)\}$ be any
sequence converging to $(k, \ell)$ in the sense of convergence in $\mathbb{R}^2$. We wish to show that
%

$$
f(k_n, \ell_n) \to f(k, \ell)
$$

%
Since $(k_n, \ell_n) \to (k, \ell)$ in $\mathbb{R}^2$, we know from the facts on
convergence in norm that the individual components converge in $\mathbb{R}$.
That is,
%

$$
k_n \to k
\quad \text{and} \quad
\ell_n \to \ell
$$

%
We also know from the facts that, for any $a$, the function $g(x) = x^a$
is continuous at $x$. It follows from the definition of continuity and
the convergence in $\mathbb{R}$ above that $k_n^\alpha \to k^{\alpha}$ and $\ell^{\beta}_n \to
\ell^\beta$.

Moreover, we know that, for any sequences $\{y_n\}$ and
$\{z_n\}$, if $y_n \to y$ and $z_n \to z$, then $y_n z_n \to yz$. Hence
%

$$
    k_n^\alpha \ell^{\beta}_n \to k^{\alpha}\ell^\beta
$$

%
That is, $f(k_n, \ell_n) \to f(k, \ell)$. Hence $f$ satisfies the
definition of continity.

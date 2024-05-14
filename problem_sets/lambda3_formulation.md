```{admonition} Roy's identity
:class: important

Consider the choice problem of a consumer endowed with strictly concave and differentiable utility function $u \colon \mathbb{R}^N_{++} \to \mathbb{R}$ where $\mathbb{R}^N_{++}$ denotes the set of vector in $\mathbb{R}^N$ with strictly positive elements.

The budget constraint is given by ${\bf p}\cdot{\bf x} \le m$ where ${\bf p} \in \mathbb{R}^N_{++}$ are prices and $m>0$ is income.

Then the demand function $x^\star({\bf p},m)$ and the indirect utility function $v({\bf p},m)$ (value function of the problem) satisfy the equations

$$
x_i^\star({\bf p},m) = -\frac{\partial v}{\partial p_i}({\bf p},m) \Big/ \frac{\partial v}{\partial m}({\bf p},m), \; \forall i \in \{1,\dots,N\}
$$
```

1. Prove the statement

2. Verify the statement by direct calculation (i.e. by expressing the indirect utility and plugging its partials into the identity) using the following specification of utility
%
$$
u({\bf x}) = \prod_{i=1}^N x_i^{\alpha_i}, \; \alpha_i > 0
$$

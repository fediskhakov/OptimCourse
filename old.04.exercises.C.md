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

# Exercise set C

## Question C.1

Consider two convergent sequences in $\mathbb{R}^n$, $\{{\bf x}_i\}_{i=1}^\infty$ and 
$\{{\bf y}_i\}_{i=1}^\infty$ such that 
%
$$
\lim_{i \to \infty} {\bf x}_i = {\bf x} \in \mathbb{R}^n, \quad
\lim_{i \to \infty} {\bf y}_i = {\bf y} \in \mathbb{R}^n
$$
%
Prove the following properties of the limits:
- $\lim_{i \to \infty} ({\bf x}_i+{\bf y}_i) = {\bf x} + {\bf y}$
- $\lim_{i \to \infty} ({\bf x}_i'{\bf y}_i) = {\bf x}'{\bf y}$
- ${\bf x}_i \le {\bf y}_i$ for $\forall i$ component-wise $\implies {\bf x} \le {\bf y}$

```{admonition} Definition
:class: caution

The scalar product ${\bf x}'{\bf y}$ of two vector is $\mathbb{R}$ is defined by ${\bf x}'{\bf y} = \sum_{j=1}^n x_j y_j$

Component-wise comparison of the vectors is defined as ${\bf x} \le {\bf y} \iff x_j \le y_j$ for all $j\in\{1,\dots,N\}$

```


```{tip}
Definition of the limit in $\mathbb{R}^n$ is essentially unchanged from the definition of the limit in $\mathbb{R}$
```

## Question C.2

Show that the Cobb-Douglas production function 
$f(k,l) = k^\alpha l^\beta$ from $[0,\infty) \times [0,\infty)$ to $\mathbb{R}$ is continuous everywhere in its domain.

```{tip}
You can use the fact that, for any $a \in \mathbb{R}$ the function $g(x) = x^a$ is continuous at any $x \in [0,\infty)$. This was mentioned towards the end of lecture 4. 
Also, remember that norm convergence implies element by element convergence.
```

## Question C.3

Let $\beta \in (0,1)$. Show that the utility function $u(c_1,c_2) = \sqrt{c_1} + \beta \sqrt{c_2}$ from $[0,\infty) \times [0,\infty)$ to $\mathbb{R}$ to $\mathbb{R}$ is continuous everywhere in its domain.

## Question C.4

Let $A$ be the set of all consumption pairs $(c_1,c_2)$ such that $c_1 \ge 0$, $c_2 \ge 0$ and $p_1 c_1 + p_2 c_2 \le M$ Here $p_1$, $p_2$ and $M$ are positive constants. Show that $A$ is a closed subset of $\mathbb{R}^2$.

```{tip}
Weak inequalities are preserved under limits
```

## Question C.5

Let ${\bf x}, {\bf y} \in \mathbb{R}^N$ and $\| {\bf x} \| $ denote the Euclidean norm.  Verify the ***Parallelogram Equality*** given by
%
$$
\| {\bf x} + {\bf y} \|^2 + \| {\bf x} - {\bf y} \|^2 = 2 \big( \| {\bf x} \|^2 + \| {\bf y} \|^2 \big)
$$
%

````{dropdown} Solutions

***Question C.1***

Let $\{\mathbf{x}_i\}_{i=1}^\infty$ and $\{\mathbf{y}_i\}_{i=1}^\infty$ be two converget sequences in $\mathbb{R}^n$ such that $\mathbf{x}_i \to \mathbf{x} \in \mathbb{R}^n$ and $\mathbf{y}_i \to y \in \mathbb{R}^n$ as $i \to \infty$.
Recall that $\mathbf{x}_i \to \mathbf{x}$ if and only if $\|\mathbf{x}_i - \mathbf{x}\| \to 0$.

**Proof** of $\lim_{i \to \infty} (\mathbf{x}_i + \mathbf{y}_i) = \mathbf{x} + \mathbf{y}$

Fix $\varepsilon > 0$.
Since $\mathbf{x}_i \to \mathbf{x}$ and $\mathbf{y}_i \to \mathbf{y}$, there exists an $N \in \mathbb{N}$ such that
%

$$
\|\mathbf{x}_i - \mathbf{x}\| < \frac{\varepsilon}{2} \qquad \text{and} \qquad  \|\mathbf{y}_i - \mathbf{y}\| < \frac{\varepsilon}{2}
$$

%
for all $i \geq N$.
Hence, the triangle inequality yields
%

$$
\|(\mathbf{x}_i + \mathbf{y}_i) - (\mathbf{x} + \mathbf{y})\| = \|\mathbf{x}_i - \mathbf{x} + \mathbf{y}_i - \mathbf{y}\| \leq \|\mathbf{x}_i - \mathbf{x}\| + \|\mathbf{y}_i - \mathbf{y}\|< \varepsilon
$$

%
for all $i \geq N$. Therefore, since $\varepsilon$ is arbitrary, we have $\mathbf{x}_i + \mathbf{y}_i \to \mathbf{x} + \mathbf{y}$ as $i \to \infty$.

**Proof** of $\lim_{i \to \infty} (\mathbf{x}_i' \mathbf{y}_i) = \mathbf{x}' \mathbf{y}$

Since $\{\mathbf{x}_i\}_{i=1}^\infty$ and $\{\mathbf{y}_i\}_{i=1}^\infty$ are convergent sequences, they are bounded (why?) by constants $M_x > 0$ and $M_y >0$, respectively.
That is, we have $\|\mathbf{x}_i\|\leq M_x$ and $\|\mathbf{y}_i\|\leq M_y$ for all $i\in\mathbb{N}$.

Let $M:= \max\{M_x, M_y, \|\mathbf{x}\|, \|\mathbf{y}\|\}$.
Fix $\varepsilon > 0$.
Again, since these sequences are convergent, there is an $N \in \mathbb{N}$ such that
%

$$
\|\mathbf{x}_i - \mathbf{x}\| < \frac{\varepsilon}{2M}, \qquad \text{and} \qquad \|\mathbf{y}_i - \mathbf{y}\| < \frac{\varepsilon}{2M}
$$

%
for all $i \geq N$.
The tirangle inequality and Cauchy-Schwarz inequality imply
%

%
$$
|\mathbf{x}_i' \mathbf{y}_i - \mathbf{x}'\mathbf{y}| 
= |\mathbf{x}_i' \mathbf{y}_i - \mathbf{x}' \mathbf{y}_i + \mathbf{x}' \mathbf{y}_i - \mathbf{x}'\mathbf{y}| \\
\leq |\mathbf{x}_i' \mathbf{y}_i - \mathbf{x}' \mathbf{y}_i| + |\mathbf{x}' \mathbf{y}_i - \mathbf{x}'\mathbf{y}| \\
= |(\mathbf{x}_i - \mathbf{x})' \mathbf{y}_i| + |\mathbf{x}'(\mathbf{y}_i-\mathbf{y})| \\
\leq \|\mathbf{y}_i\| \|\mathbf{x}_i-\mathbf{x}\| + \|\mathbf{x}\|\|\mathbf{y}_i - \mathbf{y}\| \\
\leq M \|\mathbf{x}_i - \mathbf{x}\| + M \|\mathbf{y}_i - \mathbf{y}\| \\
< M \frac{\varepsilon}{2M}+ M \frac{\varepsilon}{2M}< \varepsilon
$$
%

%
for all $i \geq N$.
Therefore, since $\varepsilon$ is arbitrary, we have $\mathbf{x}_i'\mathbf{y}_i \to \mathbf{x}'\mathbf{y}$ as $i \to \infty$.

**Proof** of "$\mathbf{x}_i \leq \mathbf{y}_i$ for all $i$ component-wise $\Longrightarrow \mathbf{x} \leq \mathbf{y}$"

Assume that $\mathbf{x}_i \leq \mathbf{y}_i$ for all $i$.
Toward contradiction, suppose that $\mathbf{x} \nleq \mathbf{y}$.
Then, there is $k\in\{1, 2, \dots, n\}$ such that $\mathbf{x}(k) > \mathbf{y}(k)$, where $\mathbf{x}(k)$ denotes the $k$-th component of $\mathbf{x} \in \mathbb{R}^n$.
Let $\varepsilon = \mathbf{x}(k) - \mathbf{y}(k) > 0$.
Since the convergences of $\{\mathbf{x}_i\}_{i=1}^\infty$ and $\{\mathbf{y}_i\}_{i=1}^\infty$ imply the convergences of $\{\mathbf{x}_i(k)\}_{i=1}^\infty$ and $\{\mathbf{y}_i(k)\}_{i=1}^\infty$ (why?),
there is an $N\in\mathbb{N}$ such that
%

$$
|\mathbf{x}_i(k) - \mathbf{x}(k)| < \frac{\varepsilon}{4} \qquad \text{and} \qquad |\mathbf{y}_i(k) - \mathbf{y}(k)| < \frac{\varepsilon}{4} \\
\Rightarrow \mathbf{x}_i(k) > \mathbf{x}(k) - \frac{\varepsilon}{4}  \qquad \text{and} \qquad \mathbf{y}_i(k) < \mathbf{y}(k) + \frac{\varepsilon}{4}
$$

%
for all $i \geq N$.
This implies that $\mathbf{x}_i(k) > \mathbf{y}_i(k)$ for all $i \geq N$.
To see this, observe that
%

$$
\mathbf{x}_i(k) - \mathbf{y}_i(k) > \mathbf{x}(k) - \frac{\varepsilon}{4} -  \Big(\mathbf{y}(k) +\frac{\varepsilon}{4}\Big)> \mathbf{x}(k) - \mathbf{y}(k) -\frac{\varepsilon}{2} = \varepsilon - \frac{\varepsilon}{2} = \frac{\varepsilon}{2}> 0
$$

%
for all $i \geq N$.
Since $\mathbf{x}_i(k)\leq \mathbf{y}_i(k)$ for all $i$ by assumption, we obtain a contraction, which implies that it must be $\mathbf{x} \leq \mathbf{y}$.

***Question C.2***

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

***Question C.3***

The proof is analogous to the proof of continuity of the Cobb-Douglas
production function given above.

***Question C.4***

To show that $A$ is closed, we need to show that the limit of any sequence
contained in $A$ is also in $A$. To this end,
let $\{{\bf x}_n\}$ be an arbitrary sequence in $A$ coverging to a point
${\bf x} \in \mathbb{R}^2$.
Since ${\bf x}_n \in A$ for all $n$ we have
${\bf x}_n \geq {\bf 0}$ in the sense of the component-vise vector inequality
and ${\bf x}_n' {\bf p} \leq m$, where ${\bf p} = (p_1, p_2)$.
We need to show that the same is true for ${\bf x}$.

Since ${\bf x}_n \to {\bf x}$, we have
${\bf x}_n' {\bf p} \to {\bf x}' {\bf p}$. Since limits preserve weak
inequalities and ${\bf x}_n' {\bf p} \leq m$ for all $n$, we have
${\bf x}' {\bf p} \leq m$. Hence it remains only to show that ${\bf x} \geq
0$. Again using the fact that weak inequalities are preserved under
limits, combined with ${\bf x}_n \geq {\bf 0}$ for all $n$, gives
${\bf x} \geq {\bf 0}$ as required.

***Question C.5***

From the definition of Euclidean norm, we have $\|{\bf x}\|^2 = \sum_{i=1}^{N}x_i^2$ where $x_i$ are components of ${\bf x}$. Therefore:
%

$$
\| {\bf x} + {\bf y} \|^2 + \| {\bf x} - {\bf y} \|^2 = \sum_{i=1}^{N}(x_i+y_i)^2 + \sum_{i=1}^{N}(x_i-y_i)^2 = \\
= \sum_{i=1}^{N} \Big( 2 x_i^2 + 2 x_i y_i - 2 x_i y_i + 2 y_i^2 \Big) = 2 \sum_{i=1}^{N}x_i^2 + 2 \sum_{i=1}^{N}y_i^2 = 2 \big( \| {\bf x} \|^2 + \| {\bf y} \|^2 \big)
$$


````
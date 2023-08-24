```{code-cell} python3
:tags: [hide/remote-cell/input/output]
---
mystnb:
image:
width: 80%
align: center
---
tags:
- hide-input
- remove-output

In [1]: import numpy as np

In [2]: from scipy.linalg import solve

In [3]: A = [[0, 2, 4],
...: [1, 4, 8],
...: [0, 3, 7]]

In [4]: b = (1, 2, 0)

In [5]: A, b = np.asarray(A), np.asarray(b)

In [6]: solve(A, b)
Out[6]: array([ 0. , 3.5, -1.5])

```
-->

This tells us that the solution is 


```{code-cell} python3
:tags: [hide/remote-cell/input/output]
---
mystnb:
image:
width: 80%
align: center
---
tags:
- hide-input
- remove-output

array([ 0. , 3.5, -1.5])

```
-->

That is, 
%
$$
%
{\bf x} =
\left(
\begin{array}{c}
x_1 \\
x_2 \\
x_3
\end{array}
\right)
=
\left(
\begin{array}{c}
0 \\
3.5 \\
-1.5
\end{array}
\right)
%
$$
%

Hey, this is easy --- what do we need to study for?

But now let's try this similar looking problem


```{code-cell} python3
:tags: [hide/remote-cell/input/output]
---
mystnb:
image:
width: 80%
align: center
---
tags:
- hide-input
- remove-output

In [1]: import numpy as np

In [2]: from scipy.linalg import solve

In [3]: A = [[0, 2, 4],
...: [1, 4, 8],
...: [0, 3, 6]]

In [4]: b = (1, 2, 0)

In [5]: A, b = np.asarray(A), np.asarray(b)

In [6]: solve(A, b)

```
-->

This is the output that we get

\begin{verbatim}
LinAlgError Traceback (most recent call last)
<ipython-input-8-4fb5f41eaf7c> in <module>()
----> 1 solve(A, b)
/home/john/anaconda/lib/python2.7/site-packages/scipy/linalg/basic.pyc in solve(a, b, sym_pos, lower, overwrite_a, overwrite_b, debug, check_finite)
97 return x
98 if info > 0:
---> 99 raise LinAlgError("singular matrix")
100 raise ValueError('illegal value in %d-th argument of internal gesv|posv'
LinAlgError: singular matrix
\end{verbatim}

What does this mean? How can we fix it?

Moral: We still need to understand the concepts

## Vector Space

### Vector Space

Recall that $\mathbb{R}^N := $ set of all $N$-vectors

An $N$-vector ${\bf x}$ is a tuple of $N$ real numbers:
%
$$
%
{\bf x} = (x_1, \ldots, x_N)
\quad
\text{ where } 
\quad x_n \in \mathbb{R} \text{ for each } n
%
$$ 
%

We can also write ${\bf x}$ vertically, like so: 
%
$$
%
{\bf x} = 
\left(
\begin{array}{c}
x_1 \\
x_2 \\
\vdots \\
x_N
\end{array}
\right)
%
$$
%

```{figure} _static/plots/vec.png
:name: f:vec

Visualization of vector ${\bf x}$ in $\mathbb{R}^2$
```

```{figure} _static/plots/vecs.png
:name: 

Three vectors in $\mathbb{R}^2$ 
```

The vector of ones will be denoted ${\bf 1}$ 

%
$$
%
{\bf 1} := 
\left(
\begin{array}{c}
1 \\
\vdots \\
1
\end{array}
\right)
%
$$
%

Vector of zeros will be denoted ${\bf 0}$

%
$$
%
{\bf 0} := 
\left(
\begin{array}{c}
0 \\
\vdots \\
0
\end{array}
\right)
%
$$
%

## Linear Operations

### Linear Operations

Two fundamental algebraic operations: 
%
1. Vector addition 
9. Scalar multiplication

1. ***Sum*** of ${\bf x} \in \mathbb{R}^N$ and ${\bf y} \in \mathbb{R}^N$ defined by

%
$$
%
{\bf x} + {\bf y} 
:=: 
\left(
\begin{array}{c}
x_1 \\
x_2 \\
\vdots \\
x_N
\end{array}
\right)
+
\left(
\begin{array}{c}
y_1 \\
y_2 \\
\vdots \\
y_N
\end{array}
\right)
:=
\left(
\begin{array}{c}
x_1 + y_1 \\
x_2 + y_2 \\
\vdots \\
x_N + y_N
\end{array}
\right)
%
$$
%

Example 1:

%
$$
%
\left(
\begin{array}{c}
1 \\
2 \\
3 \\
4
\end{array}
\right)
+
\left(
\begin{array}{c}
2 \\
4 \\
6 \\
8
\end{array}
\right)
:=
\left(
\begin{array}{c}
3 \\
6 \\
9 \\
12
\end{array}
\right)
%
$$
%

Example 2:

%
$$
%
\left(
\begin{array}{c}
1 \\
2 \\
3 \\
4
\end{array}
\right)
+
\left(
\begin{array}{c}
1 \\
1 \\
1 \\
1
\end{array}
\right)
:=
\left(
\begin{array}{c}
2 \\
3 \\
4 \\
5
\end{array}
\right)
%
$$
%

```{figure} _static/plots/vec_add.png
:name: f:vec_add

Vector addition
```

2. ***Scalar product*** of $\alpha \in \mathbb{R}$ and ${\bf x} \in \mathbb{R}^N$ defined by

%
$$
%
\alpha {\bf x} 
=
\alpha \left(
\begin{array}{c}
x_1 \\
x_2 \\
\vdots \\
x_N
\end{array}
\right)
:=
\left(
\begin{array}{c}
\alpha x_1 \\
\alpha x_2 \\
\vdots \\
\alpha x_N
\end{array}
\right)
%
$$
%

Example 1:

%
$$
%
0.5 
\left(
\begin{array}{c}
1 \\
2 \\
3 \\
4
\end{array}
\right)
:=
\left(
\begin{array}{c}
0.5 \\
1.0 \\
1.5 \\
2.0 
\end{array}
\right)
%
$$
%

Example 2:

%
$$
%
-1
\left(
\begin{array}{c}
1 \\
2 \\
3 \\
4
\end{array}
\right)
:=
\left(
\begin{array}{c}
-1 \\
-2 \\
-3 \\
-4
\end{array}
\right)
%
$$
%

```{figure} _static/plots/vec_scalar.png
:name: f:vec_scalar

Scalar multiplication
```

Subtraction performed element by element, analogous to addition 

%
$$
%
{\bf x} - {\bf y} 
:=
\left(
\begin{array}{c}
x_1 - y_1 \\
x_2 - y_2 \\
\vdots \\
x_N - y_N
\end{array}
\right)
%
$$
%

Def can be given in terms of addition and scalar multiplication:

%
$$
%
{\bf x} - {\bf y} := {\bf x} + (-1) {\bf y} 
%
$$
%

```{figure} _static/plots/vec_minus.png
:name: f:vec_minus

Difference between vectors
```

Incidentally, most high level numerical libraries treat vector addition
and scalar multiplication in the same way --- elementwise


```{code-cell} python3
:tags: [hide/remote-cell/input/output]
---
mystnb:
image:
width: 80%
align: center
---
tags:
- hide-input
- remove-output

In [1]: import numpy as np

In [2]: x = np.array((2, 4, 6))

In [3]: y = np.array((10, 10, 10))

In [4]: x + y # Vector addition
Out[4]: array([12, 14, 16])

In [6]: 2 * x # Scalar multiplication
Out[6]: array([ 4, 8, 12])

```
-->

A ***linear combination*** of vectors ${\bf x}_1,\ldots, {\bf x}_K$ in $\mathbb{R}^N$ 
is a vector 
%
$$
%
{\bf y} = \sum_{k=1}^K \alpha_k {\bf x}_k 
= \alpha_1 {\bf x}_1 + \cdots + \alpha_K {\bf x}_K 
%
$$
%
where $\alpha_1,\ldots, \alpha_K$ are scalars

\Eg

%
$$
%
0.5 \left(
\begin{array}{c}
6.0 \\
2.0 \\
8.0
\end{array}
\right)
+
3.0 \left(
\begin{array}{c}
0 \\
1.0 \\
-1.0
\end{array}
\right)
=
\left(
\begin{array}{c}
3.0 \\
4.0 \\
1.0
\end{array}
\right)
%
$$
%

### Inner Product

The ***inner product*** of two vectors ${\bf x}$ and ${\bf y}$ in $\mathbb{R}^N$ is
%
$$
%
{\bf x}' {\bf y} :=
\sum_{n=1}^N x_n y_n
%
$$
%

Example: ${\bf x} = (2, 3)$ and ${\bf y} = (-1, 1)$ implies that
%
$$
%
{\bf x}' {\bf y} 
= 2 \times (-1) + 3 \times 1 
= 1
%
$$
%

Example: ${\bf x} = (1/N) {\bf 1}$ and ${\bf y} = (y_1, \ldots, y_N)$ implies 
%
$$
%
{\bf x}' {\bf y} 
= \frac{1}{N} \sum_{n=1}^N y_n
%
$$
%


```{code-cell} python3
:tags: [hide/remote-cell/input/output]
---
mystnb:
image:
width: 80%
align: center
---
tags:
- hide-input
- remove-output

In [1]: import numpy as np

In [2]: x = np.array((1, 2, 3, 4))

In [3]: y = np.array((2, 4, 6, 8))

In [6]: np.sum(x * y) # Inner product
Out[6]: 60

```
-->

```{admonition} Fact
:class: important

For any $\alpha, \beta \in \mathbb{R}$ and any ${\bf x}, {\bf y} \in \mathbb{R}^N$, the following 
```
statements are true:
%
1. ${\bf x}' {\bf y} = {\bf y}' {\bf x}$
- $(\alpha {\bf x})' (\beta {\bf y}) = \alpha \beta ({\bf x}' {\bf y})$
9. ${\bf x}' ({\bf y} + {\bf z}) = {\bf x}' {\bf y} + {\bf x}' {\bf z}$
%

For example, item 2 is true because
%
$$
%
(\alpha {\bf x})' (\beta {\bf y}) 
= \sum_{n=1}^N \alpha x_n \beta y_n
= \alpha \beta \sum_{n=1}^N x_n y_n
= \alpha \beta ({\bf x}' {\bf y})
%
$$
%

**Exercise:** Use above rules to show that 
$(\alpha {\bf y} + \beta {\bf z})'{\bf x} = \alpha {\bf x}' {\bf y} + \beta {\bf x}' {\bf z}$

The next result is a generalization

```{admonition} Fact
:class: important

Inner products of linear combinations satisfy 
```
%
$$
%
\left(
\sum_{k=1}^K \alpha_k {\bf x}_k
\right)' 
\left(
\sum_{j=1}^J \beta_j {\bf y}_j 
\right)
=
\sum_{k=1}^K \sum_{j=1}^J \alpha_k \beta_j {\bf x}_k' {\bf y}_j 
%
$$
%

## Norms and Distance

### Norms and Distance

The (Euclidean) ***norm*** of ${\bf x} \in \mathbb{R}^N$ is defined as
%
$$
%
\| {\bf x} \| 
:= \sqrt{{\bf x}' {\bf x} } 
= \left( \sum_{n=1}^N x_n^2 \right)^{1/2}
%
$$
%

Interpretation:
%
- $\| {\bf x} \|$ represents the ``length'' of ${\bf x}$

- $\| {\bf x} - {\bf y} \|$ represents distance between ${\bf x}$ and ${\bf y}$

```{figure} _static/plots/vec.png
:name: f:vec_rpt

Length of red line $= \sqrt{x_1^2 + x_2^2}
=: \|{\bf x}\|$ 
```

$\| {\bf x} - {\bf y} \|$ represents distance between ${\bf x}$ and ${\bf y}$

```{figure} _static/plots/vec_minus.png
:name: 

```

```{admonition} Fact
:class: important

For any $\alpha \in \mathbb{R}$ and any ${\bf x}, {\bf y} \in \mathbb{R}^N$, the following 
```
statements are true:
%
1. $\| {\bf x} \| \geq 0$ and $\| {\bf x} \| = 0$ if and only if
${\bf x} = {\bf 0}$

- $\| \alpha {\bf x} \| = |\alpha| \| {\bf x} \|$

- $\| {\bf x} + {\bf y} \| \leq \| {\bf x} \| + \| {\bf y} \|$
(***triangle inequality***)

- $| {\bf x}' {\bf y} | \leq \| {\bf x} \| \| {\bf y} \|$
(***Cauchy-Schwarz inequality***)

%

For example, let's show that $\| {\bf x} \| = 0 \iff {\bf x} = {\bf 0}$

First let's assume that $\| {\bf x} \| = 0$ and show ${\bf x} = {\bf 0}$

Since $\| {\bf x} \| = 0$ we have $\| {\bf x} \|^2 = 0$ and hence
$\sum_{n=1}^N x^2_n = 0$

That is $x_n = 0$ for all $n$, or, equivalently, ${\bf x} = {\bf 0}$

Next let's assume that ${\bf x} = {\bf 0}$ and show $\| {\bf x} \| = 0$ 

This is immediate from the definition of the norm

```{admonition} Fact
:class: important

If ${\bf x} \in \mathbb{R}^N$ is nonzero, then the solution to the optimization problem 
```
%
$$
%
\max_{{\bf y}} {\bf x}'{\bf y} 
\quad \text{ subject to } \quad
{\bf y} \in \mathbb{R}^N \text{ and } \| {\bf y} \| = 1 
%
$$
%
is ${\hat{\bf x}} := {\bf x} / \| {\bf x} \|$

```{figure} _static/plots/max_inner_prod.png
:name: 

```

Proof: Fix nonzero ${\bf x} \in \mathbb{R}^N$

Let ${\hat{\bf x}} := {\bf x} / \| {\bf x} \| := \alpha {\bf x}$ when $\alpha := 1/\|{\bf x}\|$

Evidently $\| {\hat{\bf x}} \| = 1$

Pick any other ${\bf y} \in \mathbb{R}^N$ satisfying $\| {\bf y} \| = 1$

The Cauchy-Schwarz inequality yields
%
$$
%
{\bf y}' {\bf x}
\leq |{\bf y}' {\bf x}|
\leq \| {\bf y} \| \| {\bf x} \|
= \| {\bf x} \|
= \frac{{\bf x}' {\bf x}}{ \| {\bf x} \| }
= {\hat{\bf x}}' {\bf x}
%
$$
%
Hence ${\hat{\bf x}}$ is the maximizer, as claimed

## Span

### Span

Let $X \subset \mathbb{R}^N$ be any nonempty set

Set of all possible linear combinations of elements of $X$ is 
called the ***span*** of $X$, denoted by $\mathrm{span}(X)$

For finite $X := \{{\bf x}_1,\ldots, {\bf x}_K\}$ the span can be expressed
as 
% 
%
$$
%
\mathrm{span}(X):= \left\{ \text{ all } \sum_{k=1}^K \alpha_k {\bf x}_k 
\text{ such that }
(\alpha_1,\ldots, \alpha_K) \in \mathbb{R}^K \right\}
%
$$
%

We are mainly interested in the span of finite sets...

```{admonition} Example
:class: tip

Let's start with the span of a singleton

Let $X = \{ {\bf 1} \} \subset \mathbb{R}^2$, where ${\bf 1} := (1,1)$ 

The span of $X$ is all vectors of the form 

%
$$
%
\alpha {\bf 1} 
=
\left(
\begin{array}{c}
\alpha \\
\alpha
\end{array}
\right)
\quad \text{ with } \quad \alpha \in \mathbb{R} 
%
$$
%

Constitutes a line in the plane that passes through

- the vector ${\bf 1}$ (set $\alpha = 1$)
- the origin ${\bf 0}$ (set $\alpha = 0$)

```

```{figure} _static/plots/span_of_one_vec.png
:name: 

The span of ${\bf 1} := (1,1)$ in $\mathbb{R}^2$
```

```{admonition} Example
:class: tip

Let ${\bf x}_1 = (3, 4, 2)$ and let ${\bf x}_2 = (3, -4, 0.4)$

By definition, the span is all vectors of the form

%
$$
%
{\bf y} = 
\alpha \left(
\begin{array}{c}
3 \\
4 \\
2
\end{array}
\right)
+
\beta \left(
\begin{array}{c}
3 \\
-4 \\
0.4
\end{array}
\right)
\quad \text{where} \quad
\alpha, \beta \in \mathbb{R}
%
$$
%

It turns out to be a plane that passes through

- the vector ${\bf x}_1$
- the vector ${\bf x}_2$
- the origin ${\bf 0}$

```

```{figure} _static/plots/span_plane.png
:name: f:span_plane

Span of ${\bf x}_1, {\bf x}_2$
```

```{admonition} Fact
:class: important

If $X \subset Y$, then $\mathrm{span}(X) \subset \mathrm{span}(Y)$
```

To see this, pick any nonempty $X \subset Y \subset \mathbb{R}^N$

Letting ${\bf z} \in \mathrm{span}(X)$, we have

%
$$
%
{\bf z} = \sum_{k=1}^K \alpha_k {\bf x}_k 
\text{ for some }
{\bf x}_1, \ldots, {\bf x}_K \in X, \; 
\alpha_1, \ldots, \alpha_K \in \mathbb{R}
%
$$
%

Since $X \subset Y$, each ${\bf x}_k$ is also in $Y$, giving us

%
$$
%
{\bf z} = \sum_{k=1}^K \alpha_k {\bf x}_k 
\text{ for some }
{\bf x}_1, \ldots, {\bf x}_K \in Y, \; 
\alpha_1, \ldots, \alpha_K \in \mathbb{R}
%
$$
%

Hence ${\bf z} \in \mathrm{span}(Y)$

Let $Y$ be any subset of $\mathbb{R}^N$, and let $X:= \{{\bf x}_1,\ldots, {\bf x}_K\}$ 

If $Y \subset \mathrm{span}(X)$, we say that the vectors in $X$ ***span the set*** $Y$

Alternatively, we say that $X$ is a ***spanning set*** for $Y$

A nice situation: $Y$ is large but $X$ is small

$\implies$ large set $Y$ ``described'' by the small number of vectors in $X$

```{admonition} Example
:class: tip

Consider the vectors $\{{\bf e}_1, \ldots, {\bf e}_N\} \subset \mathbb{R}^N$, where

%
$$
%
{\bf e}_1 := 
\left(
\begin{array}{c}
1 \\
0 \\
\vdots \\
0
\end{array}
\right),
\quad 
{\bf e}_2 := 
\left(
\begin{array}{c}
0 \\
1 \\
\vdots \\
0
\end{array}
\right),
\; 
\cdots,
\;
{\bf e}_N := 
\left(
\begin{array}{c}
0 \\
0 \\
\vdots \\
1
\end{array}
\right)
%
$$
%

That is, ${\bf e}_n$ has all zeros except for a $1$ as the $n$-th element

Vectors ${\bf e}_1, \ldots, {\bf e}_N$ called the ***canonical basis vectors*** of $\mathbb{R}^N$

```

```{figure} _static/plots/vec_canon.png
:name: f:vec_canon

Canonical basis vectors in $\mathbb{R}^2$
```

```{admonition} Fact
:class: important

The span of $\{{\bf e}_1, \ldots, {\bf e}_N\}$ is equal
```
to all of $\mathbb{R}^N$

Proof for $N=2$: 

Pick any ${\bf y} \in \mathbb{R}^2$ 

We have
%
$$
%
{\bf y} 
:=
\left(
\begin{array}{c}
y_1 \\
y_2
\end{array}
\right)
=
\left(
\begin{array}{c}
y_1 \\
0
\end{array}
\right)
+
\left(
\begin{array}{c}
0 \\
y_1
\end{array}
\right)
\\
=
y_1
\left(
\begin{array}{c}
1 \\
0
\end{array}
\right)
+
y_2
\left(
\begin{array}{c}
0 \\
1
\end{array}
\right)
= y_1 {\bf e}_1 + y_2 {\bf e}_2
%
$$
%
Thus, ${\bf y} \in \mathrm{span} \{{\bf e}_1, {\bf e}_2\}$ 

Since ${\bf y}$ arbitrary, we have shown that $\mathrm{span} \{{\bf e}_1,
{\bf e}_2\} = \mathbb{R}^2$

```{figure} _static/plots/vec_canon_x.png
:name: f:vec_canon2

Canonical basis vectors in $\mathbb{R}^2$
```

```{admonition} Example
:class: tip

Consider the set 
```
%
$$
%
P := \{ (x_1, x_2, 0) \in \mathbb{R}^3 \colon x_1, x_2 \in \mathbb{R \}}
%
$$
%

Graphically, $P =$ flat plane in $\mathbb{R}^3$, where height
coordinate $=0$

```{figure} _static/plots/flat_plane_no_vecs.png
:name: 

```

Let ${\bf e}_1$ and ${\bf e}_2$ be the canonical basis vectors in $\mathbb{R}^3$

***Claim***: $\mathrm{span}\{{\bf e}_1, {\bf e}_2\} = P$ 

Proof:

Let ${\bf x} = (x_1, x_2, 0)$ be any element of $P$

We can write ${\bf x}$ as 

%
$$
%
{\bf x} = 
\left(
\begin{array}{c}
x_1 \\
x_2 \\
0
\end{array}
\right)
=
x_1
\left(
\begin{array}{c}
1 \\
0 \\
0
\end{array}
\right)
+ 
x_2
\left(
\begin{array}{c}
0 \\
1 \\
0
\end{array}
\right)
= x_1 {\bf e}_1 + x_2 {\bf e}_2
%
$$
%

In other words, $P \subset \mathrm{span}\{{\bf e}_1, {\bf e}_2\}$

Conversely (check it) we have $\mathrm{span}\{{\bf e}_1, {\bf e}_2\} \subset P$ 

```{figure} _static/plots/flat_plane_e_vecs.png
:name: 

$\mathrm{span}\{{\bf e}_1, {\bf e}_2\} = P$
```

## Linear Subspaces

### Linear Subspaces

A nonempty $S \subset \mathbb{R}^N$ called a \navy{linear
subspace} of $\mathbb{R}^N$ if
%
$$
%
{\bf x}, {\bf y} \in S \; \text{ and } \;\alpha, \beta \in \mathbb{R}
\quad \implies \quad
\alpha {\bf x} + \beta {\bf y} \in S 
%
$$
%

In other words, $S \subset \mathbb{R}^N$ is "closed" under vector addition
and scalar multiplication

Note: Sometimes we just say ***subspace***...

```{admonition} Example
:class: tip

$\mathbb{R}^N$ itself is a linear subspace of $\mathbb{R}^N$
```

```{admonition} Example
:class: tip

Fix ${\bf a} \in \mathbb{R}^N$ and let $A := \{ {\bf x} \in \mathbb{R}^N \colon {\bf a \}' {\bf x} = 0}$

```{admonition} Fact
:class: important

The set $A$ is a linear subspace of $\mathbb{R}^N$
```

Proof: Let ${\bf x}, {\bf y} \in A$ and let $\alpha, \beta \in \mathbb{R}$

We must show that ${\bf z} := \alpha {\bf x} + \beta {\bf y} \in A$ 

Equivalently, that ${\bf a}' {\bf z} = 0$

True because
%
$$
%
{\bf a}' {\bf z} =
{\bf a}' (\alpha {\bf x} + \beta {\bf y}) = \alpha
{\bf a}' {\bf x} + \beta {\bf a}' {\bf y} = 0 + 0 = 0
%
$$
%

```

```{admonition} Fact
:class: important

If $Z$ is a nonempty subset of $\mathbb{R}^N$, then $\mathrm{span}(Z)$ is a linear
```
subspace

Proof: If ${\bf x}, {\bf y} \in \mathrm{span}(Z)$, then $\exists$ vectors ${\bf z}_k$ in $Z$ 
and scalars $\gamma_k$ and $\delta_k$ such that 
%
$$
%
{\bf x} = \sum_{k=1}^K \gamma_k {\bf z}_k
\quad \text{and} \quad
{\bf y} = \sum_{k=1}^K \delta_k {\bf z}_k
%
$$
%
$$
%
\text{ therefore }
\alpha {\bf x} = \sum_{k=1}^K \alpha \gamma_k {\bf z}_k
\quad \text{and} \quad
\beta {\bf y} = \sum_{k=1}^K \beta \delta_k {\bf z}_k 
%
$$
%
$$
%
\text{ therefore }
\alpha {\bf x} + \beta {\bf y} 
= \sum_{k=1}^K (\alpha \gamma_k + \beta \delta_k) {\bf z}_k 
%
$$
%

This vector clearly lies in $\mathrm{span}(Z)$

```{admonition} Fact
:class: important

If $S$ and $S'$ are two linear subspaces of $\mathbb{R}^N$, then $S
```
\cap S'$ is also a linear subspace of $\mathbb{R}^N$.

Proof: Let $S$ and $S'$ be two linear subspaces of $\mathbb{R}^N$

Fix ${\bf x}, {\bf y} \in S \cap S'$ and $\alpha, \beta \in \mathbb{R}$

We claim that ${\bf z} := \alpha {\bf x} + \beta {\bf y} \in S \cap S'$

- Since ${\bf x}, {\bf y} \in S$ and $S$ is a linear subspace we have ${\bf z} \in S$

- Since ${\bf x}, {\bf y} \in S'$ and $S'$ is a linear subspace we have ${\bf z} \in S'$

Therefore ${\bf z} \in S \cap S'$

Other examples of linear subspaces
% 
- The singleton $\{{\bf 0}\}$ in $\mathbb{R}^N$

- Lines through the origin in $\mathbb{R}^2$ and $\mathbb{R}^3$

- Planes through the origin in $\mathbb{R}^3$

**Exercise:** Let $S$ be a linear subspace of $\mathbb{R}^N$. Show that

1. ${\bf 0} \in S$
- If $X \subset S$, then $\mathrm{span}(X) \subset S$
9. $\mathrm{span}(S) = S$

## Linear Independence

### Linear Independence

Important applied questions

- When is a matrix invertible?
- When do regression arguments suffer from collinearity?
- When does a set of linear equations have a solution?
- When is that solution unique?
- How can we approximate complex functions parsimoniously?
- What is the rank of a matrix?

All of these questions closely related to linear independence 

### Definition

A nonempty collection of vectors $X := \{{\bf x}_1,\ldots, {\bf x}_K\}
\subset \mathbb{R}^N$ is called ***linearly independent*** if
%
$$
%
\sum_{k=1}^K \alpha_k {\bf x}_k
= {\bf 0} 
\; \implies \;
\alpha_1 = \cdots = \alpha_K = 0
%
$$
%

As we'll see, linear independence of a set of vectors determines how large
a space they span

Loosely speaking, linearly independent sets span large spaces

```{admonition} Example
:class: tip

Let ${\bf x} := (1, 2)$ and ${\bf y} := (-5, 3)$
```

The set $X = \{{\bf x}, {\bf y}\}$ is linearly independent in $\mathbb{R}^2$

Indeed, suppose $\alpha_1$ and $\alpha_2$ are scalars with

%
$$
%
\alpha_1
\left(
\begin{array}{c}
1 \\
2
\end{array}
\right)
+ 
\alpha_2
\left(
\begin{array}{c}
-5 \\
3
\end{array}
\right)
=
{\bf 0}
%
$$
%
Equivalently,
%
$$
%
\alpha_1 = 5 \alpha_2
\\
2 \alpha_1 = -3 \alpha_2
%
$$
%

Then $2(5\alpha_2) = 10 \alpha_2 = -3 \alpha_2$, implying $\alpha_2 = 0$
and hence $\alpha_1 = 0$ 

```{admonition} Example
:class: tip

The set of canonical basis vectors $\{{\bf e}_1, \ldots, {\bf e}_N\}$
is linearly independent in $\mathbb{R}^N$

Proof: Let $\alpha_1, \ldots, \alpha_N$ be coefficients such that
$\sum_{k=1}^N \alpha_k {\bf e}_k = {\bf 0}$

Then
%
$$
%
\left(
\begin{array}{c}
\alpha_1 \\
\alpha_2 \\
\vdots \\
\alpha_N
\end{array}
\right)
= \sum_{k=1}^N \alpha_k {\bf e}_k 
= {\bf 0}
=
\left(
\begin{array}{c}
0 \\
0 \\
\vdots \\
0
\end{array}
\right)
%
$$
%

In particular, $\alpha_k = 0$ for all $k$

Hence $\{{\bf e}_1, \ldots, {\bf e}_N\}$ linearly independent

```

As a first step to better understanding linear independence let's look at
some equivalences

Take $X := \{{\bf x}_1,\ldots, {\bf x}_K\} \subset \mathbb{R}^N$

```{admonition} Fact
:class: important

For $K > 1$ all of following statements are equivalent
```
%
1. $X$ is linearly independent

- No ${\bf x}_i \in X$ can be written as linear combination of the others

9. $X_0 \subsetneq X \implies \mathrm{span}(X_0) \subsetneq \mathrm{span}(X)$
%

- Here $X_0 \subsetneq X$ means $X_0 \subset X$ and $X_0 \ne X$

- We say that $X_0$ is a ***proper subset*** of $X$ 

As an exercise, let's show that the first two statements are equivalent

The first is
%
$$
%
\tag{$\text{ such that }ar$}
\sum_{k=1}^K \alpha_k {\bf x}_k
= {\bf 0} 
\; \implies \;
\alpha_1 = \cdots = \alpha_K = 0
%
$$ (eq:cli)
%

The second is
%
$$
%
\tag{$\text{ such that }ar\text{ such that }ar$}
\text{no ${\bf x}_i \in X$ can be written as linear combination of others}
%
$$ (eq:cli2)
%

We now show that
%
- {eq}`eq:cli` $\implies$ {eq}`eq:cli2`, and
- {eq}`eq:cli2` $\implies$ {eq}`eq:cli`

To show that {eq}`eq:cli` $\implies$ {eq}`eq:cli2` let's suppose to the contrary that

1. $\sum_{k=1}^K \alpha_k {\bf x}_k = {\bf 0} \implies \alpha_1 = \cdots = \alpha_K = 0$ 
- and yet some ${\bf x}_i$ can be written as a linear combination
of the other elements of $X$

In particular, suppose that
%
$$
%
{\bf x}_i = \sum_{k \ne i} \alpha_k {\bf x}_k 
%
$$
%
Then, rearranging,
%
$$
%
\alpha_1 {\bf x}_1 + \cdots + (-1) {\bf x}_i 
+ \cdots + \alpha_K {\bf x}_K = {\bf 0}
%
$$
%

This contradicts 1., and hence {eq}`eq:cli2` holds

To show that {eq}`eq:cli2` $\implies$ {eq}`eq:cli` let's suppose to
the contrary that 

1. no ${\bf x}_i$ can be written as a linear combination of others
9. and yet $\exists$ $\alpha_1, \ldots, \alpha_K$ not all zero with $\alpha_1 {\bf x}_1 + \cdots + \alpha_K {\bf x}_K = {\bf 0}$ 

Suppose without loss of generality that $\alpha_1 \ne 0$

(Similar argument works for any $\alpha_j$)

Then
%
$$
%
{\bf x}_1 = \frac{\alpha_2}{-\alpha_1} {\bf x}_2 
+ \cdots + \frac{\alpha_K}{-\alpha_1} {\bf x}_K 
%
$$
%

This contradicts 1., and hence {eq}`eq:cli` holds

Let's show one more part of the proof as an exercise:
%
$$
%
X \text{ linearly independent } 
\implies
\text{ proper subsets of $X$ have smaller span}
%
$$
%

Proof: Suppose to the contrary that 
%
1. $X$ is linearly independent,
- $X_0 \subsetneq X$ and yet
9. $\mathrm{span}(X_0) = \mathrm{span}(X)$

Let ${\bf x}_j$ be in $X$ but not $X_0$

Since ${\bf x}_j \in \mathrm{span}(X)$, we also have ${\bf x}_j \in \mathrm{span}(X_0)$

But then ${\bf x}_j$ can be written as a linear combination of the other
elements of $X$

This contradicts linear independence

```{admonition} Example
:class: tip

Dropping any of the canonical basis vectors reduces span
```

Consider the $N=2$ case

We know that $\mathrm{span} \{{\bf e}_1, {\bf e}_2\} =$ all of $\mathbb{R}^2$

Removing either element of $\mathrm{span} \{{\bf e}_1, {\bf e}_2\}$ reduces the span to a line

```{figure} _static/plots/vec_h_axis.png
:name: f:vec_h_axis

The span of $\{{\bf e}_1\}$ alone is the horizonal axis
```

```{admonition} Example
:class: tip

As another visual example of linear independence, consider the pair
```

%
$$
%
{\bf x}_1 =
\begin{pmatrix}
3 \\
4 \\
2
\end{pmatrix}
\quad \text{and} \quad
{\bf x}_2 =
\begin{pmatrix}
3 \\
-4 \\
1
\end{pmatrix}
%
$$
%

The span of this pair is a plane in $\mathbb{R}^3$

But if we drop either one the span reduces to a line

```{figure} _static/plots/nonredundant1.png
:name: 

The span of $\{{\bf x}_1, {\bf x}_2\}$ is a plane
```

```{figure} _static/plots/nonredundant2.png
:name: 

The span of $\{{\bf x}_1\}$ alone is a line
```

```{figure} _static/plots/nonredundant3.png
:name: 

The span of $\{{\bf x}_2\}$ alone is a line
```

### Linear Dependence

If $X$ is not linearly independent then it is called ***linearly dependent***

We saw above that 

linear independence $\iff$ dropping any elements reduces span

Hence $X$ is linearly dependent when some
elements can be removed without changing $\mathrm{span}(X)$

That is,
%
$$\exists \, X_0 \subsetneq X \; \text{ such that } \; \mathrm{span}(X_0) = \mathrm{span}(X)$$
%

```{admonition} Example
:class: tip

As an example with redundacy, consider $\{{\bf x}_1, {\bf x}_2\} \subset \mathbb{R}^2$ where 
```
%
- ${\bf x}_1 = {\bf e}_1 := (1, 0)$
- ${\bf x}_2 = (-2, 0)$

```{figure} _static/plots/vec_noncanon.png
:name: f:vec_noncanon

The vectors ${\bf x}_1$ and ${\bf x}_2$
```

We claim that $\mathrm{span} \{{\bf x}_1, {\bf x}_2\} = \mathrm{span}\{{\bf x}_1\}$

Proof: $\mathrm{span} \{{\bf x}_1\} \subset \mathrm{span}\{{\bf x}_1, {\bf x}_2\}$ is clear (why?)

To see the reverse, pick any ${\bf y} \in \mathrm{span} \{{\bf x}_1, {\bf x}_2\}$ 

By definition, 
%
$$
%
\exists \;
\alpha_1,\alpha_2 \; \text{ such that } \;
{\bf y} 
= \alpha_1 {\bf x}_1 + \alpha_2 {\bf x}_2
=
\alpha_1 
\begin{pmatrix}
1 \\
0
\end{pmatrix}
+ \alpha_2 
\begin{pmatrix}
-2 \\
0
\end{pmatrix}
%
$$
%
$$
%
\text{ therefore } 
{\bf y} 
= \alpha_1 
\begin{pmatrix}
1 \\
0
\end{pmatrix}
- 2 \alpha_2 
\begin{pmatrix}
1 \\
0
\end{pmatrix}
= (\alpha_1 - 2 \alpha_2)
\begin{pmatrix}
1 \\
0
\end{pmatrix}
= (\alpha_1 -2 \alpha_2 ) {\bf x}_1 
%
$$
%

The right hand side is clearly in $\mathrm{span} \{{\bf x}_1\}$

Hence $\mathrm{span} \{{\bf x}_1, {\bf x}_2\} \subset \mathrm{span} \{{\bf x}_1\}$ as claimed

## Implications of Independence

### Implications of Independence

Let $X := \{{\bf x}_1,\ldots, {\bf x}_K\} \subset \mathbb{R}^N$

```{admonition} Fact
:class: important

If $X$ is linearly independent, then $X$ does not contain ${\bf 0}$
```

**Exercise:** Prove it

```{admonition} Fact
:class: important

If $X$ is linearly independent, then every subset of $X$ is linearly independent 
```

Sketch of proof: Suppose for example that $\{{\bf x}_1,\ldots,
{\bf x}_{K-1}\} \subset X$ is linearly dependent

Then $\exists \; \alpha_1, \ldots, \alpha_{K-1}$ not all zero with 
$\sum_{k=1}^{K-1} \alpha_k {\bf x}_k = {\bf 0}$

Setting $\alpha_K =0$ we can write this as $\sum_{k=1}^K \alpha_k {\bf x}_k = {\bf 0}$

Not all scalars zero so contradicts linear independence of $X$ 

```{admonition} Fact
:class: important

If $X:= \{{\bf x}_1,\ldots, {\bf x}_K\} \subset \mathbb{R}^N$ is linearly
```
independent and ${\bf z}$ is an $N$-vector not in $\mathrm{span}(X)$, then $X \cup
\{ {\bf z} \}$ is linearly independent 

Proof: Suppose to the contrary that $X \cup \{ {\bf z} \}$ is linearly
dependent:
%
$$
%
\exists \; \alpha_1, \ldots, \alpha_K, \beta
\text{ not all zero with }
\sum_{k=1}^K \alpha_k {\bf x}_k + \beta {\bf z} = {\bf 0}
%
$$ (eq:m)
%

If $\beta=0$, then by {eq}`eq:m` we have $\sum_{k=1}^K \alpha_k {\bf x}_k = {\bf 0}$ and 
$\alpha_k \ne 0$ for some $k$, a contradiction

If $\beta \ne0$, then by {eq}`eq:m` we have 
%
$$
%
{\bf z} = \sum_{k=1}^K \frac{-\alpha_k}{\beta} {\bf x}_k 
%
$$
%
Hence ${\bf z} \in \mathrm{span}(X)$ --- contradiction

### Unique Representations

Let 
% 
- $X := \{{\bf x}_1,\ldots,{\bf x}_K\} \subset \mathbb{R}^N$

- ${\bf y} \in \mathbb{R}^N$

We know that if ${\bf y} \in \mathrm{span}(X)$, then exists representation
%
$$
%
{\bf y} = \sum_{k=1}^K \alpha_k {\bf x}_k
%
$$
%

But when is this representation unique?

Answer: When $X$ is linearly independent

```{admonition} Fact
:class: important

If $X = \{{\bf x}_1,\ldots, {\bf x}_K\} \subset \mathbb{R}^N$ is linearly independent and
```
${\bf y} \in \mathbb{R}^N$, then there is at most one set of scalars $\alpha_1,\ldots,\alpha_K$ such
that ${\bf y} = \sum_{k=1}^K \alpha_k {\bf x}_k$

Proof: Suppose there are two such sets of scalars

That is,
%
$$
%
\exists \;
\alpha_1, \ldots, \alpha_K
\text{ and } \beta_1, \ldots, \beta_K
\; \text{ such that } \; 
{\bf y} 
= \sum_{k=1}^K \alpha_k {\bf x}_k
= \sum_{k=1}^K \beta_k {\bf x}_k
%
$$
%
$$
%
\text{ therefore } \sum_{k=1}^K (\alpha_k - \beta_k) {\bf x}_k = {\bf 0}
%
$$ 
%

%
$$
%
\text{ therefore }
\alpha_k = \beta_k 
\quad \text{for all} \quad k
%
$$
%

## Span and Independence

### Exchange Lemma

Here's one of the most fundamental results in linear algebra

```{admonition} Fact
:class: important

(Exchange lemma) If 
```
%
1. $S$ is a linear subspace of $\mathbb{R}^N$
9. $S$ is spanned by $K$ vectors,
%
then any linearly independent subset of $S$ has at most $K$
vectors

Proof: Omitted

```{admonition} Example
:class: tip

If $X := \{{\bf x}_1, {\bf x}_2, {\bf x}_3\} \subset \mathbb{R}^2$
```
then $X$ is linearly dependent

- because $\mathbb{R}^2$ is spanned by the two vectors ${\bf e}_1, {\bf e}_2$

```{figure} _static/plots/vecs.png
:name: 

Must be linearly dependent
```

```{admonition} Example
:class: tip

Recall the plane
%
$$
%
P := \{ (x_1, x_2, 0) \in \mathbb{R}^3 \colon x_1, x_2 \in \mathbb{R \}}
%
$$
%

- flat plane in $\mathbb{R}^3$ where height coordinate $=$ zero 

We showed before that $\mathrm{span}\{{\bf e}_1, {\bf e}_2\} = P$ for 

%
$$
%
{\bf e}_1 := 
\left(
\begin{array}{c}
1 \\
0 \\
0
\end{array}
\right),
\quad 
{\bf e}_2 := 
\left(
\begin{array}{c}
0 \\
1 \\
0
\end{array}
\right)
%
$$
%

Therefore any three vectors lying in $P$ are linearly dependent

```

```{figure} _static/plots/flat_plane.png
:name: 

Any three vectors in $P$ are linearly dependent
```

### When Do $N$ Vectors Span $\mathbb{R}^N$?

In general, linearly independent vectors have a relatively "large" span

- No vector is redundant, so each contributes to the span

This helps explain the following fact:

Let $X := \{ {\bf x}_1, \ldots, {\bf x}_N \}$ be any $N$ vectors in $\mathbb{R}^N$

```{admonition} Fact
:class: important

$\mathrm{span}(X) = \mathbb{R}^N$ if and only if $X$ is linearly independent
```

```{admonition} Example
:class: tip

The vectors ${\bf x} = (1, 2)$ and ${\bf y} = (-5, 3)$ span $\mathbb{R}^2$
```

- We already showed $\{{\bf x}, {\bf y}\}$ is linearly independent

Let's start with the proof that 

$X= \{ {\bf x}_1, \ldots, {\bf x}_N \}$ linearly independent $\implies$ $\mathrm{span}(X) = \mathbb{R}^N$

Seeking a contradiction, suppose that 

1. $X $ is linearly independent 
9. and yet $\exists \, {\bf z} \in \mathbb{R}^N$ with ${\bf z} \notin \mathrm{span}(X)$ 

But then $X \cup \{{\bf z}\} \subset \mathbb{R}^N$ is linearly independent (why?)

This set has $N+1$ elements 

And yet $\mathbb{R}^N$ is spanned by the $N$ canonical basis vectors

Contradiction (of what?)

Next let's show the converse

$\mathrm{span}(X) = \mathbb{R}^N$
$\implies$ 
$X= \{ {\bf x}_1, \ldots, {\bf x}_N \}$ linearly independent

Seeking a contradiction, suppose that 

1. $\mathrm{span}(X) = \mathbb{R}^N$ 
9. and yet $X$ is linearly dependent 

Since $X$ not independent, $\exists X_0 \subsetneq X$ with $\mathrm{span}(X_0) =
\mathrm{span}(X)$

But by 1 this implies that $\mathbb{R}^N$ is spanned by $K < N$ vectors

But then the $N$ canonical basis vectors must be linearly dependent

Contradiction 

## Bases

### Bases

Let $S$ be a linear subspace of $\mathbb{R}^N$ 

A set of vectors $B := \{{\bf b}_1, \ldots, {\bf b}_K\} \subset S$ is
called a ***basis of $S$*** if
%
1. $B$ is linearly independent
9. $\mathrm{span}(B) = S$

```{admonition} Example
:class: tip

Canonical basis vectors form a basis of $\mathbb{R}^N$
```

Indeed, if $E := \{{\bf e}_1, \ldots, {\bf e}_N\} \subset \mathbb{R}^N$, then

- $E$ is linearly independent -- we showed this earlier

- $\mathrm{span}(E) = \mathbb{R}^N$ -- we showed this earlier

```{admonition} Example
:class: tip

Recall the plane
%
$$
%
P := \{ (x_1, x_2, 0) \in \mathbb{R}^3 \colon x_1, x_2 \in \mathbb{R \}}
%
$$
%

We showed before that $\mathrm{span}\{{\bf e}_1, {\bf e}_2\} = P$ for 

%
$$
%
{\bf e}_1 := 
\left(
\begin{array}{c}
1 \\
0 \\
0
\end{array}
\right),
\quad 
{\bf e}_2 := 
\left(
\begin{array}{c}
0 \\
1 \\
0
\end{array}
\right)
%
$$
%

Moreover, $\{{\bf e}_1, {\bf e}_2\}$ is linearly independent (why?)

Hence $\{{\bf e}_1, {\bf e}_2\}$ is a basis for $P$

```

```{figure} _static/plots/flat_plane_e_vecs.png
:name: 

The pair $\{{\bf e}_1, {\bf e}_2\}$ form a basis for $P$
```

What are the implications of $B$ being a basis of $S$?

In short, every element of $S$ can be represented uniquely from the
smaller set $B$

In more detail:

- $B$ spans $S$ and, by linear independence, every element is
needed to span $S$ --- a "minimal" spanning set

- Since $B$ spans $S$, every ${\bf y}$ in $S$ can be represented as
a linear combination of the basis vectors

- By independence, this representation is unique

It's obvious given the definition that

```{admonition} Fact
:class: important

If $B \subset \mathbb{R}^N$ is linearly independent, then $B$ is a basis of
```
$\mathrm{span}(B)$

```{admonition} Example
:class: tip

Let $B := \{{\bf x}_1, {\bf x}_2\}$ where 
```

%
$$
%
{\bf x}_1 =
\begin{pmatrix}
3 \\
4 \\
2
\end{pmatrix}
\quad \text{and} \quad
{\bf x}_2 =
\begin{pmatrix}
3 \\
-4 \\
1
\end{pmatrix}
%
$$
%

We saw earlier that 

- $S := \mathrm{span}(B)$ is the plane in $\mathbb{R}^3$ passing through
${\bf x}_1$, ${\bf x}_2$ and ${\bf 0}$
- $B$ is linearly independent in $\mathbb{R}^3$ (dropping either reduces span)

Hence $B$ is a basis for the plane $S$ 

```{figure} _static/plots/nonredundant1.png
:name: 

The pair $\{{\bf x}_1, {\bf x}_2\}$ is a basis of its span
```

### Fundamental Properties of Bases

```{admonition} Fact
:class: important

If $S$ is a linear subspace of $\mathbb{R}^N$ distinct from $\{{\bf 0}\}$, then 
```
%
1. $S$ has at least one basis, and
9. every basis of $S$ has the same number of elements

Proof of part 2: Let $B_i$ be a basis of $S$ with $K_i$ elements, $i=1, 2$

By definition, $B_2$ is a linearly independent subset of $S$

Moreover, $S$ is spanned by the set $B_1$, which has $K_1$ elements

Hence $K_2 \leq K_1$ 

Reversing the roles of $B_1$ and $B_2$ gives $K_1 \leq K_2$

### Dimension

Let $S$ be a linear subspace of $\mathbb{R}^N$

We now know that every basis of $S$ has the same number of elements

This common number is called the ***dimension*** of $S$

```{admonition} Example
:class: tip

$\mathbb{R}^N$ is $N$ dimensional because the $N$ canonical basis vectors
```
form a basis

```{admonition} Example
:class: tip

$P := \{ (x_1, x_2, 0) \in \mathbb{R}^3 \colon x_1, x_2 \in \mathbb{R \}}$ is
```
two dimensional because the first two canonical basis vectors
of $\mathbb{R}^3$ form a basis 

```{admonition} Example
:class: tip

In $\mathbb{R}^3$, a line through the origin is one-dimensional, while a
```
plane through the origin is two-dimensional

### Dimension of Spans

```{admonition} Fact
:class: important

Let $X := \{{\bf x}_1,\ldots,{\bf x}_K\} \subset \mathbb{R}^N$ 
```

The following statements are true:
%
1. $\mathrm{dim}(\mathrm{span}(X)) \leq K$
9. $\mathrm{dim}(\mathrm{span}(X)) = K$ $\;\iff\;$ $X$ is linearly independent
%

Proof that $\mathrm{dim}(\mathrm{span}(X)) \leq K$

If not then $\mathrm{span}(X)$ has a basis with $M > K$ elements

Hence $\mathrm{span}(X)$ contains $M > K$ linearly independent vectors

This is impossible, given that $\mathrm{span}(X)$ is spanned by $K$ vectors

Now consider the second claim: 

-[1.] $X$ is linearly independent $\implies$ $\dim(\mathrm{span}(X)) = K$ 

Proof: True because the vectors ${\bf x}_1,\ldots,{\bf x}_K$ form
a basis of $\mathrm{span}(X)$

-[2.] $\mathrm{dim}(\mathrm{span}(X)) = K$ $\implies$ $X$ linearly independent

Proof: If not then $\exists \, X_0 \subsetneq X$ such that $\mathrm{span}(X_0) = \mathrm{span}(X)$

By this equality and part 1 of the theorem, 
%
$$\dim(\mathrm{span}(X)) = \dim(\mathrm{span}(X_0)) \leq \# X_0 \leq K - 1$$
%

Contradiction

```{admonition} Fact
:class: important

If $S$ a linear subspace of $\mathbb{R}^N$, then 
```
%
$$
%
\dim(S) = N \; \iff \; S = \mathbb{R}^N
%
$$
%

Useful implications

- The only $N$-dimensional subspace of $\mathbb{R}^N$ is $\mathbb{R}^N$
- To show $S = \mathbb{R}^N$ just need to show that $\dim(S) = N$ 

Proof: See course notes

### Linear Maps

In this section we investigate one of the most important classes of
functions

These are the so-called linear functions

Linear functions play a fundamental role in all fields of science

- In one-to-one correspondence with matrices

Even nonlinear functions can often be rewritten as partially linear

The properties of linear functions are closely tied to notions such as 

- linear combinations, span
- linear independence, bases, etc.

### Linearity

A function $T \colon \mathbb{R}^K \to \mathbb{R}^N$ is called
***linear*** if 
%
$$
%
T(\alpha {\bf x} + \beta {\bf y}) = \alpha T{\bf x} + \beta T{\bf y}
\qquad
\forall \, 
{\bf x}, {\bf y} \in \mathbb{R}^K, \;
\forall \,
\alpha, \beta \in \mathbb{R}
%
$$
%

Notation: 

- Linear functions often written with upper case letters

- Typically omit parenthesis around arguments when convenient

```{admonition} Example
:class: tip

$T \colon \mathbb{R} \to \mathbb{R}$ defined by $Tx = 2x$ is linear 
```

Proof: Take any $\alpha, \beta, x, y$ in $\mathbb{R}$ and observe that
%
$$
%
T(\alpha x + \beta y)
= 2(\alpha x + \beta y)
= \alpha 2 x + \beta 2 y
= \alpha Tx + \beta Ty 
%
$$
%

```{admonition} Example
:class: tip

The function $f \colon \mathbb{R} \to \mathbb{R}$ defined by $f(x) = x^2$ is
```
***non***linear

Proof: Set $\alpha = \beta = x = y = 1$

Then 
%
- $f(\alpha x + \beta y) = f(2) = 4$
- But $\alpha f(x) + \beta f(y) = 1 + 1 = 2$

```{admonition} Example
:class: tip

Given constants $c_1$ and $c_2$, the 
function $T \colon \mathbb{R}^2 \to \mathbb{R}$ defined by 
%
$$
%
T {\bf x} = T (x_1, x_2) = c_1 x_1 + c_2 x_2 
%
$$
%
is linear 

```

Proof: If we take any $\alpha, \beta$ in $\mathbb{R}$ and
${\bf x}, {\bf y}$ in $\mathbb{R}^2$, then 
%
$$
%
T(\alpha {\bf x} + \beta {\bf y})
= c_1 [\alpha x_1 + \beta y_1] + c_2 [\alpha x_2 + \beta y_2]
\\
= \alpha [c_1 x_1 + c_2 x_2] + \beta [c_1 y_1 + c_2 y_2]
\\
= \alpha T {\bf x} + \beta T {\bf y} 
%
$$
%

```{figure} _static/plots/linfunc.png
:name: 

The graph of $T {\bf x} = c_1 x_1 + c_2 x_2$ is a plane
through the origin
```

Remark: Thinking of linear functions as those whose graph is a straight
line is not correct

```{admonition} Example
:class: tip

Function $f \colon \mathbb{R} \to \mathbb{R}$ defined by $f(x) = 1 + 2x$ is
***non***linear

Proof: Take $\alpha = \beta = x = y = 1$

Then 

- $f(\alpha x + \beta y) = f(2) = 5$
- But $\alpha f(x) + \beta f(y) = 3 + 3 = 6$

```

This kind of function is called an ***affine*** function

Let ${\bf a}_1, \ldots, {\bf a}_K$ be vectors in $\mathbb{R}^N$

Let $T \colon \mathbb{R}^K \to \mathbb{R}^N$ be defined by 
%
$$
%
T{\bf x} 
=
T
\begin{pmatrix}
x_1 \\
\vdots \\
x_K
\end{pmatrix}
=
x_1 {\bf a}_1 + \ldots + x_K {\bf a}_K
%
$$
%

**Exercise:** Show that this function is linear

Remarks
%
- This is a generalization of the previous linear examples 
- In a sense it is the most general representation of a linear map
from $\mathbb{R}^K$ to $\mathbb{R}^N$
- It is also "the same" as the $N \times K$ matrix with
columns ${\bf a}_1, \ldots, {\bf a}_K$ --- more on this later

### Implications of Linearity 

```{admonition} Fact
:class: important

If $T \colon \mathbb{R}^K \to \mathbb{R}^N$ is a linear map and ${\bf x}_1,
```
\ldots, {\bf x}_J$ are vectors in $\mathbb{R}^K$, then
for any linear combination we have
%
$$
%
T
\left[ \alpha_1 {\bf x}_1 + \cdots + \alpha_J {\bf x}_J \right]
= \alpha_1 T {\bf x}_1 + \cdots + \alpha_J T {\bf x}_J
%
$$
%

Proof for $J=3$: Applying the def of linearity twice, 
%
$$
%
T
\left[ \alpha_1 {\bf x}_1 + \alpha_2 {\bf x}_2 + \alpha_3 {\bf x}_3 \right]
= T\left[ (\alpha_1 {\bf x}_1 + \alpha_2 {\bf x}_2) + \alpha_3 {\bf x}_3 \right]
\\
= T\left[ \alpha_1 {\bf x}_1 + \alpha_2 {\bf x}_2 \right] + \alpha_3 T {\bf x}_3 
\\
= \alpha_1 T {\bf x}_1 + \alpha_2 T {\bf x}_2 + \alpha_3 T {\bf x}_3 
%
$$
%

**Exercise:** Show that if $T$ is any linear function then $T{\bf 0} = {\bf 0}$

```{admonition} Fact
:class: important

If $T \colon \mathbb{R}^K \to \mathbb{R}^N$ is a linear map, then 
```
%
$$
%
\mathrm{rng}(T) = \mathrm{span}(V) 
\quad \text{where} \quad
V := \{T{\bf e}_1, \ldots, T{\bf e}_K\}
%
$$
%

- Here ${\bf e}_k$ is the $k$-th canonical basis vector in $\mathbb{R}^K$

Proof: Any ${\bf x} \in \mathbb{R}^K$ can be expressed as $\sum_{k=1}^K \alpha_k {\bf e}_k$

Hence $\mathrm{rng}(T)$ is the set of all points of the form
%
$$
%
T{\bf x}
= T \left[ \sum_{k=1}^K \alpha_k {\bf e}_k \right]
= \sum_{k=1}^K \alpha_k T {\bf e}_k 
%
$$
%
as we vary $\alpha_1, \ldots, \alpha_K$ over all combinations

This coincides with the definition of $\mathrm{span}(V)$

```{admonition} Example
:class: tip

Let $T \colon \mathbb{R}^2 \to \mathbb{R}^2$ be defined by 
%
$$
%
T{\bf x} 
=
T(x_1, x_2)
=
x_1 
\begin{pmatrix}
1 \\
2
\end{pmatrix}
+
x_2 
\begin{pmatrix}
0 \\
-2
\end{pmatrix}
%
$$
%

Then 
%
$$
%
T{\bf e}_1
=
\begin{pmatrix}
1 \\
2
\end{pmatrix}
\quad \text{and} \quad
T{\bf e}_2
=
\begin{pmatrix}
0 \\
-2
\end{pmatrix}
%
$$
%

**Exercise:** Show that $V := \{T{\bf e}_1, T{\bf e}_2\}$ is linearly independent

We conclude that the range of $T$ is all of $\mathbb{R}^2$ (why?)

```

The ***null space*** or ***kernel*** of linear map $T \colon \mathbb{R}^K \to
\mathbb{R}^N$ is
%
$$
%
\mathrm{kernel}(T) := \{ {\bf x} \in \mathbb{R}^K \colon T{\bf x \} = {\bf 0}}
%
$$
%

**Exercise:** Show that $\mathrm{kernel}(T)$ is a linear subspace of $\mathbb{R}^K$

```{admonition} Fact
:class: important

$\mathrm{kernel}(T) = \{{\bf 0}\}$ if and only if $T$ is one-to-one
```

Proof of $\implies$: Suppose that $T{\bf x} = T{\bf y}$ for arbitrary ${\bf x}, {\bf y} \in \mathbb{R}^K$

Then ${\bf 0} = T{\bf x} - T{\bf y} = T({\bf x} - {\bf y})$

In other words, ${\bf x} - {\bf y} \in \mathrm{kernel}(T)$

Hence $\mathrm{kernel}(T) = \{{\bf 0}\}$ $\implies$ ${\bf x} = {\bf y}$

### Linearity and Bijections

Many scientific and practical problems are "inverse" problems

- We observe outcomes but not what caused them
- How can we work backwards from outcomes to causes?

Examples

- What consumer preferences generated observed market behavior?
- What kinds of expectations led to given shift in exchange rates?

Loosely, we can express an inverse problem as

```{figure} _static/plots/inverse_prob.png
:name: 

```

- Does this problem have a solution?
- Is it unique?

Answers depend on whether $F$ is one-to-one, onto, etc.

The best case is a bijection

But other situations also arise

Recall that an arbitrary function can be 

- one-to-one
- onto
- both (a bijection)
- neither 

For linear functions from $\mathbb{R}^N$ to $\mathbb{R}^N$, the first three are all
equivalent!

In particular, 
%
$$
%
\text{onto } \iff \text{ one-to-one } \iff \text{ bijection}
%
$$
%

The next theorem summarizes

```{admonition} Fact
:class: important

If $T$ is a linear function from $\mathbb{R}^N$ to $\mathbb{R}^N$ then all of the
```
following are equivalent:
%
1. $T$ is a bijection
- $T$ is onto
- $T$ is one-to-one
- $\mathrm{kernel}(T) = \{ {\bf 0} \}$
- The set of vectors $V := \{T{\bf e}_1, \ldots, T{\bf e}_N\}$ is
linearly independent

If any one of these equivalent conditions is true, then $T$ is called
***nonsingular***

- Don't forget: We are talking about $\mathbb{R}^N$ to $\mathbb{R}^N$ here

```{figure} _static/plots/linbijec.png
:name: 

The case of $N=1$, nonsingular and singular
```

Proof that $T$ onto $\iff$ $V := \{T{\bf e}_1, \ldots, T{\bf e}_N\}$ is
linearly independent

Recall that for any linear map $T$ we have $\mathrm{rng}(T) = \mathrm{span}(V)$

Using this fact and the definitions,
%
$$
%
T \text{ onto } 
& \iff \mathrm{rng}(T) = \mathbb{R}^N
\\
& \iff \mathrm{span}(V) = \mathbb{R}^N
\\
& \iff V \text{ is linearly indepenent}
%
$$
%

(We saw that $N$ vectors span $\mathbb{R}^N$ iff linearly indepenent)

Rest of proof: Solved exercises

```{admonition} Fact
:class: important

If $T \colon \mathbb{R}^N \to \mathbb{R}^N$ is nonsingular then so is $T^{-1}$. 
```

What is the implication here?

If $T$ is a bijection then so is $T^{-1}$

Hence the only real claim is that $T^{-1}$ is also linear

The proof is an exercise...

### Maps Across Different Dimensions 

Remember that these results apply to maps from $\mathbb{R}^N$ to $\mathbb{R}^N$

Things change when we look at linear maps across dimensions

The general rules for linear maps are 

- Maps from lower to higher dimensions cannot be onto
- Maps from higher to lower dimensions cannot be one-to-one

In either case they cannot be bijections

The next fact summarizes

```{admonition} Fact
:class: important

For a linear map $T$ from $\mathbb{R}^K \to \mathbb{R}^N$, the following statements are
```
true:
%
1. If $K < N$ then $T$ is not onto
9. If $K > N$ then $T$ is not one-to-one
%

Proof of part 1: Let $K < N$ and let $T \colon \mathbb{R}^K \to \mathbb{R}^N$ be linear 

Letting $V := \{T{\bf e}_1, \ldots, T{\bf e}_K\}$, we have
%
$$
%
\dim(\mathrm{rng}(T)) = \dim(\mathrm{span}(V)) \leq K < N
%
$$
%
$$
%
\text{ therefore } 
\mathrm{rng}(T) \ne \mathbb{R}^N
%
$$
%

Hence $T$ is not onto 

Proof of part 2: $K > N$ $\implies$ $T$ is not one-to-one

Suppose to the contrary that $T$ is one-to-one

Let $\alpha_1, \ldots, \alpha_K$ be a collection of vectors such that 
%
$$
%
\alpha_1 T {\bf e}_1 + \cdots + \alpha_K T {\bf e}_K = {\bf 0}
%
$$
%
$$
%
\text{ therefore } 
T (\alpha_1 {\bf e}_1 + \cdots + \alpha_K {\bf e}_K) = {\bf 0}
\qquad (\text{by linearity})
%
$$
%
$$
%
\text{ therefore }
\alpha_1 {\bf e}_1 + \cdots + \alpha_K {\bf e}_K = {\bf 0}
\qquad (\text{since $\ker(T) = \{{\bf 0}\}$})
%
$$
%
$$
%
\text{ therefore } 
\alpha_1 = \cdots = \alpha_K = 0
\qquad (\text{by independence of $\{{\bf e}_1, \ldots {\bf e}_K\}$)}
%
$$
%

We have shown that $\{T{\bf e}_1, \ldots, T{\bf e}_K\}$ is linearly
independent

But then $\mathbb{R}^N$ contains a linearly independent set
with $K > N$ vectors --- contradiction

```{figure} _static/plots/cost_min_2.png
:name: 

```

```{admonition} Example
:class: tip

Cost function $c(k, \ell) = rk + w\ell$ cannot be one-to-one
```

## Matrices

### Matrices and Linear Equations

We now begin our study of matrices

As we'll see, there's an isomorphic relationship between 
%
1. matrices 
9. linear maps

Often properties of matrices are best understood via those of linear maps

### Matrices

Typical ***$N \times K$ matrix***: 

%
$$
%
{\bf A} = 
\left(
\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1K} \\
a_{21} & a_{22} & \cdots & a_{2K} \\
\vdots & \vdots & & \vdots \\
a_{N1} & a_{N2} & \cdots & a_{NK} 
\end{array}
\right)
%
$$
%

Symbol $a_{nk}$ stands for element in the 
%
- $n$-th row 
- $k$-th column

Often matrices correspond to coefficients of a linear equation

%
$$
%
\begin{array}{c}
a_{11} x_1 + a_{12} x_2 + \cdots + a_{1K} x_K = b_1 \\
a_{21} x_1 + a_{22} x_2 + \cdots + a_{2K} x_K = b_2 \\
\vdots \\
a_{N1} x_1 + a_{N2} x_2 + \cdots + a_{NK} x_K = b_N 
\end{array}
%
$$
%

Given the $a_{nm}$ and $b_n$, what values of $x_1, \ldots, x_K$ solve this
system?

We now investigate this and other related questions

But first some background on matrices...

An $N \times K$ matrix also called a 
%
- ***row vector*** if $N = 1$

- ***column vector*** if $K = 1$

\Egs

%
$$
%
{\bf b} 
= 
\begin{pmatrix}
b_1 \\
\vdots \\
b_N 
\end{pmatrix}
\text{ is }\; N \times 1,
\qquad
{\bf c} 
= 
\begin{pmatrix}
c_1 \cdots c_K 
\end{pmatrix}
\text{ is }\; 
1 \times K
%
$$
%

If $N = K$, then ${\bf A}$ is called ***square***

We use 

- $\mathrm{col}_k({\bf A})$ to denote the $k$-th column of ${\bf A}$
- $\mathrm{row}_n({\bf A})$ to denote the $n$-th row of ${\bf A}$

Example

%
$$
%
\mathrm{col}_1({\bf A})
=
\mathrm{col}_1
\left(
\begin{array}{ccc}
***a_{11***} & \cdots & a_{1K} \\
***a_{21***} & \cdots & a_{2K} \\
\vdots & \vdots & \vdots \\
***a_{N1***} & \cdots & a_{NK} 
\end{array}
\right)
=
\left(
\begin{array}{c}
a_{11} \\
a_{21} \\
\vdots \\
a_{N1} 
\end{array}
\right)
%
$$
%

The ***zero matrix*** is
%
$$
%
{\bf 0} := 
\left(
\begin{array}{cccc}
0 & 0 & \cdots & 0 \\
0 & 0 & \cdots & 0 \\
\vdots & \vdots & & \vdots \\
0 & 0 & \cdots & 0 \\
\end{array}
\right)
%
$$
%

The ***identity matrix*** is
%
$$
%
{\bf I} := 
\left(
\begin{array}{cccc}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & & \vdots \\
0 & 0 & \cdots & 1 \\
\end{array}
\right)
%
$$
%

### Algebraic Operations for Matrices

Addition and scalar multiplication are also defined for matrices

Both are element by element, as in the vector case

Scalar multiplication:

%
$$
%
\gamma 
\left(
\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1K} \\
a_{21} & a_{22} & \cdots & a_{2K} \\
\vdots & \vdots & & \vdots \\
a_{N1} & a_{N2} & \cdots & a_{NK} \\
\end{array}
\right)
:=
\left(
\begin{array}{cccc}
\gamma a_{11} & \gamma a_{12} & \cdots & \gamma a_{1K} \\
\gamma a_{21} & \gamma a_{22} & \cdots & \gamma a_{2K} \\
\vdots & \vdots & & \vdots \\
\gamma a_{N1} & \gamma a_{N2} & \cdots & \gamma a_{NK} \\
\end{array}
\right)
%
$$
%

Addition:
% 
%
$$
%
\left(
\begin{array}{ccc}
a_{11} & \cdots & a_{1K} \\
a_{21} & \cdots & a_{2K} \\
\vdots & \vdots & \vdots \\
a_{N1} & \cdots & a_{NK} \\
\end{array}
\right)
+
\left(
\begin{array}{ccc}
b_{11} & \cdots & b_{1K} \\
b_{21} & \cdots & b_{2K} \\
\vdots & \vdots & \vdots \\
b_{N1} & \cdots & b_{NK} \\
\end{array}
\right)
\\
:=
\left(
\begin{array}{ccc}
a_{11} + b_{11} & \cdots & a_{1K} + b_{1K} \\
a_{21} + b_{21} & \cdots & a_{2K} + b_{2K} \\
\vdots & \vdots & \vdots \\
a_{N1} + b_{N1} & \cdots & a_{NK} + b_{NK} \\
\end{array}
\right)
%
$$
%

Note that matrices must be same dimension

Multiplication of matrices: 

Product ${\bf A} {\bf B}$: 
$i,j$-th element is inner product of $i$-th row of ${\bf A}$ and 
$j$-th column of ${\bf B}$ 

%
$$
%
\left(
\begin{array}{ccc}
***a_{11***} & ***\cdots*** & ***a_{1K***} \\
a_{21} & \cdots & a_{2K} \\
\vdots & \vdots & \vdots \\
a_{N1} & \cdots & a_{NK} \\
\end{array}
\right)
\left(
\begin{array}{ccc}
***b_{11***} & \cdots & b_{1J} \\
***b_{21***} & \cdots & b_{2J} \\
***\vdots*** & \vdots & \vdots \\
***b_{K1***} & \cdots & b_{KJ} \\
\end{array}
\right)
=
\left(
\begin{array}{ccc}
***c_{11***} & \cdots & c_{1J} \\
c_{21} & \cdots & c_{2J} \\
\vdots & \vdots & \vdots \\
c_{N1} & \cdots & c_{NJ} \\
\end{array}
\right)
%
$$
%

In this display, 
%
$$
%
c_{11} = \sum_{k=1}^K a_{1k} b_{k1}
%
$$
%

Suppose ${\bf A}$ is $N \times K$ and ${\bf B}$ is $J \times M$

- ${\bf A} {\bf B}$ defined only if $K = J$
- Resulting matrix ${\bf A} {\bf B}$ is $N \times M$

The rule to remember:
%
$$
%
\text{product of } N \times K \text{ and } K \times M
\text{ is } N \times M
%
$$
%

Important: Multiplication is not commutative

In particular, it is not in general true that ${\bf A} {\bf B} = {\bf B} {\bf A}$ 

- In fact ${\bf B} {\bf A}$ is not well-defined unless $N = M$ also holds 

Useful observation:

%
$$
%
{\bf A} {\bf x}
= 
\left(
\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1K} \\
a_{21} & a_{22} & \cdots & a_{2K} \\
\vdots & \vdots & & \vdots \\
a_{N1} & a_{N2} & \cdots & a_{NK} 
\end{array}
\right)
\left(
\begin{array}{c}
x_1 \\
x_2 \\
\vdots \\
x_K
\end{array}
\right)
\\
=
x_1 \left(
\begin{array}{c}
a_{11} \\
a_{21} \\
\vdots \\
a_{N1} 
\end{array}
\right)
+
x_2 \left(
\begin{array}{c}
a_{12} \\
a_{22} \\
\vdots \\
a_{N2} 
\end{array}
\right)
+ \cdots + 
x_K \left(
\begin{array}{c}
a_{1K} \\
a_{2K} \\
\vdots \\
a_{NK} 
\end{array}
\right)
\\
= 
\sum_{k=1}^K x_k \mathrm{col}_k({\bf A})
%
$$
%

Rules for multiplication:

```{admonition} Fact
:class: important

Given scalar $\alpha$ and conformable ${\bf A}$, ${\bf B}$ and ${\bf C}$, we have
```

1. ${\bf A} ({\bf B} {\bf C}) = ({\bf A} {\bf B}) {\bf C}$

- ${\bf A} ({\bf B} + {\bf C}) = {\bf A} {\bf B} + {\bf A} {\bf C}$

- $({\bf A} + {\bf B}) {\bf C} = {\bf A} {\bf C} + {\bf B} {\bf C}$

9. ${\bf A} \alpha {\bf B} = \alpha {\bf A} {\bf B}$

(Here ``conformable'' means operation makes sense)

The ***$k$-th power*** of a square matrix ${\bf A}$ is 

%
$$ {\bf A}^k := \underbrace{{\bf A} \cdots {\bf A}}_{k \text{ terms}} $$
%

If it exists, the ***square root*** of ${\bf A}$ is written ${\bf A}^{1/2}$ 

Defined as the matrix ${\bf B}$ such that ${\bf B}^2$ is ${\bf A}$

More on these later...

In matrix multiplication, ${\bf I}$ is the multiplicative unit

That is, assuming conformability, we always have
%
$$
%
{\bf A} {\bf I} = {\bf I} {\bf A} = {\bf A}
%
$$
%

**Exercise:** Check it using the definition of matrix multiplication

Note: If ${\bf I}$ is $K \times K$, then
%
$$
%
\mathrm{col}_k({\bf I})
= {\bf e}_k
= \text{ $k$-th canonical basis vector in } \mathbb{R}^K
%
$$
%


```{code-cell} python3
:tags: [hide/remote-cell/input/output]
---
mystnb:
image:
width: 80%
align: center
---
tags:
- hide-input
- remove-output

In [1]: import numpy as np

In [2]: A = [[2, 4],
...: [4, 2]]

In [3]: A = np.array(A) # Convert A to array

In [4]: B = np.identity(2)

In [5]: B
Out[5]: 
array([[ 1., 0.],
[ 0., 1.]])

```
-->


```{code-cell} python3
:tags: [hide/remote-cell/input/output]
---
mystnb:
image:
width: 80%
align: center
---
tags:
- hide-input
- remove-output

In [6]: A + B # Matrix addition
Out[6]: 
array([[ 3., 4.],
[ 4., 3.]])

In [7]: np.dot(A, B) # Matrix multiplication
Out[7]: 
array([[ 2., 4.],
[ 4., 2.]])

```
-->

## Matrices as Maps

### Matrices as Maps

Any $N \times K$ matrix ${\bf A}$ can be thought of as a function
${\bf x} \mapsto {\bf A} {\bf x}$
%
- In ${\bf A} {\bf x}$ the ${\bf x}$ is understood to be
a column vector

It turns out that every such map is linear

To see this fix $N \times K$ matrix ${\bf A}$ and let $T$ be defined by
%
$$
%
T \colon \mathbb{R}^K \to \mathbb{R}^N, 
\qquad
T{\bf x} = {\bf A} {\bf x}
%
$$
%

Pick any ${\bf x}$, ${\bf y}$ in $\mathbb{R}^K$, and any scalars $\alpha$ and $\beta$

The rules of matrix arithmetic tell us that
%
$$
%
T(\alpha {\bf x} + \beta {\bf y}) 
:= {\bf A} (\alpha {\bf x} + \beta {\bf y})
= \alpha {\bf A} {\bf x} + \beta {\bf A} {\bf y}
=: \alpha T{\bf x} + \beta T{\bf y} 
%
$$
%

So matrices make linear functions

How about examples of linear functions that don't involve matrices? 

Actually there are none!

```{admonition} Fact
:class: important

If $T \colon \mathbb{R}^K \to \mathbb{R}^N$ then 
```
%
$$
%
T \text{ is linear }
\; \iff \;
\exists \; N \times K \text{ matrix } {\bf A} \text{ such that } T{\bf x} = {\bf A} {\bf x}, 
\;\forall \, {\bf x} \in \mathbb{R}^K
%
$$
%

- On the last slide we showed the $\Longleftarrow$ part

- On the next slide we show the $\implies$ part

Let $T \colon \mathbb{R}^K \to \mathbb{R}^N$ be linear

We aim to construct an $N \times K$ matrix ${\bf A}$ such that
%
$$ T{\bf x} = {\bf A} {\bf x}, \qquad \forall \, {\bf x} \in \mathbb{R}^K $$
%

As usual, let
${\bf e}_k$ be the $k$-th canonical basis vector in $\mathbb{R}^K$

Define a matrix ${\bf A}$ by $\mathrm{col}_k({\bf A}) = T{\bf e}_k$

Pick any ${\bf x} = (x_1, \ldots, x_K) \in \mathbb{R}^K$

By linearity we have 
%
$$
%
T{\bf x} 
= T \left[\sum_{k=1}^K x_k {\bf e}_k \right]
= \sum_{k=1}^K x_k T {\bf e}_k
= \sum_{k=1}^K x_k \mathrm{col}_k({\bf A})
= {\bf A} {\bf x}
%
$$
%

### Matrix Product as Composition

Let

- ${\bf A}$ be $N \times K$ and ${\bf B}$ be $K \times M$
- $T \colon \mathbb{R}^K \to \mathbb{R}^N$ be the linear map $T{\bf x} = {\bf A}{\bf x}$ 
- $U \colon \mathbb{R}^M \to \mathbb{R}^K$ be the linear map $U{\bf x} = {\bf B}{\bf x}$ 

The matrix product ${\bf A} {\bf B}$ corresponds exactly to the
***composition*** of $T$ and $U$ 

Proof:
%
$$
%
(T \circ U) ({\bf x})
= T( U{\bf x})
= T( {\bf B} {\bf x})
= {\bf A} {\bf B} {\bf x}
%
$$
%

This helps us understand a few things

For example, let
%
- ${\bf A}$ be $N \times K$ and ${\bf B}$ be $J \times M$
- $T \colon \mathbb{R}^K \to \mathbb{R}^N$ be the linear map $T{\bf x} = {\bf A}{\bf x}$ 
- $U \colon \mathbb{R}^M \to \mathbb{R}^J$ be the linear map $U{\bf x} = {\bf B}{\bf x}$ 

Then ${\bf A} {\bf B}$ is only defined when $K = J$

This is because ${\bf A} {\bf B}$ corresponds to $T \circ U$

But for $T \circ U$ to be well defined we need $K = J$

Then $U$ maps $\mathbb{R}^M$ to $\mathbb{R}^K$ and $T$ maps $\mathbb{R}^K$ to $\mathbb{R}^N$

## Rank

### Column Space

Let ${\bf A}$ be an $N \times K$ matrix

The ***column space*** of ${\bf A}$ is defined as the span of its columns
%
$$
%
\mathrm{span}({\bf A}) 
= \mathrm{span} \{ \mathrm{col}_1 ({\bf A}), \ldots, \mathrm{col}_K({\bf A}) \}
\\
= \text{all vectors of the form } \sum_{k=1}^K x_k \mathrm{col}_k({\bf A})
%
$$
%

Equivalently,
%
$$
%
\mathrm{span}({\bf A}) := \{ {\bf A \colon \bf x \}}{ {\bf x} \in \mathbb{R}^K}
%
$$
%

This is exactly the range of the associated linear map
%

$T \colon \mathbb{R}^K \to \mathbb{R}^N$ defined by $T {\bf x} = {\bf A} {\bf x}$

```{admonition} Example
:class: tip

If
```
%
$$
%
{\bf A} =
\begin{pmatrix}
1 & -5 \\
2 & 3
\end{pmatrix}
%
$$
%

then the span is all linear combinations
%
$$
%
x_1
\left(
\begin{array}{c}
1 \\
2
\end{array}
\right)
+ 
x_2
\left(
\begin{array}{c}
-5 \\
3
\end{array}
\right)
\quad
\text{where}
\quad
(x_1, x_2) \in \mathbb{R}^2
%
$$
%

These columns are linearly independent (shown earlier)

Hence the column space is all of $\mathbb{R}^2$ (why?)

**Exercise:** Show that the column space of any $N \times K$ matrix is a linear
subspace of $\mathbb{R}^N$

### Rank

Equivalent questions
%
- How large is the range of the linear map $T {\bf x} = {\bf A} {\bf x}$?
- How large is the column space of ${\bf A}$?

The obvious measure of size for a linear subspace is its dimension

The dimension of $\mathrm{span}({\bf A})$ is known as the ***rank*** of ${\bf A}$ 
%
$$
%
\mathrm{rank}({\bf A}) := \mathrm{dim}(\mathrm{span}({\bf A}))
%
$$
%

Because $\mathrm{span}({\bf A})$ is the span of $K$ vectors, we have
%
$$
%
\mathrm{rank}({\bf A}) = \mathrm{dim}(\mathrm{span}({\bf A})) \leq K
%
$$
%

${\bf A}$ is said to have ***full column rank*** if 
%
$$
%
\mathrm{rank}({\bf A}) = \text{ number of columns of } {\bf A}
%
$$
%

```{admonition} Fact
:class: important

For any matrix ${\bf A}$, the following statements are equivalent:
```
%
1. ${\bf A}$ is of full column rank

- The columns of ${\bf A}$ are linearly independent

9. If ${\bf A} {\bf x} = {\bf 0}$, then ${\bf x} = {\bf 0}$
%

**Exercise:** Check this, recalling that
%
$$
%
\dim(\mathrm{span}\{{\bf a}_1, \ldots, {\bf a}_K\}) = K
\, \iff \,
\{{\bf a}_1, \ldots, {\bf a}_K\} \text{ linearly indepenent}
%
$$
%


```{code-cell} python3
:tags: [hide/remote-cell/input/output]
---
mystnb:
image:
width: 80%
align: center
---
tags:
- hide-input
- remove-output

In [1]: import numpy as np

In [2]: A = [[2.0, 1.0],
...: [6.3, 3.0]]

In [3]: np.linalg.matrix_rank(A)
Out[3]: 2

In [4]: A = [[2.0, 1.0], # Col 2 is half col 1
...: [6.0, 3.0]]

In [5]: np.linalg.matrix_rank(A)
Out[5]: 1

```
-->

### Reminder I

Suppose we want to find the $x$ that solves $f(x) = y$

The ideal case is when $f$ is a bijection

```{figure} _static/plots/function2.png
:name: 

```

Equivalent:
%
- $f$ is a bijection
- each $y \in B$ has a unique preimage
- $f(x) = y$ has a unique solution $x$ for each $y$

### Reminder II

Let $T$ be a linear function from $\mathbb{R}^N$ to $\mathbb{R}^N$ 

We saw that in this case all of the following are equivalent:
%
1. $T$ is a bijection
- $T$ is onto
- $T$ is one-to-one
- $\mathrm{kernel}(T) = \{ {\bf 0} \}$
9. $V := \{T{\bf e}_1, \ldots, T{\bf e}_N\}$ is linearly independent

We then say that $T$ is nonsingular ($=$ linear bijection)

## $N \times N$ Linear Equations

### Linear Equations

Let's look at solving linear equations such as ${\bf A} {\bf x} = {\bf b}$ 

We start with the "best" case: 

number of equations $=$ number of unknowns

Thus, 

- Take $N \times N$ matrix ${\bf A}$ and $N \times 1$ vector ${\bf b}$ as given 
- Search for an $N \times 1$ solution ${\bf x}$

But does such a solution exist? If so is it unique?

The best way to think about this is to consider 
the corresponding linear map
%
$$
%
T \colon \mathbb{R}^N \to \mathbb{R}^N,
\qquad T{\bf x} = {\bf A} {\bf x}
%
$$
%

```{figure} _static/plots/linbijec.png
:name: 

```

Equivalent:
%
1. ${\bf A} {\bf x} = {\bf b}$ has a unique solution ${\bf x}$ for any
given ${\bf b}$
- $T {\bf x} = {\bf b}$ has a unique solution ${\bf x}$ for any
given ${\bf b}$
9. $T$ is a bijection

We already have conditions for linear maps to be bijections

Just need to translate these into the matrix setting

Recall that $T$ called nonsingular if $T$ is a linear bijection

We say that ${\bf A}$ is ***nonsingular*** if $T$ is nonsingular

Equivalent:

- ${\bf x} \mapsto {\bf A} {\bf x}$ is a bijection from $\mathbb{R}^N$ to $\mathbb{R}^N$

We now list equivalent conditions for nonsingularity

Let ${\bf A}$ be an $N \times N$ matrix

```{admonition} Fact
:class: important

All of the following conditions are equivalent
```
%
1. ${\bf A}$ is nonsingular

- The columns of ${\bf A}$ are linearly independent

- $\mathrm{rank}({\bf A}) = N$

- $\mathrm{span}({\bf A}) = \mathbb{R}^N$

- If ${\bf A} {\bf x} = {\bf A} {\bf y}$, then ${\bf x} = {\bf y}$

- If ${\bf A} {\bf x} = {\bf 0}$, then ${\bf x} = {\bf 0}$

- For each ${\bf b} \in \mathbb{R}^N$, the equation ${\bf A} {\bf x} = {\bf b}$
has a solution

- For each ${\bf b} \in \mathbb{R}^N$, the equation ${\bf A} {\bf x} = {\bf b}$
has a unique solution

%

All equivalent ways of saying that $T{\bf x} = {\bf A} {\bf x}$ is a bijection!

```{admonition} Example
:class: tip

For condition 5 the equivalence is
```
% 
%
$$
%
\text{ if ${\bf A} {\bf x} = {\bf A} {\bf y}$,} & \text{ then ${\bf x} = {\bf y}$ }
\\
& \iff \text{ if $T {\bf x} = T {\bf y}$, then ${\bf x} = {\bf y}$ }
\\
&\iff \text{ $T$ is one-to-one }
\\
\text{Since $T$ is a linear map from} & \text{ $\mathbb{R}^N$ to $\mathbb{R}^N$, }
\\
&\iff \text{ $T$ is a bijection }
%
$$
%

```{admonition} Example
:class: tip

For condition 6 the equivalence is
```
% 
%
$$
%
\text{ if ${\bf A} {\bf x} = {\bf 0}$,} & \text{ then ${\bf x} = {\bf 0}$ }
\\
&\iff \{ {\bf x} \colon {\bf A \} {\bf x} = {\bf 0}} =\{ {\bf 0} \}
\\
&\iff \{ {\bf x} \colon T {\bf x \} = {\bf 0}} =\{ {\bf 0} \}
\\
&\iff \ker(T) = \{ {\bf 0} \} 
\\
\text{Since $T$ is a linear map from} & \text{ $\mathbb{R}^N$ to $\mathbb{R}^N$, }
\\
&\iff \text{ $T$ is a bijection }
%
$$
%

```{admonition} Example
:class: tip

For condition 7 the equivalence is 
```

%
$$
%
\text{for each ${\bf b} \in \mathbb{R}^N$, } & \text{the equation ${\bf A} {\bf x} = {\bf b}$
has a solution}
\\
&\iff \text{ every ${\bf b} \in \mathbb{R}^N$ has an ${\bf x}$ such that ${\bf A}{\bf x} = {\bf b}$ }
\\
&\iff \text{ every ${\bf b} \in \mathbb{R}^N$ has an ${\bf x}$ such that $T{\bf x} = {\bf b}$ }
\\
&\iff \text{ $T$ is onto}
\\
\text{Since $T$ is a linear } & \text{map from $\mathbb{R}^N$ to $\mathbb{R}^N$, }
\\
&\iff \text{ $T$ is a bijection }
%
$$
%

Now consider condition 2:

The columns of ${\bf A}$ are linearly independent

Let ${\bf e}_n$ be the $n$-th canonical basis vector in $\mathbb{R}^N$

Observe that ${\bf A} {\bf e}_n = \mathrm{col}_n ({\bf A})$
%

%
$$
%
\text{ therefore } T{\bf e}_n = \mathrm{col}_n ({\bf A})
%
$$
%

%
$$
%
\text{ therefore } 
V := \{T {\bf e}_1, \ldots, T{\bf e}_N\}
= \text{ columns of ${\bf A}$}
%
$$
%

And $V$ is linearly independent if and only if $T$ is a bijection

```{admonition} Example
:class: tip

Consider a one good linear market system 
```
%
$$
%
q = a - b p \qquad (\text{demand}) \\
q = c + d p \qquad (\text{supply})
%
$$
%

Treating $q$ and $p$ as the unknowns, let's write in matrix form as 
%
$$
%
\begin{pmatrix}
1 & b \\
1 & -d
\end{pmatrix}
\begin{pmatrix}
q\\
p
\end{pmatrix}
=
\begin{pmatrix}
a \\
c 
\end{pmatrix}
%
$$
%

A unique solution exists whenever the columns are linearly independent

- means that $(b, -d)$ is not a scalar multiple of ${\bf 1}$
- means that $b \ne -d$ 

```{figure} _static/plots/not_multiple_of_one.png
:name: 

$(b, -d)$ is not a scalar multiple of ${\bf 1}$
```

```{admonition} Example
:class: tip

Recall when we try to solve the system ${\bf A} {\bf x} = {\bf b}$
```
of this form


```{code-cell} python3
:tags: [hide/remote-cell/input/output]
---
mystnb:
image:
width: 80%
align: center
---
tags:
- hide-input
- remove-output

In [1]: import numpy as np
In [2]: from scipy.linalg import solve

In [3]: A = [[0, 2, 4],
...: [1, 4, 8],
...: [0, 3, 6]]

In [4]: b = (1, 2, 0)

In [5]: A, b = np.asarray(A), np.asarray(b)

In [6]: solve(A, b)

```

This is the output that we got

\begin{verbatim}
LinAlgError Traceback (most recent call last)
<ipython-input-8-4fb5f41eaf7c> in <module>()
---- > 1 solve(A, b)
/home/john/anaconda/lib/python2.7/site-packages/scipy/linalg/basic.pyc in solve(a, b, sym_pos, lower, overwrite_a, overwrite_b, debug, check_finite)
97 return x
98 if info > 0:
--- > 99 raise LinAlgError("singular matrix")
100 raise ValueError('illegal value in %d-th argument of internal gesv|posv'
LinAlgError: singular matrix
\end{verbatim}

The problem is that ${\bf A}$ is singular (not nonsingular)

- In particular, $\mathrm{col}_3({\bf A}) = 2 \mathrm{col}_2({\bf A})$

### Inverse Matrices

Given square matrix ${\bf A}$, suppose $\exists$ square matrix ${\bf B}$ such
that 
%
$${\bf A} {\bf B} = {\bf B} {\bf A} = {\bf I}$$ 
%
Then
%
- ${\bf B}$ is called the ***inverse*** of ${\bf A}$, and written ${\bf A}^{-1}$
- ${\bf A}$ is called ***invertible***

```{admonition} Fact
:class: important

A square matrix ${\bf A}$ is nonsingular if and only if it is
```
invertible

Remark
%
- ${\bf A}^{-1}$ is just the matrix corresponding to the linear map $T^{-1}$

```{admonition} Fact
:class: important

Given nonsingular $N \times N$ matrix ${\bf A}$ and ${\bf b} \in \mathbb{R}^N$, the unique
```
solution to ${\bf A} {\bf x} = {\bf b}$ is given by 
%
$$ {\bf x}_b := {\bf A}^{-1} {\bf b} $$
%

Proof: Since ${\bf A}$ is nonsingular we already know any solution is
unique

- $T$ is a bijection, and hence one-to-one
- if ${\bf A} {\bf x} = {\bf A} {\bf y} = {\bf b}$ then ${\bf x} = {\bf y}$

To show that ${\bf x}_b$ is indeed a solution we need to show that 
${\bf A} {\bf x}_b = {\bf b}$ 

To see this, observe that
%
$$
%
{\bf A} {\bf x}_b = {\bf A} {\bf A}^{-1} {\bf b} = {\bf I} {\bf b} = {\bf b}
%
$$
%

```{admonition} Example
:class: tip

Recall the one good linear market system 
```
%
$$
%
\begin{array}{c}
q = a - b p \\
q = c + d p
\end{array}
\quad \iff \quad
\begin{pmatrix}
1 & b \\
1 & -d
\end{pmatrix}
\begin{pmatrix}
q\\
p
\end{pmatrix}
=
\begin{pmatrix}
a \\
c 
\end{pmatrix}
%
$$
%

Suppose that $a=5$, $b=2$, $c=1$, $d=1.5$

The matrix system is ${\bf A} {\bf x} = {\bf b}$ where
%
$$
%
{\bf A} :=
\begin{pmatrix}
1 & 2 \\
1 & -1.5
\end{pmatrix},
\;
{\bf x} :=
\begin{pmatrix}
q\\
p
\end{pmatrix},
\;
{\bf b} :=
\begin{pmatrix}
5 \\
1 
\end{pmatrix}
%
$$
%

Since $b \ne -d$ we can solve for the unique solution

Easy by hand but let's try on the computer


```{code-cell} python3
:tags: [hide/remote-cell/input/output]
---
mystnb:
image:
width: 80%
align: center
---
tags:
- hide-input
- remove-output

In [1]: import numpy as np
In [2]: from scipy.linalg import inv

In [3]: A = [[1, 2],
...: [1, -1.5]]

In [4]: b = [5, 1]

In [5]: q, p = np.dot(inv(A), b) # A^{-1} b

In [6]: q
Out[6]: 2.7142857142857144
In [7]: p
Out[7]: 1.1428571428571428

```
-->

```{figure} _static/plots/simple_mkt.png
:name: 

Equilibrium $(p^*, q^*)$ in the one good case
```

```{admonition} Fact
:class: important

In the $2 \times 2$ case, the inverse has the form
```

%
$$
%
\left(
\begin{array}{cc}
a & b \\
c & d \\
\end{array}
\right)^{-1} = 
\frac{1}{ad - bc}
\left(
\begin{array}{cc}
d & -b \\
-c & a \\
\end{array}
\right)
%
$$
%

```{admonition} Example
:class: tip

```

%
$$
%
{\bf A} = 
\left(
\begin{array}{cc}
1 & 2 \\
1 & -1.5 \\
\end{array}
\right)
\quad \implies \quad
{\bf A}^{-1} = 
\frac{1}{-3.5}
\left(
\begin{array}{cc}
-1.5 & -2 \\
-1 & 1 \\
\end{array}
\right)
%
$$
%

```{admonition} Example
:class: tip

Consider the $N$ good linear demand system
```
%
$$
%
q_n = \sum_{k=1}^N a_{nk} p_k + b_n,
\quad n = 1, \ldots N
%
$$ (eq:ds)
%

Task: take quantities $q_1, \ldots, q_N$ as given and find
corresponding prices $p_1, \ldots, p_N$ --- the "inverse demand curves"

We can write {eq}`eq:ds` as 
%
$$
%
{\bf q} = {\bf A} {\bf p} + {\bf b}
%
$$
%
where vectors are $N$-vectors and ${\bf A}$ is $N \times N$

If the columns of ${\bf A}$ are linearly independent then a unique solution
exists for each fixed ${\bf q}$ and ${\bf b}$, and is given by
%
$$
%
{\bf p} = {\bf A}^{-1} ({\bf q} - {\bf b})
%
$$
%

### Left and Right Inverses

Given square matrix ${\bf A}$, a matrix ${\bf B}$ is called 
% 
- a ***left inverse*** of ${\bf A}$ if ${\bf B} {\bf A} = {\bf I}$
- a ***right inverse*** of ${\bf A}$ if ${\bf A} {\bf B} = {\bf I}$

By definition, a matrix that is both an left inverse and a right inverse is an inverse

```{admonition} Fact
:class: important

If square matrix ${\bf B}$ is either a left or right inverse for
```
${\bf A}$, then ${\bf A}$ is nonsingular and ${\bf A}^{-1} = {\bf B}$

In other words, for square matrices,
%

left inverse $\iff$ right inverse $\iff$ inverse

### Rules for Inverses

```{admonition} Fact
:class: important

If ${\bf A}$ is nonsingular and $\alpha \ne 0$, then
```
%
1. ${\bf A}^{-1}$ is nonsingular and $({\bf A}^{-1})^{-1} = {\bf A}$
9. $\alpha {\bf A}$ is nonsingular and $(\alpha {\bf A})^{-1} = \alpha^{-1} {\bf A}^{-1}$

Proof of part 2: 

It suffices to show that $\alpha^{-1} {\bf A}^{-1}$ is the right inverse of 
$\alpha {\bf A}$

This is true because
%
$$
%
\alpha {\bf A} \alpha^{-1} {\bf A}^{-1} 
=
\alpha \alpha^{-1} {\bf A} {\bf A}^{-1} 
= {\bf I}
%
$$
%

```{admonition} Fact
:class: important

If ${\bf A}$ and ${\bf B}$ are $N \times N$ and nonsingular then
```
%
1. ${\bf A} {\bf B}$ is also nonsingular

9. $({\bf A} {\bf B})^{-1} = {\bf B}^{-1} {\bf A}^{-1}$

Proof I: Let $T$ and $U$ be the linear maps corresponding to ${\bf A}$ and
${\bf B}$

Recall that

- $T \circ U$ is the linear map corresponding to ${\bf A} {\bf B}$
- Compositions of linear maps are linear
- Compositions of bijections are bijections

Hence $T \circ U$ is a linear bijection with $(T \circ U)^{-1} = U^{-1} \circ T^{-1}$

That is, ${\bf A}{\bf B}$ is nonsingular with inverse ${\bf B}^{-1} {\bf A}^{-1}$

Proof II: 

A different proof that ${\bf A} {\bf B}$ is nonsingular with inverse 
${\bf B}^{-1} {\bf A}^{-1}$

Suffices to show that ${\bf B}^{-1} {\bf A}^{-1}$ is the right inverse of ${\bf A} {\bf B}$

To see this, observe that 
%
$$
%
{\bf A} {\bf B} {\bf B}^{-1} {\bf A}^{-1}
= {\bf A} {\bf A}^{-1}
= {\bf I}
%
$$
%

Hence ${\bf B}^{-1} {\bf A}^{-1}$ is a right inverse as claimed

## The Singular Case

### When the Conditions Fail

Suppose as before we have 
%
- an $N \times N$ matrix ${\bf A}$ 
- an $N \times 1$ vector ${\bf b}$ 

We seek a solution ${\bf x}$ to the equation ${\bf A} {\bf x} = {\bf b}$

What if ${\bf A}$ is ***singular***?

Then $T{\bf x} = {\bf A} {\bf x}$ is not a bijection, and in fact
%
- $T$ cannot be onto (otherwise it's a bijection)

- $T$ cannot be one-to-one (otherwise it's a bijection)

Hence neither existence nor uniqueness is guaranteed

```{admonition} Example
:class: tip

The matrix ${\bf A}$ with columns
```
%
$$
%
{\bf a}_1 :=
\begin{pmatrix}
3 \\
4 \\
2
\end{pmatrix},
\quad
{\bf a}_2 :=
\begin{pmatrix}
3 \\
-4 \\
1
\end{pmatrix}
\quad \text{and} \quad
{\bf a}_3 :=
\begin{pmatrix}
-3 \\
4 \\
-1
\end{pmatrix}
%
$$
%
is singular (${\bf a}_3 = - {\bf a}_2$)

Its column space $\mathrm{span}({\bf A})$ is just a plane in $\mathbb{R}^2$

Recall ${\bf b} \in \mathrm{span}({\bf A})$ 
%
-[] $\iff$ $\exists \, x_1, \ldots, x_N$ such that $\sum_{k=1}^N
x_k \mathrm{col}_k({\bf A}) = {\bf b}$

-[] $\iff$ $\exists \, {\bf x}$ such that ${\bf A} {\bf x} = {\bf b}$

Thus if ${\bf b}$ is not in this plane then ${\bf A} {\bf x} = {\bf b}$ has no
solution

```{figure} _static/plots/not_in_span.png
:name: 

The vector ${\bf b}$ is not in $\mathrm{span}({\bf A})$
```

When ${\bf A}$ is $N \times N$ and singular how rare is scenario ${\bf b} \in
\mathrm{span}({\bf A})$?

Answer: In a sense, very rare

We know that $\dim(\mathrm{span}({\bf A})) < N$

Such sets are always "very small" subset of $\mathbb{R}^N$ in terms of "volume"

- A $K < N$ dimensional subspace has "measure zero" in $\mathbb{R}^N$
- A "randomly chosen" ${\bf b}$ has zero probability of being in such
a set

```{admonition} Example
:class: tip

Consider the case where $N = 3$ and $K=2$
```

A two-dimensional linear subspace is a 2D plane in $\mathbb{R}^3$

This set has no volume because planes have no ``thickness''

All this means that if ${\bf A}$ is singular then existence
of a solution to ${\bf A} {\bf x} = {\bf b}$ typically fails

In fact the problem is worse --- uniqueness fails as well

```{admonition} Fact
:class: important

If ${\bf A}$ is a singular matrix and ${\bf A} {\bf x} = {\bf b}$ has a
```
solution then it has an infinity (in fact a continuum) of solutions

Proof: Let ${\bf A}$ be singular and let ${\bf x}$ be a solution

Since ${\bf A}$ is singular there exists a nonzero ${\bf y}$ with ${\bf A}
{\bf y} = {\bf 0}$

But then $\alpha {\bf y} + {\bf x}$ is also a solution for any $\alpha \in
\mathbb{R}$ because
%
$$ 
%
{\bf A}(\alpha {\bf y} + {\bf x}) 
= \alpha {\bf A} {\bf y} + {\bf A} {\bf x}
= {\bf A} {\bf x} = {\bf b}
%
$$
%

## Determinants

### Determinants

Let $S(N)$ be set of all bijections from $\{1, \ldots, N\}$ to itself

For $\pi \in S(N)$ we define the ***signature*** of $\pi$ as 
%
$$
%
\mathrm{sgn}(\pi) := \prod_{m < n} \frac{\pi(m) - \pi(n)}{m - n}
%
$$
%

The ***determinant*** of $N \times N$ matrix ${\bf A}$ is then given as
%
$$
%
\det({\bf A}) 
:= \sum_{\pi \in S(N)} \mathrm{sgn}(\pi) \prod_{n=1}^N a_{\pi(n) n}
%
$$
%

- You don't need to understand or remember this for our course

```{admonition} Fact
:class: important

In the $N = 2$ case this definition reduces to
```

%
$$
%
\det 
\left(
\begin{array}{cc}
a & b \\
c & d \\
\end{array}
\right)
= ad - bc
%
$$
%

- Remark: But you do need to remember this $2 \times 2$ case

```{admonition} Example
:class: tip

%
$$
%
\det 
\left(
\begin{array}{cc}
2 & 0 \\
7 & -1 \\
\end{array}
\right)
= (2 \times -1) - (7 \times 0) = -2
%
$$
%

```

Important facts concerning the determinant

```{admonition} Fact
:class: important

If ${\bf I}$ is the $N \times N$ identity, ${\bf A}$ and ${\bf B}$ are $N
```
\times N$ matrices and $\alpha \in \mathbb{R}$, then
%
1. $\det({\bf I}) = 1$ 

- ${\bf A}$ is nonsingular if and only if $\det({\bf A})
\ne 0$

- $\det({\bf A}{\bf B}) = \det({\bf A})
\det({\bf B})$

- $\det(\alpha {\bf A}) = \alpha^N \det({\bf A})$

9. $\det({\bf A}^{-1}) = (\det({\bf A}))^{-1}$

```{admonition} Example
:class: tip

Thus singularity in the $2 \times 2$ case is equivalent to
```
%
$$
%
\det({\bf A})
=
\det 
\left(
\begin{array}{cc}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
\end{array}
\right)
= a_{11}a_{22} - a_{12} a_{21} = 0
%
$$
%

**Exercise:** Let ${\bf a}_i := \mathrm{col}_i({\bf A})$ and assume that $a_{ij} \ne 0$ for each $i, j$

Show the following are equivalent:
%
1. $a_{11}a_{22} = a_{12} a_{21}$
9. ${\bf a}_1 = \lambda {\bf a}_2$ for some $\lambda \in \mathbb{R}$
%


```{code-cell} python3
:tags: [hide/remote-cell/input/output]
---
mystnb:
image:
width: 80%
align: center
---
tags:
- hide-input
- remove-output

In [1]: import numpy as np

In [2]: A = np.random.randn(2, 2) # Random matrix

In [3]: A
Out[3]: 
array([[-0.70120551, 0.57088203],
[ 0.40757074, -0.72769741]])

In [4]: np.linalg.det(A)
Out[4]: 0.27759063032043652

In [5]: 1.0 / np.linalg.det(np.linalg.inv(A))
Out[5]: 0.27759063032043652

```
-->

As an exercise, let's now show that any right inverse is an inverse

Fix square ${\bf A}$ and suppose ${\bf B}$ is a right inverse:
%
$$
%
{\bf A} {\bf B} = {\bf I}
%
$$ (eq:ud)
%

Applying the determinant to both sides gives $\det({\bf A}) \det({\bf B}) = 1$

Hence ${\bf B}$ is nonsingular (why?) and we can
%
1. multiply {eq}`eq:ud` by ${\bf B}$ to get ${\bf B} {\bf A} {\bf B} = {\bf B}$
9. then postmultiply by ${\bf B}^{-1}$ to get ${\bf B} {\bf A} = {\bf I}$

We see that ${\bf B}$ is also left inverse, and therefore an inverse of ${\bf A}$ 

**Exercise:** Do the left inverse case 

## Other Linear Equations

### Other Linear Equations

So far we have considered the nice $N \times N$ case for equations

- number of equations $=$ number of unknowns

We have to deal with other cases too

Underdetermined systems: 

- eqs $<$ unknowns

Overdetermined systems: 

- eqs $>$ unknowns

### Overdetermined Systems

Consider the system ${\bf A} {\bf x} = {\bf b}$ where ${\bf A}$ is $N \times K$ and $K < N$

- The elements of ${\bf x}$ are the unknowns 

- More equations than unknowns ($N > K$)

May not be able to find an ${\bf x}$ that satisfies all $N$ equations 

Let's look at this in more detail...

Fix $N \times K$ matrix ${\bf A}$ with $K < N$

Let $T \colon \mathbb{R}^K \to \mathbb{R}^N$ be defined by $T {\bf x} = {\bf A} {\bf x}$

We know these to be equivalent:
%
1. there exists an ${\bf x} \in \mathbb{R}^K$ with ${\bf A} {\bf x} = {\bf b}$

- ${\bf b}$ has a preimage under $T$

- ${\bf b}$ is in $\mathrm{rng}(T)$

9. ${\bf b}$ is in $\mathrm{span}({\bf A})$

We also know $T$ ***cannot*** be onto (maps small to big space)

Hence ${\bf b} \in \mathrm{span}({\bf A})$ will not always hold

Given our assumption that $K < N$, how rare is the scenario ${\bf b} \in
\mathrm{span}({\bf A})$?

Answer: We talked about this before --- it's very rare

We know that $\dim(\mathrm{rng}(T)) = \dim(\mathrm{span}({\bf A})) \leq K < N$

A $K < N$ dimensional subspace has "measure zero" in $\mathbb{R}^N$

So should we give up on solving ${\bf A} {\bf x} = {\bf b}$ in the
overdetermined case?

What's typically done is we try to find a best approximation

To define ``best'' we need a way of ranking approximations

The standard way is in terms of Euclidean norm

In particular, we search for the ${\bf x}$ that solves

%
$$ \min_{{\bf x} \in \mathbb{R}^K} \| {\bf A} {\bf x} - {\bf b}\|$$
%

Details later

### Underdetermined Systems

Now consider ${\bf A} {\bf x} = {\bf b}$ when ${\bf A}$ is $N \times K$ and $K > N$

Let $T \colon \mathbb{R}^K \to \mathbb{R}^N$ be defined by $T {\bf x} = {\bf A} {\bf x}$

Now $T$ maps from a larger to a smaller place

This tells us that $T$ is not one-to-one

Hence solutions are not in general unique

In fact the following is true

**Exercise:** Show that ${\bf A} {\bf x} =
{\bf b}$ has a solution and $K > N$, then the same equation has an infinity of solutions

Remark: Working with underdetermined systems is relatively rare in economics / elsewhere

### Transpose

The ***transpose*** of ${\bf A}$ is the matrix ${\bf A}'$ defined by 
%
$$\mathrm{col}_n({\bf A}') = \mathrm{row}_n({\bf A})$$
%

```{admonition} Example
:class: tip

If
```
%
$$
%
{\bf A} := 
\left(
\begin{array}{cc}
10 & 40 \\
20 & 50 \\
30 & 60
\end{array}
\right)
\quad \text{then} \quad
{\bf A}' = 
\left(
\begin{array}{ccc}
10 & 20 & 30 \\
40 & 50 & 60 
\end{array}
\right)
%
$$ (eq:aandb)
%

If
%
$$
%
{\bf B} := 
\left(
\begin{array}{ccc}
1 & 3 & 5 \\
2 & 4 & 6 \\
\end{array}
\right)
\quad \text{then} \quad
{\bf B}' := 
\left(
\begin{array}{cc}
1 & 2 \\
3 & 4 \\
5 & 6 
\end{array}
\right)
%
$$
%

```{admonition} Fact
:class: important

For conformable matrices ${\bf A}$ and ${\bf B}$, transposition satisfies
```
%
1. $({\bf A}')' = {\bf A}$

- $({\bf A} {\bf B})' = {\bf B}' {\bf A}'$

- $({\bf A} + {\bf B})' = {\bf A}' + {\bf B}'$

9. $(c {\bf A})' = c {\bf A}'$ for any constant $c$
%

For each square matrix ${\bf A}$, 
%
1. $\det({\bf A}') = \det({\bf A})$

9. If ${\bf A}$ is nonsingular then so is ${\bf A}'$, and $({\bf A}')^{-1}= ({\bf A}^{-1})'$
%


```{code-cell} python3
:tags: [hide/remote-cell/input/output]
---
mystnb:
image:
width: 80%
align: center
---
tags:
- hide-input
- remove-output

In [1]: import numpy as np

In [2]: A = np.random.randn(2, 2)

In [3]: np.linalg.inv(A.transpose())
Out[3]: 
array([[ 4.52767206, -1.83628665],
[ 0.90504942, 1.5014984 ]])

In [4]: np.linalg.inv(A).transpose()
Out[4]: 
array([[ 4.52767206, -1.83628665],
[ 0.90504942, 1.5014984 ]])

```
-->

A square matrix ${\bf A}$ is called ***symmetric*** if ${\bf A}' = {\bf A}$

Equivalent: $a_{nk} = a_{kn}$ for all $n, k$

\Egs

%
$$
%
{\bf A} 
:= 
\left(
\begin{array}{cc}
10 & 20 \\
20 & 50 
\end{array}
\right),
\qquad
{\bf B} 
:= 
\left(
\begin{array}{ccc}
1 & 2 & 3 \\
2 & 0 & 0 \\ 
3 & 0 & 2 
\end{array}
\right)
%
$$
%

**Exercise:** For any matrix ${\bf A}$, show that ${\bf A}' {\bf A}$ and ${\bf A} {\bf A}'$ are always
%
1. well-defined (multiplication makes sense)
9. symmetric

The ***trace*** of a square matrix is defined by 
%

%
$$
%
\mathrm{trace} \left(
\begin{array}{ccc}
a_{11} & \cdots & a_{1N} \\
\vdots & & \vdots \\
a_{N1} & \cdots & a_{NN} \\
\end{array}
\right)
= 
\sum_{n=1}^N a_{nn}
%
$$
%

```{admonition} Fact
:class: important

$\mathrm{trace}({\bf A}) = \mathrm{trace}({\bf A}')$
```

```{admonition} Fact
:class: important

If ${\bf A}$ and ${\bf B}$ are square matrices and
```
$\alpha, \beta \in \mathbb{R}$, then 
%
$$
%
\mathrm{trace}(\alpha {\bf A} + \beta {\bf B}) 
= \alpha \mathrm{trace}({\bf A}) + \beta \mathrm{trace}({\bf B})
%
$$
%

```{admonition} Fact
:class: important

When conformable, $\mathrm{trace}({\bf A} {\bf B}) = \mathrm{trace}({\bf B} {\bf A})$
```

A square matrix ${\bf A}$ is called ***idempotent*** if ${\bf A} {\bf A} = {\bf A}$

\Egs

%
$$
%
{\bf A} 
:= 
\left(
\begin{array}{cc}
1 & 1 \\
0 & 0 
\end{array}
\right),
\qquad
{\bf I} 
:= 
\left(
\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\ 
0 & 0 & 1 
\end{array}
\right)
%
$$
%

The next result is often used in statistics / econometrics:

```{admonition} Fact
:class: important

If ${\bf A}$ is idempotent, then $\mathrm{rank}({\bf A}) = \mathrm{trace}({\bf A})$
```

## Diagonal Matrices

### Diagonal Matrices

Consider a square $N \times N$ matrix ${\bf A}$

The $N$ elements of the form $a_{nn}$ are called the ***principal diagonal***

%
$$
%
\left(
\begin{array}{cccc}
***a_{11***} & a_{12} & \cdots & a_{1N} \\
a_{21} & ***a_{22***} & \cdots & a_{2N} \\
\vdots & \vdots & & \vdots \\
a_{N1} & a_{N2} & \cdots & ***a_{NN***} \\
\end{array}
\right)
%
$$
%

A square matrix ${\bf D}$ is called ***diagonal*** if all entries off the
principal diagonal are zero

%
$$
%
{\bf D} = 
\left(
\begin{array}{cccc}
d_1 & 0 & \cdots & 0 \\
0 & d_2 & \cdots & 0 \\
\vdots & \vdots & & \vdots \\
0 & 0 & \cdots & d_N \\
\end{array}
\right)
%
$$
%

Often written as

%
$$
%
{\bf D} = \mathrm{diag}(d_1, \ldots, d_N) 
%
$$
%

Incidentally, the same notation works in Python


```{code-cell} python3
:tags: [hide/remote-cell/input/output]
---
mystnb:
image:
width: 80%
align: center
---
tags:
- hide-input
- remove-output

In [1]: import numpy as np

In [2]: D = np.diag((2, 4, 6, 8, 10))

In [3]: D
Out[3]: 
array([[ 2, 0, 0, 0, 0],
[ 0, 4, 0, 0, 0],
[ 0, 0, 6, 0, 0],
[ 0, 0, 0, 8, 0],
[ 0, 0, 0, 0, 10]])

```
-->

Diagonal systems are very easy to solve

\Eg

%
$$
%
\begin{pmatrix}
d_1 & 0 & 0 \\
0 & d_2 & 0 \\
0 & 0 & d_3 
\end{pmatrix}
\begin{pmatrix}
x_1 \\
x_2 \\
x_3 
\end{pmatrix}
=
\begin{pmatrix}
b_1 \\
b_2 \\
b_3 
\end{pmatrix}
%
$$
%

is equivalent to

%
$$
%
\begin{array}{c}
d_1 x_1 = b_1 \\
d_2x_2 = b_2 \\
d_3 x_3 = b_3
\end{array}
%
$$
%

```{admonition} Fact
:class: important

If ${\bf C} = \mathrm{diag}(c_1, \ldots, c_N)$ and ${\bf D} = \mathrm{diag}(d_1, \ldots,
```
d_N)$ then
%
1. ${\bf C} + {\bf D} = \mathrm{diag}(c_1 + d_1, \ldots, c_N + d_N)$

- ${\bf C} {\bf D} = \mathrm{diag}(c_1 d_1, \ldots, c_N d_N)$

- ${\bf D}^k = \mathrm{diag}(d^k_1, \ldots, d^k_N)$ for any $k \in \mathbb{N}$

- $d_n \geq 0$ for all $n$ $\implies$ ${\bf D}^{1/2}$ exists and equals
%
$$\mathrm{diag}(\sqrt{d_1}, \ldots, \sqrt{d_N})$$
%

- $d_n \ne 0$ for all $n$ $\implies$ ${\bf D}$ is nonsingular and 
%
$${\bf D}^{-1} = \mathrm{diag}(d_1^{-1}, \ldots, d_N^{-1})$$
%

%

Proofs: Check 1 and 2 directly, other parts follow


```{code-cell} python3
:tags: [hide/remote-cell/input/output]
---
mystnb:
image:
width: 80%
align: center
---
tags:
- hide-input
- remove-output

In [1]: import numpy as np

In [2]: D = np.diag((2, 4, 10, 100))

In [3]: np.linalg.inv(D)
Out[3]: 
array([[ 0.5 , 0. , 0. , 0. ],
[ 0. , 0.25, 0. , 0. ],
[ 0. , 0. , 0.1 , 0. ],
[ 0. , 0. , 0. , 0.01]])

```
-->

A square matrix is called ***lower triangular*** if every element strictly above the
principle diagonal is zero

\Eg
%
$$
%
{\bf L} :=
\left(
\begin{array}{ccc}
1 & 0 & 0 \\
2 & 5 & 0 \\
3 & 6 & 1
\end{array}
\right)
%
$$ (eq:ltute)
%

A square matrix is called ***upper triangular*** if every element
strictly below the principle diagonal is zero

\Eg
%
$$
%
{\bf U} :=
\left(
\begin{array}{ccc}
1 & 2 & 3 \\
0 & 5 & 6 \\
0 & 0 & 1
\end{array}
\right)
%
$$
%

Called ***triangular*** if either upper or lower triangular

Associated linear equations also simple to solve 

\Eg
% 
%
$$
%
\left(
\begin{array}{ccc}
4 & 0 & 0 \\
2 & 5 & 0 \\
3 & 6 & 1
\end{array}
\right)
\left(
\begin{array}{ccc}
x_1 \\
x_2 \\
x_3 
\end{array}
\right)
=
\left(
\begin{array}{c}
b_1 \\
b_2 \\
b_3 \\
\end{array}
\right)
%
$$
%

becomes

%
$$
%
\begin{array}{c}
4x_1 = b_1 \\
2x_1 + 5x_2 = b_2 \\
3x_1 + 6x_2 + x_3 = b_3
\end{array}
%
$$
%

Top equation involves only $x_1$, so can solve for it directly

Plug that value into second equation, solve out for $x_2$, etc.

## Eigenvalues

### Eigenvalues and Eigenvectors

Let ${\bf A}$ be $N \times N$ 

In general ${\bf A}$ maps ${\bf x}$ to some arbitrary new location ${\bf A} {\bf x}$

But sometimes ${\bf x}$ will only be ***scaled***:
%
$$
%
{\bf A} {\bf x} = \lambda {\bf x}
\quad \text{for some scalar $\lambda$}
%
$$ (eq:eiei)
%

If {eq}`eq:eiei` holds and ${\bf x}$ is nonzero, then 
%
1. ${\bf x}$ is called an ***eigenvector*** of ${\bf A}$
and $\lambda$ is called an ***eigenvalue***

9. $({\bf x}, \lambda)$ is called an ***eigenpair***

Clearly $({\bf x}, \lambda)$ is an eigenpair of ${\bf A}$ $\implies$
$(\alpha {\bf x}, \lambda)$ is an eigenpair of ${\bf A}$ for any nonzero $\alpha$

```{admonition} Example
:class: tip

Let
```
%
$$
%
{\bf A} :=
\begin{pmatrix}
1 & -1 \\
3 & 5
\end{pmatrix}
%
$$
%

Then

%
$$
%
\lambda = 2 
\quad \text{ and } \quad
{\bf x}
=
\begin{pmatrix}
1 \\
-1
\end{pmatrix}
%
$$
%

form an eigenpair because ${\bf x} \ne {\bf 0}$ and

%
$$
%
{\bf A} {\bf x} =
\begin{pmatrix}
1 & -1 \\
3 & 5
\end{pmatrix}
\begin{pmatrix}
1 \\
-1
\end{pmatrix}
=
\begin{pmatrix}
2 \\
-2
\end{pmatrix}
= 2
\begin{pmatrix}
1 \\
-1
\end{pmatrix}
=
\lambda {\bf x} 
%
$$
%

\Eg


```{code-cell} python3
:tags: [hide/remote-cell/input/output]
---
mystnb:
image:
width: 80%
align: center
---
tags:
- hide-input
- remove-output

In [3]: import numpy as np
In [4]: A = [[1, 2],
...: [2, 1]]

In [5]: eigvals, eigvecs = np.linalg.eig(A)

In [6]: x = eigvecs[:,0] # Let x = first eigenvector
In [7]: lm = eigvals[0] # Let lm = first eigenvalue

In [8]: np.dot(A, x) # Compute Ax
Out[8]: array([ 2.12132034, 2.12132034])
In [9]: lm * x # Compute lm x 
Out[9]: array([ 2.12132034, 2.12132034])

```
-->

```{figure} _static/plots/eigenvecs.png
:name: 

The eigenvectors of ${\bf A}$
```

Consider the matrix 
%
$$
%
{\bf R} := 
\left(
\begin{array}{cc}
0 & -1 \\
1 & 0 \\
\end{array}
\right)
%
$$
%

Induces counter-clockwise rotation on any point by $90^{\circ}$

Hence no point ${\bf x}$ is scaled

Hence there exists ***no*** pair $\lambda \in \mathbb{R}$ and ${\bf x} \ne
{\bf 0}$
such that
%
$${\bf R} {\bf x} = \lambda {\bf x}$$ 
%

- In other words, no ***real-valued*** eigenpairs exist

```{figure} _static/plots/rotation_1.png
:name: 

The matrix ${\bf R}$ rotates points by $90^{\circ}$
```

```{figure} _static/plots/rotation_2.png
:name: 

The matrix ${\bf R}$ rotates points by $90^{\circ}$
```

But ${\bf R} {\bf x} = \lambda {\bf x}$ can hold ***if*** we allow
complex values

```{admonition} Example
:class: tip

```
%
$$
%
\left(
\begin{array}{cc}
0 & -1 \\
1 & 0 \\
\end{array}
\right)
\begin{pmatrix}
1 \\
-i
\end{pmatrix}
=
\begin{pmatrix}
i \\
1
\end{pmatrix}
=
i
\begin{pmatrix}
1 \\
-i
\end{pmatrix}
%
$$
%

That is,
%
$$
%
{\bf R} {\bf x} = \lambda {\bf x}
\quad \text{for} \quad
\lambda := i
\quad \text{and} \quad
{\bf x} := 
\begin{pmatrix}
1 \\
-i
\end{pmatrix}
%
$$
%

Hence $({\bf x}, \lambda)$ is an eigenpair provided we admit complex values 

We do, since this is standard

```{admonition} Fact
:class: important

For any square matrix ${\bf A}$ 
```
%
$$
%
\lambda \text{ is an eigenvalue of } {\bf A} \; \iff \;
\det({\bf A} - \lambda {\bf I}) = 0
%
$$
%

Proof: Let ${\bf A}$ by $N \times N$ and let ${\bf I}$ be the $N \times N$
identity

We have
%
$$
%
\det({\bf A} - \lambda {\bf I}) = 0
& \iff {\bf A} - \lambda {\bf I} \text{ is singular}
\\
& \iff \exists \, {\bf x} \ne {\bf 0} \text{ such that }
({\bf A} - \lambda {\bf I}) {\bf x} = {\bf 0}
\\
& \iff \exists \, {\bf x} \ne {\bf 0} \text{ such that }
{\bf A} {\bf x} = \lambda {\bf x}
\\
& \iff \lambda 
\text{ is an eigenvalue of } {\bf A}
%
$$
%

```{admonition} Example
:class: tip

In the $2 \times 2$ case,
```
%
$$
%
{\bf A} =
\left(
\begin{array}{cc}
a & b \\
c & d \\
\end{array}
\right)
\quad \implies \quad
{\bf A} - \lambda {\bf I} =
\left(
\begin{array}{cc}
a - \lambda & b \\
c & d - \lambda 
\end{array}
\right)
%
$$
%
$$
%
\text{ therefore }
\det({\bf A} - \lambda {\bf I}) 
= (a - \lambda)(d - \lambda) - bc
\\
= \lambda^2 - (a + d) \lambda + (ad - bc)
%
$$
%

Hence the eigenvalues of ${\bf A}$ are given by the two roots of 
%
$$
%
\lambda^2 - (a + d) \lambda + (ad - bc) = 0
%
$$
%

Equivalently,
%
$$
%
\lambda^2 - \mathrm{trace}({\bf A}) \lambda + \det({\bf A}) = 0
%
$$
%

### Existence of Eigenvalues

Fix $N \times N$ matrix ${\bf A}$ 

```{admonition} Fact
:class: important

There exist complex numbers $\lambda_1, \ldots, \lambda_N$ such that
```
%
$$
%
\det({\bf A} - \lambda {\bf I}) = \prod_{n=1}^N (\lambda_n - \lambda)
%
$$
%

Each such $\lambda_i$ is an eigenvalue of ${\bf A}$ because
%
$$
%
\det({\bf A} - \lambda_i {\bf I}) 
= \prod_{n=1}^N (\lambda_n - \lambda_i) 
= 0
%
$$
%

Important: Not all are necessarily distinct --- there can be repeats

```{admonition} Fact
:class: important

Given $N \times N$ matrix ${\bf A}$ with eigenvalues $\lambda_1, \ldots, \lambda_N$
```
we have
%

- $\det({\bf A}) = \prod_{n=1}^N \lambda_n$

- $\mathrm{trace}({\bf A}) = \sum_{n=1}^N \lambda_n$

- If ${\bf A}$ is symmetric, then $\lambda_n \in \mathbb{R}$ for all $n$

9. If ${\bf A} = \mathrm{diag}(d_1, \ldots, d_N)$, then $\lambda_n = d_n$ for all $n$

Hence ${\bf A}$ is nonsingular $\iff$ all eigenvalues are nonzero (why?)

```{admonition} Fact
:class: important

If ${\bf A}$ is nonsingular, then 
```
%
$$
%
\text{eigenvalues of } {\bf A}^{-1}
= 1/\lambda_1, \ldots, 1/\lambda_N
%
$$
%

### Diagonalization

Square matrix ${\bf A}$ is said to be ***similar*** to square matrix ${\bf B}$ if 
%
$$
%
\exists \text{ invertible matrix ${\bf P}$ such that }
{\bf A} = {\bf P} {\bf B} {\bf P}^{-1}
%
$$ 
%

```{figure} _static/plots/diagonalize.png
:name: 

```

```{admonition} Fact
:class: important

If ${\bf A}$ is similar to ${\bf B}$, then ${\bf A}^t$ is similar to
```
${\bf B}^t$ for all $t \in \mathbb{N}$

Proof for case $t=2$: 
%
$$
%
{\bf A}^2
= {\bf A} {\bf A} \\
= {\bf P} {\bf B} {\bf P}^{-1} {\bf P} {\bf B} {\bf P}^{-1} \\
= {\bf P} {\bf B} {\bf B} {\bf P}^{-1} \\
= {\bf P} {\bf B}^2 {\bf P}^{-1} 
%
$$
%

If ${\bf A}$ is similar to a diagonal matrix, then ${\bf A}$ is
called ***diagonalizable***

```{admonition} Fact
:class: important

Let ${\bf A}$ be diagonalizable with ${\bf A} = {\bf P} {\bf D}
```
{\bf P}^{-1}$ and let
%
1. ${\bf D} = \mathrm{diag}(\lambda_1, \ldots, \lambda_N)$
9. ${\bf p}_n := \mathrm{col}_n({\bf P})$
%
Then $({\bf p}_n, \lambda_n)$ is an eigenpair of ${\bf A}$ for each $n$

Proof: From ${\bf A} = {\bf P} {\bf D} {\bf P}^{-1}$ we get ${\bf A} {\bf P} = {\bf P} {\bf D}$

Equating $n$-th column on each side gives 
%
$$
%
{\bf A} {\bf p}_n = \lambda_n {\bf p}_n
%
$$
%

Moreover ${\bf p}_n \ne {\bf 0}$ because ${\bf P}$ is invertible (which
facts?)

```{admonition} Fact
:class: important

If $N \times N$ matrix ${\bf A}$ has $N$ distinct eigenvalues
```
$\lambda_1, \ldots, \lambda_N$, then
${\bf A}$ is diagonalizable as ${\bf A} = {\bf P} {\bf D} {\bf P}^{-1}$ where
%
1. ${\bf D} = \mathrm{diag}(\lambda_1, \ldots, \lambda_N)$
9. $\mathrm{col}_n({\bf P})$ is an eigenvector for $\lambda_n$

```{admonition} Example
:class: tip

Let
```
%
$$
%
{\bf A} :=
\begin{pmatrix}
1 & -1 \\
3 & 5
\end{pmatrix}
%
$$
%

The eigenvalues of ${\bf A}$ are 2 and 4, while the eigenvectors are
%
$$
%
{\bf p}_1 :=
\begin{pmatrix}
1 \\
-1
\end{pmatrix}
\quad \text{and} \quad
{\bf p}_2 :=
\begin{pmatrix}
1 \\
-3
\end{pmatrix}
%
$$
%

Hence
%
$$
%
{\bf A} = {\bf P} \mathrm{diag}(2, 4) {\bf P}^{-1}
%
$$
%


```{code-cell} python3
:tags: [hide/remote-cell/input/output]
---
mystnb:
image:
width: 80%
align: center
---
tags:
- hide-input
- remove-output

In [1]: import numpy as np
In [2]: from numpy.linalg import inv

In [3]: A = [[1, -1],
...: [3, 5]]

In [4]: D = np.diag((2, 4))

In [5]: P = [[1, 1], # Matrix of eigenvectors
...: [-1, -3]]

In [6]: np.dot(P, np.dot(D, inv(P))) # PDP^{-1} = A?
Out[6]: 
array([[ 1., -1.],
[ 3., 5.]])

```
-->

## Matrix Norm

### The Euclidean Matrix Norm

The concept of norm is very helpful for working with vectors

- provides notions of distance, similarity, convergence

How about an analogous concept for matrices?

Given $N \times K$ matrix ${\bf A}$, we define 
%
$$
%
\| {\bf A} \| :=
\max \left\{ 
\frac{\| {\bf A} {\bf x} \|}{ \| {\bf x} \|} \,: \, 
{\bf x} \in \mathbb{R}^K, \; {\bf x} \ne {\bf 0}
\right\}
%
$$
%

- LHS is the ***matrix norm*** of ${\bf A}$
- RHS is ordinary Euclidean vector norms

In the maximization we can restrict attention to ${\bf x}$ s.t. $\| {\bf x} \| = 1$

To see this let
%
$$
%
a :=
\max_{{\bf x} \ne {\bf 0}} \frac{\| {\bf A} {\bf x} \|}{ \| {\bf x} \|} 
\qquad \text{and} \qquad
b :=
\max_{\| {\bf x} \| = 1} \frac{\| {\bf A} {\bf x} \|}{ \| {\bf x} \|} 
= \max_{\| {\bf x} \| = 1} \| {\bf A} {\bf x} \|
%
$$
%

Evidently $a \geq b$ because max is over a larger domain

To see the reverse let 

- ${\bf x}_a$ be the maximizer over ${\bf x} \ne {\bf 0}$ and
let $\alpha := 1 / \| {\bf x}_a\|$
- ${\bf x}_b := \alpha {\bf x}_a $ 

Then 
%
$$
%
b 
\geq \frac{ \| {\bf A} {\bf x}_b \| }{ \| {\bf x}_b \|}
= \frac{ \| \alpha {\bf A} {\bf x}_a \| }{ \| \alpha {\bf x}_a \|}
= \frac{\alpha}{\alpha} \frac{\| {\bf A} {\bf x}_a \|}{ \| {\bf x}_a \|}
= a
%
$$
%

**Exercise:** Show that for any ${\bf x}$ we have $\|{\bf A} {\bf x}\| \leq \| {\bf A} \| \| {\bf x} \|$

If $\| {\bf A} \| < 1$ then ${\bf A}$ is called ***contractive*** --- it
shrinks the norm

```{figure} _static/plots/contractive.png
:name: 

```

The matrix norm has similar properties to the Euclidean norm

```{admonition} Fact
:class: important

For conformable matrices ${\bf A}$ and ${\bf B}$, we have
```
%
1. $\| {\bf A} \| = {\bf 0}$ if and only if all entries of
${\bf A}$ are zero

- $\| \alpha {\bf A} \| = |\alpha| \| {\bf A} \|$ for any scalar
$\alpha$

- $\| {\bf A} + {\bf B} \| \leq \| {\bf A} \| + \| {\bf B} \|$

9. $\| {\bf A} {\bf B} \| \leq \| {\bf A} \| \| {\bf B} \|$

The last inequality is called the submultiplicative property of the matrix
norm

For square ${\bf A}$ it implies that $\|{\bf A}^k\| \leq \|{\bf A} \|^k$ for any $k \in \mathbb{N}$

```{admonition} Fact
:class: important

For the diagonal matrix
```
%
$$
%
{\bf D} = 
\mathrm{diag}(d_1, \ldots, d_N) 
=
\left(
\begin{array}{cccc}
d_1 & 0 & \cdots & 0 \\
0 & d_2 & \cdots & 0 \\
\vdots & \vdots & & \vdots \\
0 & 0 & \cdots & d_N \\
\end{array}
\right)
%
$$
%

we have

%
$$ 
%
\| {\bf D} \| = \max_n |d_n|
%
$$
%

Let $\{ {\bf A}_j \}$ and ${\bf A}$ be $N \times K$ matrices

- If $\| {\bf A}_j - {\bf A} \| \to 0$ then we say that ${\bf A}_j$
***converges*** to ${\bf A}$

- If $\sum_{j=1}^J {\bf A}_j$ converges to some matrix
${\bf B}_{\infty}$ as $J \to \infty$ we write
%
$$
%
\sum_{j=1}^{\infty} {\bf A}_j = {\bf B}_{\infty}
%
$$
%

In other words,
%
$$
%
{\bf B}_{\infty} = \sum_{j=1}^{\infty} {\bf A}_j 
\quad \iff \quad
\lim_{J \to \infty}
\;
\left\| \sum_{j=1}^J {\bf A}_j - {\bf B}_{\infty} \right\|
\to 0
%
$$
%

## Neumann Series

### Neumann Series

Consider the difference equation ${\bf x}_{t+1} = {\bf A} {\bf x}_t + {\bf b}$, where 
%
- ${\bf x}_t \in \mathbb{R}^N$ represents the values of some variables at time $t$

- ${\bf A}$ and ${\bf b}$ form the parameters in the law of motion for ${\bf x}_t$

Question of interest: is there an ${\bf x}$ such that 
%
$$
%
{\bf x}_t = {\bf x} \; \implies \; {\bf x}_{t+1} = {\bf x}
%
$$
%

In other words, we seek an ${\bf x} \in \mathbb{R}^N$ that solves the system of equations
%
$$
%
{\bf x} = {\bf A} {\bf x} + {\bf b}, 
\quad \text{where} \quad {\bf A} \text{ is } N \times N
\text{ and } {\bf b} \text{ is } N \times 1
%
$$
%

We can get some insight from the scalar case $x = a x + b$

If $|a| < 1$, then this equation has the solution
%
$$
%
\bar x 
= \frac{b}{1-a} 
= b \sum_{k=0}^{\infty} a^k 
%
$$
%

Does an analogous result hold in the vector case ${\bf x} = {\bf A} {\bf x} + {\bf b}$?

Yes, if we replace condition $|a| < 1$ with $\| {\bf A} \| < 1$ 

Let ${\bf b}$ be any vector in $\mathbb{R}^N$ and ${\bf A}$ be an $N \times N$ matrix

The next result is called the ***Neumann series lemma*** 

```{admonition} Fact
:class: important

If $\| {\bf A}^k \| < 1$ for some $k \in \mathbb{N}$, then ${\bf I} - {\bf A}$
```
is invertible and
%
$$
%
({\bf I} - {\bf A})^{-1} = \sum_{j=0}^{\infty} {\bf A}^j
%
$$
%

In this case ${\bf x} = {\bf A} {\bf x} + {\bf b}$ has the unique solution
%
$$
%
\bar {\bf x} = \sum_{j=0}^{\infty} {\bf A}^j {\bf b} 
%
$$
%

Sketch of proof that $({\bf I} - {\bf A})^{-1} = \sum_{j=0}^{\infty} {\bf A}^j$ 
for case $\|{\bf A} \| < 1$

We have $({\bf I} - {\bf A}) \sum_{j=0}^{\infty} {\bf A}^j =
{\bf I} $ because
%
$$
%
\left\|
({\bf I} - {\bf A}) \sum_{j=0}^{\infty} {\bf A}^j - {\bf I}
\right\|
& 
=
\left\|
({\bf I} - {\bf A}) \lim_{J \to \infty}\sum_{j=0}^J {\bf A}^j - {\bf I}
\right\|
\\
& 
=
\lim_{J \to \infty}
\left\|
({\bf I} - {\bf A}) \sum_{j=0}^J {\bf A}^j - {\bf I}
\right\|
\\
=
\lim_{J \to \infty}
\left\|
{\bf A}^J 
\right\|
\\
& \leq
\lim_{J \to \infty}
\left\| {\bf A} \right\|^J = 0
%
$$
%

How to test the hypotheses of the Neumann series lemma?

The ***spectral radius*** of square matrix ${\bf A}$ is
%
$$
%
\rho({\bf A}) := \max \{ |\lambda| \colon \lambda \text{ is an eigenvalue of \} {\bf A}}
%
$$
%

Here $|\lambda|$ is the ***modulus*** of the possibly complex number $\lambda$

```{admonition} Example
:class: tip

If $\lambda = a + ib$, then 
```
%
$$|\lambda| = (a^2 + b^2)^{1/2}$$
%

```{admonition} Example
:class: tip

If $\lambda \in \mathbb{R}$, then $|\lambda|$ is the absolute value
```

```{admonition} Fact
:class: important

If $\rho({\bf A}) < 1$, then $\| {\bf A}^j \| < 1$ for some $j \in \mathbb{N}$ 
```

Proof, for diagonalizable ${\bf A}$:

We have ${\bf A}^j = {\bf P} {\bf D}^j {\bf P}^{-1}$ where
%
$$
%
{\bf D} = \mathrm{diag}(\lambda_1, \ldots, \lambda_N)
\quad \text{and hence} \quad
{\bf D}^j = \mathrm{diag}(\lambda_1^j, \ldots, \lambda_N^j)
%
$$
%

Hence
%
$$
%
\| {\bf A}^j \|
= \| {\bf P} {\bf D}^j {\bf P}^{-1} \|
\leq \| {\bf P} \| \| {\bf D}^j \| \| {\bf P}^{-1} \|
%
$$
%

In particular, when $C := \| {\bf P} \|\| {\bf P}^{-1} \|$,
%
$$
%
\| {\bf A}^j \| 
\leq C \max_n |\lambda_n^j| 
= C \max_n |\lambda_n|^j
= C \rho({\bf A})^j
%
$$
%

This is $<1$ for large enough $j$ because $\rho({\bf A}) < 1$

## Quadratic Forms

### Quadratic Forms

Up till now we have studied linear functions extensively

Next level of complexity is quadratic maps

Let ${\bf A}$ be $N \times N$ and symmetric, and let ${\bf x}$ be $N \times 1$

The ***quadratic function*** on $\mathbb{R}^N$ associated with ${\bf A}$ is the
map 
%
$$
%
Q \colon \mathbb{R}^N \to \mathbb{R}, \qquad
Q({\bf x}) := {\bf x}' {\bf A} {\bf x} = \sum_{j=1}^N \sum_{i=1}^N a_{ij} x_i x_j
%
$$
%

The properties of $Q$ depend on ${\bf A}$

An $N \times N$ symmetric matrix ${\bf A}$ is called

1. ***nonnegative definite*** if ${\bf x}' {\bf A} {\bf x} \geq 0$
for all ${\bf x} \in \mathbb{R}^N$ 

- ***positive definite*** if ${\bf x}' {\bf A} {\bf x} > 0$ for all ${\bf x}
\in \mathbb{R}^N$ with ${\bf x} \ne {\bf 0}$

- ***nonpositive definite*** if ${\bf x}' {\bf A} {\bf x} \leq 0$
for all ${\bf x} \in \mathbb{R}^N$

- ***negative definite*** if ${\bf x}' {\bf A} {\bf x} < 0$ for all ${\bf x}
\in \mathbb{R}^N$ with ${\bf x} \ne {\bf 0}$

%

```{figure} _static/plots/qform_pd.png
:name: f:qform_pd

A positive definite case: $Q({\bf x}) = {\bf x}' {\bf I} {\bf x}$ 
```

```{figure} _static/plots/qform_nd.png
:name: f:qform_nd

A negative definite case: $Q({\bf x}) =
{\bf x}'(-{\bf I}){\bf x}$ 
```

Note that some matrices have none of these properties

- ${\bf x}' {\bf A} {\bf x} < 0$ for some ${\bf x}$

- ${\bf x}' {\bf A} {\bf x} > 0$ for other ${\bf x}$

In this case ${\bf A}$ is called ***indefinite***

```{figure} _static/plots/qform_indef.png
:name: f:qform_indef

Indefinite quadratic function $Q({\bf x}) = x_1^2/2 +
8 x_1 x_2 + x_2^2/2$ 
```

```{admonition} Fact
:class: important

A symmetric matrix ${\bf A}$ is 
```
%
1. positive definite $\iff$ all eigenvalues are strictly positive

- negative definite $\iff$ all eigenvalues are strictly negative

- nonpositive definite $\iff$ all eigenvalues are nonpositive

9. nonnegative definite $\iff$ all eigenvalues are nonnegative
%

It follows that 
%
- ${\bf A}$ is positive definite $\implies$ $\det({\bf A}) > 0$ 

In particular, ${\bf A}$ is nonsingular

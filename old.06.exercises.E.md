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

# Exercise set E


## Question E.1

Show that the function $f(x) = - |x|$ from $\mathbb{R}$ to $\mathbb{R}$ is concave.

## Question E.2

Let ${\bf A}$ be the $1 \times 1$ matrix $(a)$. Give a necessary and
sufficient condition on $a$ (that is, an "if and only if" condition on
$a$) under which ${\bf A}$ is nonsingular.

## Question E.3

Consider the function $f$ from $\mathbb{R}$ to $\mathbb{R}$ defined by
%
$$
%
f(x) = (c x)^2 + z
%
$$
%
Give a necessary and sufficient (if and only if) condition on $c$ under
which $f$ has a unique minimizer.

## Question E.4

Let ${\bf C}$ be an $N \times K$ matrix, let $z \in \mathbb{R}$ and consider the function
$f$ from $\mathbb{R}^K$ to $\mathbb{R}$ defined by
%
$$
%
f({\bf x}) = {\bf x}' {\bf C}' {\bf C} {\bf x} + z
%
$$
%
Show that $f$ has a unique minimizer on $\mathbb{R}^K$ if and only if ${\bf C}$
has linearly independent columns.

```{tip}
Obviously, you should
draw intuition from the preceding question. Also, what does linear
independence of the columns of ${\bf C}$ say about the vector ${\bf C}
{\bf x}$ for different choices of ${\bf x}$?
```

## Question E.5

Consider the maximization problem
%
$$
%
\max_{c_1, c_2} ( \sqrt c_1 + \beta \sqrt{c_2})
%
$$
%
subject to $c_1, c_2 \geq 0$ and $p_1 c_1 + p_2 c_2 \leq m$. 
Here $p_1, p_2$ and $m$ are nonnegative constants, and $\beta \in (0, 1)$.

Show that this problem has a solution if and only if $p_1$ and $p_2$ are both
strictly positive.

## Question E.6

Let $A$ be a nonempty bounded set and let $B := \{ b \in \mathbb{R} \colon b = 2a \text{ for some } a \in A\}$.
Obtain $\sup B$ in terms of $\sup A$. Justify your answer.




````{dropdown} Solutions

**Question E.1**

Pick any $x, y \in \mathbb{R}$ and any $\lambda \in [0, 1]$.
By the triangle inequality, we have
%
$$
%
|\lambda x + (1 - \lambda) y|
\leq |\lambda x| + |(1 - \lambda) y|
%
$$
%
and hence
%
$$
%
- |\lambda x + (1 - \lambda) y|
\geq - |\lambda x| - |(1 - \lambda) y|
= - \lambda |x| - (1 - \lambda) |y|
%
$$
%
That is, $f(\lambda x + (1 - \lambda) y) \geq \lambda f(x) + (1 -
\lambda)f(y)$. Hence $f$ is concave as claimed.

**Question E.2**

The condition for nonsingularity of $(a)$ is $a \ne 0$. There are many
ways we could show this. One is that ${\bf A}$ is nonsingular when ${\bf A}
{\bf x} = {\bf 0} \implies {\bf x} = {\bf 0}$. Here this translates to
$ax = 0 \implies x = 0$. The question then becomes, for what $a$ is this
implication true? It is true exactly when $a \ne 0$, for if $a
\ne 0$ and $ax=0$, the only possibility is that $x=0$.

**Question E.3**

The function $f$ has a unique minimizer at $x^* = 0$ if and only if $c
\ne 0$. Here's one proof: If $c \ne 0$ then the function is strictly
convex. Moreover, it is stationary at $x^* = 0$. Hence, by our facts on
minimization under convexity, $x^*$ is the unique minimizer. The
condition is necessary and sufficient because if $c = 0$, then $f$ is a constant
function, which clearly does not have a unique minimizer.

Here's a second (more direct) proof that the correct condition is $c
\ne 0$. Suppose first that $c \ne0$ and
pick any $x \in \mathbb{R}$. We have
%
$$
%
f(x) = (cx)^2 + z \geq z = f(0)
%
$$
%
This tells us that $x^* = 0$ is a minimizer. Moreover,
%
$$
%
f(x) = (cx)^2 + z > z = f(0)
\quad \text{whenever} \quad
x \ne x^*
%
$$
%
Hence $x^* = 0$ is the unique minimizer. 

Suppose next that $x^* = 0$ is the unique minimizer. Then it must be that $c
\ne0$, for if $c=0$ then $f(x) = f(x^*)$ for every $x \in \mathbb{R}$.

**Question E.4**

Suppose first that ${\bf C}$ has linearly independent columns. We claim
that ${\bf x} = {\bf 0}$ is the unique minimizer of $f$ on $\mathbb{R}^K$. To see
this observe that if ${\bf x} = {\bf 0}$ then $f({\bf x}) = z$. On the
other hand, if ${\bf x} \ne {\bf 0}$, then, by linear independence,
${\bf C}{\bf x}$ is not the origin, and hence $\| {\bf C}{\bf x} \| > 0$.
Therefore
%
$$
%
f({\bf x}) 
= {\bf x}' {\bf C}' {\bf C} {\bf x} + z
= ({\bf C} {\bf x} )' {\bf C} {\bf x} + z
= \| {\bf C} {\bf x} \|^2 + z > z
%
$$
%
Thus ${\bf x} = {\bf 0}$ is the unique minimizer of $f$ on $\mathbb{R}^K$ as
claimed. 

Since this is an "if and only if" proof we also need to show that when
$f$ has a unique minimizer on $\mathbb{R}^K$, it must be that ${\bf C}$ has
linearly independent columns. Suppose to the contrary that 
the columns of ${\bf C}$ are not linearly independent. We will show that
multiple minimizers exist.

Since $f({\bf x}) = \| {\bf C} {\bf x} \|^2 + z$ it is clear that $f({\bf x})
\geq z$, and hence ${\bf x} = {\bf 0}$ is one minimizer.
(At this point, $f$ evaluates to $z$.) Since
the columns of ${\bf C}$ are not linearly independent, there
exists a nonzero vector ${\bf y}$ such that ${\bf C} {\bf y} = {\bf 0}$.
At this vector we clearly have $f({\bf y}) = z$. Hence ${\bf y}$ is another
minimizer. 

**Question E.5**

First, show that $U(c_1, c_2) = \sqrt c_1 + \beta \sqrt{c_2}$ is continuous and that
%
$$
B := \{ (c_1, c_2) \colon c_i \geq 0 \text{ and }
p_1 c_1 + p_2 c_2 \leq m\}
$$
%
is closed. Hence, by the Weierstrass extreme value theorem, a maximizer
will exist whenever $B$ is bounded. If $p_1$ and $p_2$ are strictly
positive then $B$ is bounded. This is intuitive but we can also show it
formally by observing that $(c_1, c_2) \in B$ implies $c_i \leq m / p_i$
for $i =1,2$. Hence 
%
$$
%
{\bf c} := (c_1, c_2) \in B
\implies \| {\bf c} \|
\leq M := \sqrt{ \left(\frac{m}{p_1}\right)^2 
+ \left(\frac{m}{p_2}\right)^2 }
%
$$
%
We also need to show that if one price is zero then no maximizer exists.
Suppose to the contrary that $p_1 = 0$. Intuitively, no maximizer exists
because we can always consumer more of good one, thereby increasing our
utility. To formalize this we can
suppose that a maximizer exists and derive a contradiction. To this end,
suppose that ${\bf c}^* = (c_1^*,
c_2^*)$ is a maximizer of $U$ over $B$. Since $p_1 = 0$, 
the fact that $(c_1^*, c_2^*) \in B$ implies ${\bf c}^{**} := (c_1^* + 1,
c_2^*) \in B$. Since $U$ is strictly increasing in its first argument,
we also have $U({\bf c}^{**}) > U({\bf c}^*)$. This contradicts the
statement that ${\bf c}^*$ is a maximizer of $U$ over $B$.

**Question E.6**

Let $A$ and $B$ be as stated in the question. We claim that $\sup B =
\bar b$ where $\bar b := 2 \sup A$. According to the definition of the
supremum, to prove this we need to show that
%
1. $b \leq \bar b$ for all $b \in B$
9. $\bar b \leq u$ for all $u \in U(B)$
%
Regarding part 1, pick any $b \in B$. By definition, $b = 2a$ for some $a
\in A$. We know that $a \leq \sup A$ and hence $2 a \leq 2 \sup A$.
Therefore $b = 2a \leq \bar b$, as was to be shown.

Regarding part 2, take any $u \in U(B)$. For any $a \in A$ we have $2a
\in B$ and hence $2a \leq u$. Therefore $a \leq u/2$ for all $a \in A$,
and hence $u/2$ is an upper bound of $A$. Therefore $\sup A \leq u/2$.
Rearranging gives $\bar b \leq u$, as claimed.


````
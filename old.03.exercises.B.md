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

# Exercise set B

## Question B.1

Each of the definitions below is an attempt to define a set. Determine whether a set is indeed defined in each case, and if not explain why.

1. $\{1,e,-2,-\pi\}$
1. $\{15,\{1,2,3\},\text{ANU},\text{Europe},\text{USA}\}$
1. $\{1,2,\dots,99 \}$
1. $\{1,4,7,91, \dots \}$
1. $\{x \in \mathbb{R} \colon x^2 \le 5\}$
1. $\{(x,y) \in \mathbb{R}^2 \colon 5x^2 + y^2 \le 10\}$
1. $\{f \colon [0,1] \rightarrow \mathbb{R} \colon f \text{ is one-to-one} \}$
1. $\{ f_n(x) \colon [0,1] \rightarrow \mathbb{R} \colon f_n(x) = x^n \}$
1. $\{A \subset S : x_0 \in A \}$ for given $S$ and $x_0 \in S$


## Question B.2

Let $A$,$B$ and $C$ be any three sets.
Show that $A \cap (B \cup C) = (A\cap B) \cup (A \cap C)$.

```{hint}
Hint, if you need it: One way to show that $E=F$ is show that a arbitrary element of $E$ must also be in $F$ and vice versa.
```

## Question B.3

Let $A$, $B$, $C$ and $D$ be some set such that $A \subset C$ and $B \subset C$.
Let $f\colon D \rightarrow C$ be a function.

Show that $f^{-1}(A \setminus B) = f^{-1}(A) \setminus f^{-1}(B)$.

## Question B.4

Find the composition $g \circ f$ of two functions $f$ and $g$, if it exists:

1. $f \colon \mathbb{R} \rightarrow \mathbb{R}$ defined by $f(x)=\sin(x)$ and $g \colon \mathbb{R} \rightarrow \mathbb{R}$ defined by $g(x)= \frac{x}{1+x^2}$

2. $f \colon \mathbb{R} \rightarrow \mathbb{R}$ defined by $f(x)= 1-x^4$ and $g \colon (1,\infty) \rightarrow \mathbb{R}$ defined by $g(x)= \log(x-1)$

3. $f \colon \mathbb{R} \rightarrow \mathbb{R}$ defined by $f(x)=\cos(x)$ and $g \colon \mathbb{R}\setminus\{1\} \rightarrow \mathbb{R}$ defined by $g(x)= \frac{x}{1-x}$


```{hint}
Is there a composition in each case?
```

## Question B.5

Let $f$ and $g$ be any two functions from $\mathbb{R}$ to $\mathbb{R}$.  Is it true that
$g \circ f = f \circ g$ always holds?

```{hint}
There are two
things implicit in this question.  First, there is an implicit final
sentence here, which is: If yes, prove it.  If no, give a
counterexample.  Second, an equality sign between two functions means
that they are the same function.  Hence to show equality you need to
show that they agree everywhere on the domain.  To show inequality,
you need to give just one point in the domain where the function
values differ.
```

## Question B.6

```{admonition} Fact: the sufficient conditions for concavity/convexity in 2D

Let $z = f(x,y)$ be a twice continuously differentiable function defined for all
$(x, y) \in R^2$.

Then it holds:

- $f \text{ is convex } \iff f''_{1,1} \ge 0, \; f''_{2,2} \ge 0 , \text{ and } f''_{1,1} f''_{2,2} − (f''_{1,2})^2 \ge 0$

- $f \text{ is concave } \iff f''_{1,1} \le 0, \; f''_{2,2} \le 0 , \text{ and } f''_{1,1} f''_{2,2} − (f''_{1,2})^2 \ge 0$

- $f''_{1,1} > 0 \text{ and } f''_{1,1} f''_{2,2} \implies f \text{ is strictly convex}$

- $f''_{1,1} < 0 \text{ and } f''_{1,1} f''_{2,2} \implies f \text{ is strictly concave}$

```

1. Find the largest domain $S$ on which 
$f(x, y) = x^2 − y^2 − xy − x^3$ is concave.
2. How about strictly concave?


````{dropdown} Solutions

***Question B.1***

A set is _a collection of objects viewed as a whole_, see a precise definition.

Therefore:

1. Yes
1. Yes
1. Yes
1. No, no apparent pattern for a definition
1. Yes
1. Yes
1. Yes, all functions from $[0,1]$ to $\mathbb{R}$ form a set
1. No, as the set of $n$ is not specified
1. Yes

***Question B.2***

Let $A, B$ and $C$ be any three sets, as in the question.
Let
%

$$
E := A \cap (B \cup C)
\quad \text{and} \quad
F := (A \cap B) \cup (A \cap C)
$$

We need to show that $E = F$, or, equivalently, that $E \subset F$ and $F
\subset E$.

To see that $E \subset F$, pick any $x \in E$. We claim that $x \in F$ also
holds. To see this, observe that since $x \in E$, it must be true that $x$ is
in $A$ as well as being in at least one of $B$ and $C$. In the first case $x$
is in both $A$ and $B$. In the second case $x$ is in both $A$ and $C$. In
either case we have $x \in F$ by the definition of $F$.

To see that $F \subset E$, pick any $x \in F$. We claim that $x
\in E$ also holds. Indeed, since $x \in F$ we know that either $x$ is in both
$A$ and $B$ or $x$ is in both $A$ and $C$. In other words, $x$ is in $A$ and
also at least one of $B$ and $C$. Hence $x \in E$.

***Question B.3***

Note the definitions that $f^{-1}(A) := \{x\in D\colon f(x) \in A \}$ and $(f^{-1}(B))^c = \{x\in D\colon f(x) ∉  B\}$.
%
To show the equality we can prove the the left hand side (LHS) implies the right hand side (RHS), i.e. LHS $\Rightarrow$ RHS, and then show that RHS $\Rightarrow$ LHS. These two steps are usually referred to as
_necessity_ and _sufficiency_ (of the RHS for LHS).

**Necessity**: assume $x \in f^{-1}(A \setminus B)$, then $f(x) \in A$ and $f(x) \notin B$, and so $x \in f^{-1}(A)$ and $x \notin f^{-1}(B)$.

**Sufficiency**: if $x \in f^{-1}(A) \setminus f^{-1}(B)$, then $f(x) \in A$ and $f(x) \notin B$, and so $x \in f^{-1}(A \setminus B)$.

***Question B.4***

The issue we have to deal with is the compatibility of the domains and ranges of the functions.

1. All good
   %

   $$
   g \circ f \colon \mathbb{R} \rightarrow \mathbb{R}, \;\; (g \circ f)(x) = \frac{\sin(x)}{1+\sin^2(x)}
   $$

   %

2. The range of $f(x)$ and the domain of $g(x)$ are disjoint, so the composition is not defined.

3. The points where $f(x)=1$ have to be excluded in the composition
   %
   $$
   g \circ f \colon \mathbb{R}\setminus\{x: \cos(x)=1\} \rightarrow \mathbb{R}, \;\; (g \circ f)(x) = \frac{\cos(x)}{1-\cos(x)}
   $$
   %

***Question B.5***

This is not always true. For example, if $f(x) = x^2$ and
$g(x) = 4x$, then $g \circ f$ and $f \circ g$ differ. Indeed, if we set
$x=1$, then
%

$$
(g \circ f)(1) = g(f(1)) = 4(1^2) = 4,
$$

while

$$
(f \circ g)(1) = f(g(1)) = (4 \times 1)^2 = 16.
$$

%
Hence $g \circ f \not= f \circ g$ as claimed.

```{note}
Can you think of restrictions on $f$ and $g$ that would make the claim true?
```

***Question B.6***

1. $f^{\prime}_{1}(x, y) = 2x - y -3x^2$

   $f^{\prime}_{2}(x, y) = -2y - x$

   $f^{\prime\prime}_{1, 1}(x, y) = 2 - 6x$

   $f^{\prime\prime}_{2, 2}(x, y) = -2$

   $f^{\prime\prime}_{1, 2}(x, y) = -1$

   %
   $$
   f(x, y) \text{ is concave } \iff
   \begin{cases}
    f^{\prime\prime}_{1, 1}(x, y) = 2 - 6x \leq 0 \\
    f^{\prime\prime}_{2, 2}(x, y) = -2 \leq 0 \\
    f^{\prime\prime}_{1, 1}(x, y) f^{\prime\prime}_{2, 2}(x, y) - f^{\prime\prime}_{1, 2}(x, y)^2 = (2 - 6x)(-2) - (-1)^2 = 12x - 5 \geq 0 \\
   \end{cases} \\
   \iff x \geq \frac{5}{12}\\
   $$
   %
   Thus, $S = \{(x, y) \in \mathbb{R^2}: x \geq \frac{5}{12}\}= [\frac{5}{12}, +\infty) \times \mathbb{R}$.

2. We just replace all the inequality in question 1 to strict inequality, and we get $S = \{(x, y) \in \mathbb{R^2}: x > \frac{5}{12}\}= (\frac{5}{12}, +\infty) \times \mathbb{R}$.


````
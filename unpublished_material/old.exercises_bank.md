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

## Question E.2

Let ${\bf A}$ be the $1 \times 1$ matrix $(a)$. Give a necessary and
sufficient condition on $a$ (that is, an "if and only if" condition on
$a$) under which ${\bf A}$ is nonsingular.

## SOLUTION

The condition for nonsingularity of $(a)$ is $a \ne 0$. There are many
ways we could show this. One is that ${\bf A}$ is nonsingular when ${\bf A}
{\bf x} = {\bf 0} \implies {\bf x} = {\bf 0}$. Here this translates to
$ax = 0 \implies x = 0$. The question then becomes, for what $a$ is this
implication true? It is true exactly when $a \ne 0$, for if $a
\ne 0$ and $ax=0$, the only possibility is that $x=0$.



## Question E.6

Let $A$ be a nonempty bounded set and let $B := \{ b \in \mathbb{R} \colon b = 2a \text{ for some } a \in A\}$.
Obtain $\sup B$ in terms of $\sup A$. Justify your answer.


## SOLUTION

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






Suppose first that ${\bf C}$ has linearly independent columns. We claim
that ${\bf x} = {\bf 0}$ is the unique minimizer of $f$ on $\mathbb{R}^K$. To see
this observe that if ${\bf x} = {\bf 0}$ then $f({\bf x}) = z$. On the
other hand, if ${\bf x} \ne {\bf 0}$, then, by linear independence,
${\bf C}{\bf x}$ is not the origin, and hence $\| {\bf C}{\bf x} \| > 0$.
Therefore

$$
f({\bf x}) 
= {\bf x}' {\bf C}' {\bf C} {\bf x} + z
= ({\bf C} {\bf x} )' {\bf C} {\bf x} + z
= \| {\bf C} {\bf x} \|^2 + z > z
$$

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
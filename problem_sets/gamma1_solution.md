Let $A, B$ and $C$ be any three sets, as in the question.
Let

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
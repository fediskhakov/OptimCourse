Note the definitions that $f^{-1}(A) := \{x\in D\colon f(x) \in A \}$ and $(f^{-1}(B))^c = \{x\in D\colon f(x) \notin  B\}$.
%
To show the equality we can prove the the left hand side (LHS) implies the right hand side (RHS), i.e. LHS $\Rightarrow$ RHS, and then show that RHS $\Rightarrow$ LHS. These two steps are usually referred to as
_necessity_ and _sufficiency_ (of the RHS for LHS).

**Necessity**: assume $x \in f^{-1}(A \setminus B)$, then $f(x) \in A$ and $f(x) \notin B$, and so $x \in f^{-1}(A)$ and $x \notin f^{-1}(B)$.

**Sufficiency**: if $x \in f^{-1}(A) \setminus f^{-1}(B)$, then $f(x) \in A$ and $f(x) \notin B$, and so $x \in f^{-1}(A \setminus B)$.

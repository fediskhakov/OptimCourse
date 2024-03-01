First, we note that for $n=1$ the statement holds: $1 < 2^1$. This forms the bases for mathematical induction.

Second, assuming that the statement is true for $n$, i.e. $n < 2^n$, we need to prove that it holds for $n+1$, i.e. $n+1 < 2^{n+1}$.

1. multiplying both sides of $n < 2^n$ by 2 we have $2n < 2^{n+1}$
2. but $n+1 < 2n$ for all $n > 1$ because the difference $2n - (n+1) = n-1$ is always positive for $n > 1$
3. we have $n+1 < 2n < 2^{n+1}$, therefore taking the leftmost and rightmost inequality we have $n+1 < 2^{n+1}$

The first and the second parts together form the base of the induction and the induction step. The statement is therefore true for all $n=1,2,\dots$.
$\blacksquare$
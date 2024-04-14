In general a matrix can be decomposed into a symmetric and an anti-symmetric part as follows:

$$
M=\frac{1}{2}(M+M^T)+\frac{1}{2}(M-M^T)=M_s+M_a
$$

Note that the symmetric part is invariant to the transpose, $M^T_s=M_s$
while the antisymmetric part changes its sign under transposition:
$M^T_a=-M_a$

Let us examine the purely antisymmetric matrix

$$
q=x^T M_a x=(x^T M_a^T x)^T=-q
$$

Which implies that $q=0$ has to hold true for all $x$!

Then, it is clear that the $A = \frac{1}{2}(B+B^T)$ solves the problem.

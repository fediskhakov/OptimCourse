The answer is yes. Here's one proof: Suppose to the contrary that 
$\{\gamma {\bf x}_1, \gamma {\bf x}_2\}$ is linearly dependent. Then one
element can be written as a linear combination of the others. In our
setting with only two vectors, this translates to $\gamma {\bf x}_1 =
\alpha \gamma {\bf x}_2$ for some $\alpha$. Since $\gamma \ne 0$ we can
multiply each side by $1/\gamma$ to get ${\bf x}_1 = \alpha {\bf x}_2$. But
now each ${\bf x}_i$ is a multiple of the other. This contradicts linear
independence of $\{{\bf x}_1, {\bf x}_2\}$.

Here's another proof: Take any $\alpha_1, \alpha_2 \in \mathbb{R}$ with 

$$
\alpha_1 \gamma {\bf x}_1 + \alpha_2 \gamma {\bf x}_2 = {\bf 0}
$$

We need to show that $\alpha_1 = \alpha_2 = 0$. To see this, observe that

$$
\alpha_1 \gamma {\bf x}_1 + \alpha_2 \gamma {\bf x}_2 
= \gamma (\alpha_1 {\bf x}_1 + \alpha_2 {\bf x}_2)
$$

Hence $\gamma (\alpha_1 {\bf x}_1 + \alpha_2 {\bf x}_2) = {\bf 0}$.
Since $\gamma \ne 0$, the only way this could occur is that
$\alpha_1 {\bf x}_1 + \alpha_2 {\bf x}_2 = {\bf 0}$.
But $\{{\bf x}_1, {\bf x}_2\}$ is linearly independent, so this implies
that $\alpha_1 = \alpha_2 = 0$. The proof is done.

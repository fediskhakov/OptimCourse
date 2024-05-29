The function $f$ has a unique minimizer at $x^* = 0$ if and only if $c
\ne 0$. 

Here's one proof: If $c \ne 0$ then the function is strictly
convex. Moreover, it is stationary at $x^* = 0$. Hence, by our facts on
minimization under convexity, $x^*$ is the unique minimizer. The
condition is necessary and sufficient because if $c = 0$, then $f$ is a constant
function, which clearly does not have a unique minimizer.

Here's a second (more direct) proof that the correct condition is $c
\ne 0$. Suppose first that $c \ne0$ and
pick any $x \in \mathbb{R}$. We have

$$
f(x) = (cx)^2 + z \geq z = f(0)
$$

This tells us that $x^* = 0$ is a minimizer. Moreover,

$$
f(x) = (cx)^2 + z > z = f(0)
\quad \text{whenever} \quad
x \ne x^*
$$

Hence $x^* = 0$ is the unique minimizer. 

Suppose next that $x^* = 0$ is the unique minimizer. Then it must be that $c
\ne0$, for if $c=0$ then $f(x) = f(x^*)$ for every $x \in \mathbb{R}$.

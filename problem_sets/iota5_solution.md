First, note that $U(c_1, c_2) = \sqrt c_1 + \beta \sqrt{c_2}$ is continuous as a composition of continuous functions.
Then, observe that the admissible set

$$
B = \{ (c_1, c_2) \colon c_i \geq 0 \text{ and }
p_1 c_1 + p_2 c_2 \leq m\}
$$

is closed, all inequalities are weak.

Hence, by the Weierstrass extreme value theorem, a maximizer
will exist whenever $B$ is bounded. 

If $p_1$ and $p_2$ are strictly
positive then $B$ is bounded. This is intuitive but we can also show it
formally by observing that $(c_1, c_2) \in B$ implies $c_i \leq m / p_i$
for $i =1,2$. Hence 

$$
{\bf c} = (c_1, c_2) \in B
\implies \| {\bf c} \|
\leq M = \sqrt{ \left(\frac{m}{p_1}\right)^2 
+ \left(\frac{m}{p_2}\right)^2 }
$$

We also need to show that if one price is zero then no maximizer exists.
Suppose to the contrary that $p_1 = 0$. Intuitively, no maximizer exists
because we can always consumer more of good one, thereby increasing our
utility. 

To formalize this we can suppose that a maximizer exists and 
derive a contradiction. To this end,
suppose that ${\bf c}^* = (c_1^*, c_2^*)$ is a maximizer of $U$ over $B$. 
Since $p_1 = 0$, the fact that $(c_1^*, c_2^*) \in B$ implies 
${\bf c}^{**} = (c_1^* + 1, c_2^*) \in B$. 
Since $U$ is strictly increasing in its first argument,
we also have $U({\bf c}^{**}) > U({\bf c}^*)$. This contradicts the
statement that ${\bf c}^*$ is a maximizer of $U$ over $B$.

Now, to solve the problem explicitly, review the argument that the inequality 
$p_1 c_1 + p_2 c_2 \leq m$ can be replaced by an equality with no effect on the set of maximizers.
Indeed, if $p_1 c_1 + p_2 c_2 < m$ then we can increase $c_1$ or $c_2$ until the equality is satisfied, and because the criterion function is strictly increasing in each argument, the interior point is not a maximizer.

Inverting $p_1 c_1 + p_2 c_2 = m$ with respect to $c_2$ gives $c_2 = (m - p_1 c_1) / p_2$.

First, solve by substitution. The first order condition is

$$
\frac{d}{dc_1} \left( \sqrt{c_1} + \beta \sqrt{\tfrac{m}{p_2}-\tfrac{p_1}{p_2}c_1} \right) = 0
$$

$$
\frac{1}{2 \sqrt{c_1}} + \frac{\beta}{2\sqrt{\tfrac{m}{p_2}-\tfrac{p_1}{p_2}c_1}} \left( -\frac{p_1}{p_2} \right) = 0
$$

$$
\frac{1}{\sqrt{c_1}} =
\frac{p_1 \beta}{p_2\sqrt{\tfrac{m}{p_2}-\tfrac{p_1}{p_2}c_1}}
$$

$$
p_2\sqrt{\tfrac{m}{p_2}-\tfrac{p_1}{p_2}c_1}
=
p_1 \beta\sqrt{c_1}
$$

$$
p_2 (m-p_1c_1)
=
p_1^2 \beta^2 c_1
$$

$$
c_1 = \frac{p_2 m}{p_1^2 \beta^2 + p_1 p_2}
$$

It is convenient to check the second order conditions right away for the one dimensional problem. Simple derivation (left for exercise) yields that the second derivative is negative independent of $c_1$, and so the function $\sqrt{c_1} + \beta \sqrt{\tfrac{m}{p_2}-\tfrac{p_1}{p_2}c_1}$ is strictly concave.
Therefore, any point that satisfies the first order condition is a unique maximizer.

It is only left to find maximizing $c_2$ from the constraint.

$$
c_2 = \frac{m}{p_2} - \frac{p_1 c_1}{p_2} =
\frac{m}{p_2} - \frac{m}{p_1 \beta^2 + p_2} =
\frac{m p_1 \beta^2}{p_1 p_2 \beta^2 + p_2^2}
$$

To solve the problem using the tangency condition, recall that the maximizer is characterized by 

$$
\frac{f_1(x_1, x_2)}{f_2(x_1, x_2)}
= \frac{g_1(x_1, x_2)}{g_2(x_1, x_2)}
$$

where $f(x_1,x_2)$ is the criterion and $g(x_1,x_2)=0$ is the constraint, and the equality condition itself.

In our case $x_1=c_1$, $x_2=c_2$, and we have

$$
f_1(x_1, x_2) =
\frac{\partial }{\partial c_1} \left( \sqrt{c_1} + \beta \sqrt{c_2} \right) =
\frac{1}{2 \sqrt{c_1}}
$$

$$
f_2(x_1, x_2) =
\frac{\partial }{\partial c_2} \left( \sqrt{c_1} + \beta \sqrt{c_2} \right) =
\frac{\beta}{2 \sqrt{c_2}}
$$

$$
g_1(x_1, x_2) =
\frac{\partial }{\partial c_1} \left( p_1c_1 + p_2c_2 -m \right) = p_1
$$

$$
g_2(x_1, x_2) =
\frac{\partial }{\partial c_2} \left( p_1c_1 + p_2c_2 -m \right) = p_2
$$

Hence, the optimum is the solution of

$$
\begin{cases}
\frac{\sqrt{c_2}}{\beta \sqrt{c_1}} =
\frac{p_1}{p_2}
\\
p_1c_1 + p_2c_2 = m
\end{cases}
$$

Clearly, this system leads to the same equation as before after the substitution $c_2 = (m - p_1 c_1) / p_2$ is made.



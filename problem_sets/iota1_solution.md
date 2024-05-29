Combining the fact on definiteness of the Hessian of two-variate functions from the [lecture notes](https://optim.iskh.me/09.unconstrained.html#establishing-definiteness-of-hessian-in-mathbb-r-2-case) with the Hessian based conditions for convexity of functions, we can formulate the following fact.

```{admonition} Fact: the sufficient conditions for concavity/convexity in 2D

Let $z = f(x,y)$ be a twice continuously differentiable function defined for all
$(x, y) \in R^2$.

Then it holds:

- $f \text{ is convex } \iff f''_{1,1} \ge 0, \; f''_{2,2} \ge 0 , \text{ and } f''_{1,1} f''_{2,2} - (f''_{1,2})^2 \ge 0$

- $f \text{ is concave } \iff f''_{1,1} \le 0, \; f''_{2,2} \le 0 , \text{ and } f''_{1,1} f''_{2,2} - (f''_{1,2})^2 \ge 0$

- $f''_{1,1} > 0 \text{ and } f''_{1,1} f''_{2,2} \implies f \text{ is strictly convex}$

- $f''_{1,1} < 0 \text{ and } f''_{1,1} f''_{2,2} \implies f \text{ is strictly concave}$

```

The proof is a simple combination of the known facts named above.

Now we have 

$f^{\prime}_{1}(x, y) = 2x - y -3x^2$

$f^{\prime}_{2}(x, y) = -2y - x$

$f^{\prime\prime}_{1, 1}(x, y) = 2 - 6x$

$f^{\prime\prime}_{2, 2}(x, y) = -2$

$f^{\prime\prime}_{1, 2}(x, y) = -1$

$$
f(x, y) \text{ is concave } \iff
$$

$$
\begin{cases}
f^{\prime\prime}_{1, 1}(x, y) = 2 - 6x \leq 0 \\
f^{\prime\prime}_{2, 2}(x, y) = -2 \leq 0 \\
f^{\prime\prime}_{1, 1}(x, y) f^{\prime\prime}_{2, 2}(x, y) - f^{\prime\prime}_{1, 2}(x, y)^2 = (2 - 6x)(-2) - (-1)^2 = 12x - 5 \geq 0 \\
\end{cases}
$$

$$
\iff x \geq \frac{5}{12}\\
$$

Thus, $S = \{(x, y) \in \mathbb{R^2}: x \geq \frac{5}{12}\}= [\frac{5}{12}, +\infty) \times \mathbb{R}$.


For the strict concavity  we just replace all the inequalities to strict inequalities, and we get $S = \{(x, y) \in \mathbb{R^2}: x > \frac{5}{12}\}= (\frac{5}{12}, +\infty) \times \mathbb{R}$.


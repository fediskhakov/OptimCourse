---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Problems bank




## Question B.6

```{admonition} Fact: the sufficient conditions for concavity/convexity in 2D

Let $z = f(x,y)$ be a twice continuously differentiable function defined for all
$(x, y) \in R^2$.

Then it holds:

- $f \text{ is convex } \iff f''_{1,1} \ge 0, \; f''_{2,2} \ge 0 , \text{ and } f''_{1,1} f''_{2,2} − (f''_{1,2})^2 \ge 0$

- $f \text{ is concave } \iff f''_{1,1} \le 0, \; f''_{2,2} \le 0 , \text{ and } f''_{1,1} f''_{2,2} − (f''_{1,2})^2 \ge 0$

- $f''_{1,1} > 0 \text{ and } f''_{1,1} f''_{2,2} \implies f \text{ is strictly convex}$

- $f''_{1,1} < 0 \text{ and } f''_{1,1} f''_{2,2} \implies f \text{ is strictly concave}$

```

1. Find the largest domain $S$ on which 
$f(x, y) = x^2 − y^2 − xy − x^3$ is concave.
2. How about strictly concave?


````{admonition} Solutions
:class: caution

***Question B.6***

1. $f^{\prime}_{1}(x, y) = 2x - y -3x^2$

   $f^{\prime}_{2}(x, y) = -2y - x$

   $f^{\prime\prime}_{1, 1}(x, y) = 2 - 6x$

   $f^{\prime\prime}_{2, 2}(x, y) = -2$

   $f^{\prime\prime}_{1, 2}(x, y) = -1$

   %
   $$
   f(x, y) \text{ is concave } \iff
   \begin{cases}
    f^{\prime\prime}_{1, 1}(x, y) = 2 - 6x \leq 0 \\
    f^{\prime\prime}_{2, 2}(x, y) = -2 \leq 0 \\
    f^{\prime\prime}_{1, 1}(x, y) f^{\prime\prime}_{2, 2}(x, y) - f^{\prime\prime}_{1, 2}(x, y)^2 = (2 - 6x)(-2) - (-1)^2 = 12x - 5 \geq 0 \\
   \end{cases} \\
   \iff x \geq \frac{5}{12}\\
   $$
   %
   Thus, $S = \{(x, y) \in \mathbb{R^2}: x \geq \frac{5}{12}\}= [\frac{5}{12}, +\infty) \times \mathbb{R}$.

2. We just replace all the inequality in question 1 to strict inequality, and we get $S = \{(x, y) \in \mathbb{R^2}: x > \frac{5}{12}\}= (\frac{5}{12}, +\infty) \times \mathbb{R}$.


````
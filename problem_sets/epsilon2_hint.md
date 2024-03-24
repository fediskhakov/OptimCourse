You can assume that ${\bf x}$ is a column vector, and that any vector function of ${\bf x}$ is also a column vector.

:::{admonition} Definition
:class: caution

Let $A$ denote an open set in $\mathbb{R}^N$, and let $f \colon A \to \mathbb{R}$. Assume that $f$ is twice differentiable at $x \in A$.

The total derivative of the gradient of function $f$ at point $x$, $\nabla f(x)$ is called the **Hessian** matrix of $f$ denoted by $Hf$ or $\nabla^2 f$, and is given by a $N \times N$ matrix

$$
Hf(x) = \nabla^2 f(x) = 
\left(
\begin{array}{ccc}
\frac{\partial^2 f}{\partial x_1 \partial x_1}(x) & 
\cdots &
\frac{\partial^2 f}{\partial x_1 \partial x_N}(x) \\
\vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_N \partial x_1}(x) &
\cdots & 
\frac{\partial^2 f}{\partial x_N \partial x_N}(x)
\end{array}
\right)
$$
:::

From the definition of Euclidean norm, we have $\|{\bf x}\|^2 = \sum_{i=1}^{N}x_i^2$ where $x_i$ are components of ${\bf x}$. Therefore:

$$
\| {\bf x} + {\bf y} \|^2 + \| {\bf x} - {\bf y} \|^2 = \sum_{i=1}^{N}(x_i+y_i)^2 + \sum_{i=1}^{N}(x_i-y_i)^2 = \\
= \sum_{i=1}^{N} \Big( 2 x_i^2 + 2 x_i y_i - 2 x_i y_i + 2 y_i^2 \Big) = 2 \sum_{i=1}^{N}x_i^2 + 2 \sum_{i=1}^{N}y_i^2 = 2 \big( \| {\bf x} \|^2 + \| {\bf y} \|^2 \big)
$$

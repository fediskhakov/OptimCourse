**Proof** of $\lim_{i \to \infty} (\mathbf{x}_i + \mathbf{y}_i) = \mathbf{x} + \mathbf{y}$

Fix $\varepsilon > 0$.
Since $\mathbf{x}_i \to \mathbf{x}$ and $\mathbf{y}_i \to \mathbf{y}$, there exists an $N \in \mathbb{N}$ such that

$$
\|\mathbf{x}_i - \mathbf{x}\| < \frac{\varepsilon}{2} \qquad \text{and} \qquad  \|\mathbf{y}_i - \mathbf{y}\| < \frac{\varepsilon}{2}
$$

for all $i \geq N$.
Hence, the triangle inequality yields

$$
\|(\mathbf{x}_i + \mathbf{y}_i) - (\mathbf{x} + \mathbf{y})\| = \|\mathbf{x}_i - \mathbf{x} + \mathbf{y}_i - \mathbf{y}\| \leq \|\mathbf{x}_i - \mathbf{x}\| + \|\mathbf{y}_i - \mathbf{y}\|< \varepsilon
$$

for all $i \geq N$. Therefore, since $\varepsilon$ is arbitrary, we have $\mathbf{x}_i + \mathbf{y}_i \to \mathbf{x} + \mathbf{y}$ as $i \to \infty$.

**Proof** of $\lim_{i \to \infty} (\mathbf{x}_i' \mathbf{y}_i) = \mathbf{x}' \mathbf{y}$

Since $\{\mathbf{x}_i\}_{i=1}^\infty$ and $\{\mathbf{y}_i\}_{i=1}^\infty$ are convergent sequences, they are bounded (why?) by constants $M_x > 0$ and $M_y >0$, respectively.
That is, we have $\|\mathbf{x}_i\|\leq M_x$ and $\|\mathbf{y}_i\|\leq M_y$ for all $i\in\mathbb{N}$.

Let $M:= \max\{M_x, M_y, \|\mathbf{x}\|, \|\mathbf{y}\|\}$.
Fix $\varepsilon > 0$.
Again, since these sequences are convergent, there is an $N \in \mathbb{N}$ such that

$$
\|\mathbf{x}_i - \mathbf{x}\| < \frac{\varepsilon}{2M}, \qquad \text{and} \qquad \|\mathbf{y}_i - \mathbf{y}\| < \frac{\varepsilon}{2M}
$$

for all $i \geq N$.
The tirangle inequality and Cauchy-Schwarz inequality imply

$$
\begin{array}{l}
|\mathbf{x}_i' \mathbf{y}_i - \mathbf{x}'\mathbf{y}| 
= |\mathbf{x}_i' \mathbf{y}_i - \mathbf{x}' \mathbf{y}_i + \mathbf{x}' \mathbf{y}_i - \mathbf{x}'\mathbf{y}| \\
\leq |\mathbf{x}_i' \mathbf{y}_i - \mathbf{x}' \mathbf{y}_i| + |\mathbf{x}' \mathbf{y}_i - \mathbf{x}'\mathbf{y}| \\
= |(\mathbf{x}_i - \mathbf{x})' \mathbf{y}_i| + |\mathbf{x}'(\mathbf{y}_i-\mathbf{y})| \\
\leq \|\mathbf{y}_i\| \|\mathbf{x}_i-\mathbf{x}\| + \|\mathbf{x}\|\|\mathbf{y}_i - \mathbf{y}\| \\
\leq M \|\mathbf{x}_i - \mathbf{x}\| + M \|\mathbf{y}_i - \mathbf{y}\| \\
< M \frac{\varepsilon}{2M}+ M \frac{\varepsilon}{2M}< \varepsilon
\end{array}
$$

for all $i \geq N$.
Therefore, since $\varepsilon$ is arbitrary, we have $\mathbf{x}_i'\mathbf{y}_i \to \mathbf{x}'\mathbf{y}$ as $i \to \infty$.

**Proof** of "$\mathbf{x}_i \leq \mathbf{y}_i$ for all $i$ component-wise $\Longrightarrow \mathbf{x} \leq \mathbf{y}$"

Assume that $\mathbf{x}_i \leq \mathbf{y}_i$ for all $i$.
Toward contradiction, suppose that $\mathbf{x} \nleq \mathbf{y}$.
Then, there is $k\in\{1, 2, \dots, n\}$ such that $\mathbf{x}(k) > \mathbf{y}(k)$, where $\mathbf{x}(k)$ denotes the $k$-th component of $\mathbf{x} \in \mathbb{R}^n$.
Let $\varepsilon = \mathbf{x}(k) - \mathbf{y}(k) > 0$.
Since the convergences of $\{\mathbf{x}_i\}_{i=1}^\infty$ and $\{\mathbf{y}_i\}_{i=1}^\infty$ imply the convergences of $\{\mathbf{x}_i(k)\}_{i=1}^\infty$ and $\{\mathbf{y}_i(k)\}_{i=1}^\infty$ (why?),
there is an $N\in\mathbb{N}$ such that

$$
|\mathbf{x}_i(k) - \mathbf{x}(k)| < \frac{\varepsilon}{4} \qquad \text{and} \qquad |\mathbf{y}_i(k) - \mathbf{y}(k)| < \frac{\varepsilon}{4} \\
\Rightarrow \mathbf{x}_i(k) > \mathbf{x}(k) - \frac{\varepsilon}{4}  \qquad \text{and} \qquad \mathbf{y}_i(k) < \mathbf{y}(k) + \frac{\varepsilon}{4}
$$

for all $i \geq N$.
This implies that $\mathbf{x}_i(k) > \mathbf{y}_i(k)$ for all $i \geq N$.
To see this, observe that

$$
\mathbf{x}_i(k) - \mathbf{y}_i(k) > \mathbf{x}(k) - \frac{\varepsilon}{4} -  \Big(\mathbf{y}(k) +\frac{\varepsilon}{4}\Big)> \mathbf{x}(k) - \mathbf{y}(k) -\frac{\varepsilon}{2} = \varepsilon - \frac{\varepsilon}{2} = \frac{\varepsilon}{2}> 0
$$

for all $i \geq N$.
Since $\mathbf{x}_i(k)\leq \mathbf{y}_i(k)$ for all $i$ by assumption, we obtain a contraction, which implies that it must be $\mathbf{x} \leq \mathbf{y}$.


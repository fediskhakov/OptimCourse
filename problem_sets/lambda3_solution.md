> We first show the Roy's identity.

The value function is $v(p, m)=\max\{u(x): p \cdot x \leq m\}$ where $u\colon \mathbb{R}^{N}_{++}\to \mathbb{R}$.
The Lagrangian of the maximization problem is $\mathcal{L}(x, \lambda, p, m) = u(x) - \lambda (\sum_{i=1}^{N}p_{i}x_{i}-m)$.
The Envelope Theorem implies

$$
\frac{\partial v}{\partial p_{j}}=\frac{\partial\mathcal{L}}{\partial{p_{j}}}=-\lambda x_{j} \qquad (j=1,\dots, N)\\
\frac{\partial{v}}{\partial{m}}= \frac{\partial{\mathcal{L}}}{\partial{m}}=\lambda
$$

> Note, by the way, that here $\lambda$ is indeed the *shadow price of the budget constraint*: the slope of the indirect utility along the $m$ dimension is $\lambda$

It follows from the previous equations that 

$$
x_{j}=- \frac{1}{\lambda} \frac{\partial v}{\partial p_{j}} = - \frac{\partial v}{\partial p_{j}} \bigg/ \frac{\partial v}{\partial m}.
$$

Next, let $u(x)= \prod_{i=1}^{N}x_{i}^{\alpha_i}$ where $\alpha_i>0$ for all $i$.
Since $\log(\cdot)$ function is strictly monotone, the optimization problem is equivalent to maximize $u(x)=\sum_{i=1}^{N}\alpha_{i}\log(x_i)$.
The corresponding Lagrangian is 

$$
\mathcal{L}(x, \lambda, p, m) = \sum_{i=1}^{N}\alpha_{i}\log(x_{i}) - \lambda (\sum_{i}^{N}p_{i}x_{i}- m)
$$

The first-order conditions yield

$$
\frac{\partial\mathcal{L}}{\partial{x_{j}}}
= \frac{\alpha_{i}}{x_{j}}-\lambda p_{j=0} \qquad (j=1,\dots, N)\\
\frac{\partial\mathcal{L}}{\partial{\lambda}}
= \sum_{i}^{N}p_{i}x_{i}- m = 0 \\
\Longrightarrow \lambda
= \frac{\sum_{i=1}^{N}\alpha_{i}}{m}\\
x_{j}
= \frac{\alpha_{j}}{\lambda p_{j}} 
=\frac{\alpha_{j}}{\sum_{i=1}^{N}\alpha_{i}} \frac{m}{p_{j}}
$$

Hence, the optimal value function is 

$$
v(p,m)=u(x^{*}(p,m))=\prod_{i=1}^{N}\left(\frac{\alpha_{j}}{\sum_{i=1}^{N}\alpha_{i}} \frac{m}{p_{j}}\right)^{\alpha_{i}}
$$

To verify Roy's identity, observe that 

$$
\frac{\partial{v}}{\partial{p_{j}}}
=\frac{\partial}{\partial{p_{j}}} e^{\log v} 
= e^{\log v} \frac{\partial}{\partial{p_{j}}}\log v = v \frac{\partial}{\partial{p_{j}}}\log v\\
= v\frac{\partial}{\partial{p_{j}}}\left\{\sum_{i=1}^{N}\log\left(\frac{\alpha_{i}}{\sum_{i}\alpha_{i}}\right)+\alpha_{i}\log \frac{m}{p_{i}} \right\}\\
= v \left(\alpha_{j} \frac{1}{\frac{m}{p_{j}}}\frac{-m}{p_{j}^{2}} \right)
=\frac{-\alpha_j}{p_{j}}v
$$

$$
\frac{\partial{v}}{\partial{m}}
=v\frac{\partial}{\partial{p_{j}}} \log v \\
= v \sum_{i=1}^{N}\alpha_{i}\frac{1}{\frac{m}{p_{j}}} \frac{1}{p_{i}} = \frac{\sum_{i=1}^{N}\alpha_{i}}{m} v 
$$

Then, we have

$$
-\frac{\partial{v}}{\partial{p_{j}}}\Bigg/ \frac{\partial{v}}{\partial{m}}
=\frac{\frac{-\alpha_j}{p_{j}}v} {\frac{\sum_{i=1}^{N}\alpha_{i}}{m} v}
=\frac{\alpha_{j}}{\sum_{i=1}^{N}\alpha_{i}} \frac{m}{p_{j}} 
=x_{j}.
$$

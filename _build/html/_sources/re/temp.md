## Question K.2

The proof is very similar to the above, but FOC from the constrained optimization problem have to be used

See also the notes by Mark Walker
https://www.u.arizona.edu/~mwalker/MathCamp2020/EnvelopeTheorem.pdf

And his videos on Envelope theorems
- https://youtu.be/DiRwRERgglw?si=mKESOez0j4KiFpTz
- https://youtu.be/FX7kcDvEsJk?si=-BJ94gvkoxCK5XFn

Here is a version of proof. The Lagrangian is
$$\mathcal{L}(x^{*}(\theta),\lambda^{*}(\theta), \theta) = 
f(x^{*}(\theta),\theta)- \sum_{i=1}^{I}\lambda_{i}^{*}(\theta) g_{i}(x^{*}(\theta), \theta )$$
Fix $j=1,\dots,K$. Then, the partial derivative with respect to $\theta_{j}$ is 
$$
\begin{align*}
\frac{\partial\mathcal{L}(x^{*}(\theta), \lambda^{*}(\theta), \theta)}{\partial{\theta_{j}}}
&= 
\frac{\partial f(x^{*}(\theta),  \theta)}{\partial{\theta_{j}}} 
- \sum_{i=1}^{I} \frac{\partial\lambda_{i}^{*}(\theta)}{\partial \theta_{j}}g_{i}(x^{*}(\theta), \theta) + \lambda_{i}^{*} \frac{\partial g_{i}(x^{*}(\theta), \theta) }{\partial \theta_{j}} \\
&= \frac{\partial f(x^{*}(\theta),  \theta)}{\partial{\theta_{j}}} 
- \sum_{i=1}^{I} \lambda_{i}^{*} \frac{\partial g_{i}(x^{*}(\theta), \theta) }{\partial \theta_{j}} 
\end{align*}
$$
where the last equality follows from the equality constraints $g_{i}(x^{*}(\theta), \theta)=0$ for all $i$.
The partial derivative of value function is
$$
\begin{align*}
\frac{\partial\mathcal{v}(\theta)}{\partial{\theta_{j}}}
&= 
\frac{d f(x^{*}(\theta), \lambda^{*}(\theta), \theta)}{d \theta_{j}} \\ 
&=  \sum_{n=1}^{N} \frac{\partial f(x^{*}(\theta), \theta)}{\partial x_{n}} \frac{dx^{*}}{ \theta_{j}} 
+\frac{\partial f(x^{*}(\theta), \theta) }{\partial \theta_{j}} \\
&= \sum_{n=1}^{N} \left(\sum_{i=1}^{I}\lambda_{i} \frac{\partial g_i(x^{*}(\theta), \theta)}{\partial x_{n}} \right)\frac{\partial x_{n}(\theta)}{ \partial \theta_{j}} 
+\frac{\partial f(x^{*}(\theta), \theta) }{\partial \theta_{j}} \\
&= \sum_{i=1}^{I}\lambda_{i} \sum_{n=1}^{N}  \frac{\partial g_i(x^{*}(\theta), \theta)}{\partial x_{n}}\frac{\partial x_{n}(\theta)}{\partial\theta_{j}} 
+\frac{\partial f(x^{*}(\theta), \theta) }{\partial \theta_{j}} \\
&= - \sum_{i=1}^{I}\lambda_{i}  \frac{\partial g_i(x^{*}(\theta), \theta)}{\partial \theta_j}
+\frac{\partial f(x^{*}(\theta), \theta) }{\partial \theta_{j}}\\
&= \frac{\partial\mathcal{L}(x^{*}(\theta), \lambda^{*}(\theta), \theta)}{\partial{\theta_{j}}}
\end{align*}
$$
where the third equality follows from the first-order conditions,
$$
\begin{align*}
0 = \frac{\partial\mathcal{L}(x^{*}(\theta), \lambda^{*}(\theta), \theta)}{\partial{x_n}}
&= 
\frac{\partial f(x^{*}(\theta),  \theta)}{\partial{x_n}} 
- \sum_{i=1}^{I} \lambda_{i}^{*}(\theta) \frac{\partial g_{i}(x^{*}(\theta), \theta) }{\partial x_{n}}, \\
\end{align*}
$$
and the fifth equality follows from the constraint and its total derivative
$$g_{i}(x^{*}(\theta), \theta)=0\\ \Longrightarrow 
\sum_{n=1}^{N}  \frac{\partial g_i(x^{*}(\theta), \theta)}{\partial x_{n}}\frac{\partial x_{n}(\theta)}{ \partial\theta_{j}} 
+ \frac{\partial g_i(x^{*}(\theta), \theta)}{\partial \theta_{j}}= 0
$$


## Question K.3

We first show the Roy's identity.
The value function is $v(p, m)=\max\{u(x): p \cdot x \leq m\}$ where $u\colon \mathbb{R}^{N}_{++}\to \mathbb{R}$.
The Lagrangian of the maximization problem is $\mathcal{L}(x, \lambda, p, m) = u(x) - \lambda (\sum_{i=1}^{N}p_{i}x_{i}- m)$. 
The Envelope Theorem implies
$$
\begin{align*}
&\frac{\partial V}{\partial p_{j}}=\frac{\partial\mathcal{L}}{\partial{p_{j}}}=-\lambda x_{j} \qquad (j=1,\dots, N)\\
&\frac{\partial{V}}{\partial{m}}= \frac{\partial{\mathcal{L}}}{\partial{m}}=\lambda
\end{align*}
$$
It follows from the previous equations that 
$$x_{j}=- \frac{1}{\lambda} \frac{\partial V}{\partial p_{j}} = - \frac{\partial V}{\partial p_{j}} \bigg/ \frac{\partial V}{\partial m}.$$
Next, let $u(x)= \prod_{i=1}^{N}x_{i}^{\alpha_i}$ where $\alpha_i>0$ for all $i$.
Since $\log(\cdot)$ function is strictly monotone, the optimization problem is equivalent to maximize $u(x)=\sum_{i=1}^{N}\alpha_{i}\log(x_i)$.
The corresponding Lagrangian is 
$$\mathcal{L}(x, \lambda, p, m) = \sum_{i=1}^{N}\alpha_{i}\log(x_{i}) - \lambda (\sum_{i}^{N}p_{i}x_{i}- m)$$
The first-order conditions yield
$$
\begin{align*}
\frac{\partial\mathcal{L}}{\partial{x_{j}}}&= \frac{\alpha_{i}}{x_{j}}-\lambda p_{j=0} \qquad (j=1,\dots, N)\\
\frac{\partial\mathcal{L}}{\partial{\lambda}}&= \sum_{i}^{N}p_{i}x_{i}- m = 0 \\
\Longrightarrow \lambda&= \frac{\sum_{i=1}^{N}\alpha_{i}}{m}\\
x_{j}&= \frac{\alpha_{j}}{\lambda p_{j}} 
=\frac{\alpha_{j}}{\sum_{i=1}^{N}\alpha_{i}} \frac{m}{p_{j}}
\end{align*}
$$
Hence, the optimal value function is 
$$v(p,m)=u(x^{*}(p,m))=\prod_{i=1}^{N}\left(\frac{\alpha_{j}}{\sum_{i=1}^{N}\alpha_{i}} \frac{m}{p_{j}}\right)^{\alpha_{i}}$$
To verify Roy's identity, observe that 
$$
\begin{align*}
\frac{\partial{v}}{\partial{p_{j}}}&=\frac{\partial}{\partial{p_{j}}} e^{\log v} 
= e^{\log v} \frac{\partial}{\partial{p_{j}}}\log v = v \frac{\partial}{\partial{p_{j}}}\log v\\
&= v\frac{\partial}{\partial{p_{j}}}\left\{\sum_{i=1}^{N}\log\left(\frac{\alpha_{i}}{\sum_{i}\alpha_{i}}\right)+\alpha_{i}\log \frac{m}{p_{i}} \right\}\\
&= v \left(\alpha_{j} \frac{1}{\frac{m}{p_{j}}}\frac{-m}{p_{j}^{2}}  \right)
=\frac{-\alpha_j}{p_{j}}v \\
\frac{\partial{v}}{\partial{m}}&=v\frac{\partial}{\partial{p_{j}}} \log v \\
&= v \sum_{i=1}^{N}\alpha_{i}\frac{1}{\frac{m}{p_{j}}} \frac{1}{p_{i}} = \frac{\sum_{i=1}^{N}\alpha_{i}}{m} v 
\end{align*}
$$
Then, we have
$$
-\frac{\partial{v}}{\partial{p_{j}}}\Bigg/ \frac{\partial{v}}{\partial{m}}
=\frac{\frac{-\alpha_j}{p_{j}}v} {\frac{\sum_{i=1}^{N}\alpha_{i}}{m} v}
=\frac{\alpha_{j}}{\sum_{i=1}^{N}\alpha_{i}} \frac{m}{p_{j}} 
=x_{j}.
$$


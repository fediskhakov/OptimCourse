1.

Let's prove that $\lim_{n \to \infty} \frac{1}{n} = 0$ using the definition of a limit.

First pick an arbitrary $\epsilon > 0$. Now we have to come up with an $N$ such that 
$$
n \geq N
\implies
|1/n - 0| < \epsilon
$$

Let $N$ be the first integer greater than $1/\epsilon$. Then 
$$
n \geq N 
\implies n > 1/\epsilon 
\implies 1/n < \epsilon 
\implies |1/n - 0| < \epsilon 
$$

2. 

$$
\begin{array}{l}
\lim_{n \to \infty} \frac{n+2}{2n+1} = 
\lim_{n \to \infty} \frac{1+2/n}{2+1/n} = \\ =
\frac{1+\lim_{n \to \infty}2/n}{2+\lim_{n \to \infty}1/n} =
\frac{1+0}{2+0} = \frac{1}{2}
\end{array}
$$

3. 

$$
\begin{array}{l}
\lim_{n \to \infty} \frac{2n^2(n-2)}{(1-3n)(2+n^2)} = 
\lim_{n \to \infty} \frac{2n^3-4n^2}{2+n^2-6n-3n^3} = \\ =
\lim_{n \to \infty} \frac{2-4/n}{2/n^3+1/n-6/n^2-3} =
\frac{2-\lim_{n \to \infty}4/n}{\lim_{n \to \infty}2/n^3+\lim_{n \to \infty}1/n-\lim_{n \to \infty}6/n^2-3} = \\ =
\frac{2-0}{0+0-0-3} = -\frac{2}{3}
\end{array}
$$

4.

Note that the factorial operation is defined as $(n+1)! = (n+1)n(n-1)\cdot .. \cdot 1$

$$
\begin{array}{l}
\lim_{n \to \infty} \frac{(n+1)!}{n! - (n+1)!} =
\lim_{n \to \infty} \frac{(n+1)n!}{n!(1- (n+1))} = \\ =
\lim_{n \to \infty} \frac{n+1}{1- n -1} = 
\lim_{n \to \infty} \frac{1+1/n}{(-1)} = \\ =
\frac{1+\lim_{n \to \infty} 1/n}{(-1)} =
-\frac{1+0}{1} = -1
\end{array}
$$

5.

$$
\begin{array}{l}
\lim_{n \to \infty} \sqrt{\frac{9+n^2}{4n^2}} =
\sqrt{\lim_{n \to \infty} \frac{9/n^2+1}{4}} = \\ =
\sqrt{\frac{\lim_{n \to \infty}9/n^2+1}{4}} = 
\sqrt{\frac{0+1}{4}} = \frac{1}{2}
\end{array}
$$

Following the algorithm for the univariate optimization from the lecture notes

1. Locate all stationary points
  - according to the definition the stationary points are those interior points where $f'(x) = 0$

$$
f'(x) = \frac{d}{dx} \left( \frac{e^x}{x} \right) = \frac{e^x}{x} -\frac{1}{x^2} e^x = \frac{e^x}{x^2} \left( x - 1 \right)
$$
$$
f'(x) =0 \iff x=1 
$$


2. Evaluate the function at the stationary points and the boundaries, in our case only one boundary $x=2$.

$$
f(1) = e \approx 2.718, \; f(2) = \frac{e^2}{2} \approx 3.694 \
$$ 

Evaluating the function at $x=0$ is not possible because the function is not defined there!  We have to be careful and investigate the behavior of the function as $x$ approaches $0$.

Because $exp(x)$ is always positive, for small values of $x$ the function takes on large numbers.  The smaller $x$ is, the larger the function becomes.  This means that the function is unbounded as $x$ approaches $0$ (from the right).  Therefore, we could move forward taking $f(0) = \infty$.

3. Compare the values of the function at the stationary points and the boundaries to pick out the solution.

The minimizer of the function on $(0,2]$ is $x=1$ because $\min\{e,e^2/2,\infty\} = e$.

The maximizer of the function could be $x=0$ because $\max\{e,e^2/2,\infty\} = \infty$, but as the function is not defined at $x=0$. We showed that the function grows without bound as $x$ becomes closer and closer to 0, therefore it is impossible to find a precise $x$ where it attains the maximum value (there is always possible to make a step towards zero to increase the function a little more).
The conclusion is that there is no maximizer on $[0,2]$.

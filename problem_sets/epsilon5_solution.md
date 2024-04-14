Denote $(x_0,y_0) = (4,-2)$, and $v = (1/\sqrt{10},3/\sqrt{10})$.

Note that $\|v\| = \sqrt{(1/\sqrt{10})^2+(3/\sqrt{10})^2} = (1+3^2)/10 = 1$.

**First approach**

Let $g(h)$ denote the univariate function of $h$ obtained by slicing the function $f(x,y)$ through the point $(x_0,y_0)$ in the direction of the vector $v$:

$$
g(h) = f(x_0+hv_1,y_0+hv_2) = (x_0+hv_1)(y_0+hv_2)^2 + (x_0+hv_1)^3(y_0+hv_2)
$$

We have 

$$
\begin{array}{l}
\frac{d g(h)}{dh} = v_1(y_0+hv_2)^2 + 2v_2(x_0+hv_1)(y_0+hv_2) +
3v_1(x_0+hv_1)^2(y_0+hv_2)+v_2(x_0+hv_1)^3 \\
\frac{d g(0)}{dh} = v_1 y_0^2 + 2v_2 x_0 y_0 + 3v_1 x_0^2 y_0 + v_2 x_0^3
\end{array}
$$

Evaluating the last expression at the given $(x_0,y_0)$ and $v$ we get

$$
\begin{array}{l}
\frac{d g(0)}{dh} = 
(1/\sqrt{10}) (-2)^2 + 2 (3/\sqrt{10})4(-2) + 3 (1/\sqrt{10}) 4^2 (-2) + (3/\sqrt{10}) 4^3 = \\ = (4-48-96+192)/\sqrt{10} = 52/\sqrt{10}
\end{array}
$$

**Second approach**

Compute the partial derivatives and the gradient

$$
\begin{array}{l}
\frac{\partial f(x,y)}{\partial x} = y^2+3x^2y \\
\frac{\partial f(x,y)}{\partial y} = 2xy+x^3 \\
\nabla f(x,y) = \left( y^2+3x^2y, 2xy+x^3 \right) \\
D_v f(x_0,y_0) = \nabla f(x_0,y_0) \cdot v = (y_0^2+3x_0^2y_0, 2x_0y_0+x_0^3) \cdot (1/\sqrt{10},3/\sqrt{10}) = \\ = ((-2)^2+3\cdot 4^2(-2), 2\cdot 4(-2)+4^3) \cdot (1/\sqrt{10},3/\sqrt{10}) = \\ = (4-96, -16+64) \cdot (1/\sqrt{10},3/\sqrt{10}) = \\ = (-92,48) \cdot (1/\sqrt{10},3/\sqrt{10}) = -92/\sqrt{10} + 48\cdot 3/\sqrt{10} = 52/\sqrt{10}
\end{array}
$$

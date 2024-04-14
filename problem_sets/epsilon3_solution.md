The direction of most rapid ascent of the multivariate function is given by its gradient.

**1.**

$$
\begin{array}{l}
\partial f(x,y)/\partial x = 8xy \\
\partial f(x,y)/\partial y = 4x^2 \\
\nabla f(x,y) = (8xy, 4x^2) \\
\nabla f(2,3) = (48, 16)
\end{array}
$$

We need to make sure that the direction vector had length 1, so we divide by its norm 

$$
\|(48, 32)\| = \sqrt{48^2+16^2} = \sqrt{2^{8}3^{2}+2^8} = 2^4 sqrt{10}
$$

The direction vector is then $(48, 16)/16\sqrt{10} = (3/\sqrt{10}, 1/\sqrt{10})$

**2.**

$$
\begin{array}{l}
\partial f(x,y)/\partial x = 3 y^2 e^{3x} \\
\partial f(x,y)/\partial y = 2y e^{3x} \\
\nabla f(x,y) = (3 y^2 e^{3x}, 2y e^{3x}) = e^{3x} (3 y^2, 2y) \\
\nabla f(0,3) = (27, 6)
\end{array}
$$

We need to make sure that the direction vector had length 1, so we divide by its norm 

$$
\|(27, 6)\| = \sqrt{27^2+6^2} = \sqrt{3^{6}+3^2 2^2} = 3 \sqrt{81+4}
$$

The direction vector is then $(27, 6)/3\sqrt{85} = (9/\sqrt{85}, 2/\sqrt{85})$

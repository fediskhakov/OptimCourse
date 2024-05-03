**Ellipse**

Let focal points of ellipse be located at $(c,0)$ and $(-c,0)$, and consider an arbitrary point $(x,y) \in \mathbb{R}^2$ which satisfies the defining property of the ellipse, namely the sum of distances from $(x,y)$ to the focal points is constant denoted $2d$.

$$
\begin{array}{rcl}
\sqrt{(x-c)^2 + y^2} + \sqrt{(x+c)^2 + y^2} &=& 2d \\
\sqrt{(x-c)^2 + y^2} &=& 2d - \sqrt{(x+c)^2 + y^2} \\
(x-c)^2 + y^2 &=& 4d^2 - 4d\sqrt{(x+c)^2 + y^2} + (x+c)^2 + y^2 \\
4d\sqrt{(x+c)^2 + y^2} &=& 4d^2 +4xc \\ 
d^2(x+c)^2 + d^2y^2 &=& d^4 +2xcd^2 +x^2c^2 \\ 
x^2d^2 + 2xcd^2 + c^2d^2 + d^2y^2 &=& d^4 +2xcd^2 +x^2c^2 \\ 
x^2 (d^2-c^2) + y^2d^2 &=& d^4 - c^2d^2
\end{array}
$$

$$
\frac{x^2}{d^2} + \frac{y^2}{d^2-c^2} = 1
$$

That is, the canonical parameters $a^2 = d^2$ and $b^2 = d^2-c^2$. Ellipse intersects the $x$-axis at $x = \pm a$ and $y$-axis at $y = \pm b$.

The focal points in canonical parameters are located at $(\sqrt{a^2-b^2},0)$ and $(-\sqrt{a^2-b^2},0)$.

**Parabola**

Let the focal point of parabola be located at $(0,c)$ and the dirextrix at $y=-c$. Consider an arbitrary point $(x,y) \in \mathbb{R}^2$ which satisfies the defining property of the parabola, namely the distance from $(x,y)$ to the focal point is equal to the distance from $(x,y)$ to the directrix $y=-c$. The latter is equal to the distance from the projection of the point $(x,y)$ to point $(0,-c)$ where the directrix crosses $y$-axis.

$$
\begin{array}{rcl}
\sqrt{x^2+(y-c)^2}
&=&
y+c \\
x^2+(y-c)^2
&=&
y^2+2yc+c^2 \\
x^2+y^2-2yc+c^2
&=&
y^2+2yc+c^2 \\
x^2 &=& 4yc
\end{array}
$$

That is, the canonical parameter for parabola is $p = 2c$, the distance from the focal point to the directrix. The vertex of the parabola is in the origin, half way between.

**Hyperbola**

Again, let the focal points be located at $(c,0)$ and $(-c,0)$, and consider an arbitrary point $(x,y) \in \mathbb{R}^2$ which satisfies the defining property of the hyperbola, namely the difference of distances from $(x,y)$ to the focal points is constant denoted $2d$.

$$
\begin{array}{rcl}
\sqrt{(x+c)^2 + y^2} - \sqrt{(x-c)^2 + y^2} &=& 2d \\
\sqrt{(x+c)^2 + y^2} &=& 2d + \sqrt{(x-c)^2 + y^2} \\
(x+c)^2 + y^2 &=& 4d^2 + 4d\sqrt{(x-c)^2 + y^2} + (x-c)^2 + y^2 \\
4d\sqrt{(x-c)^2 + y^2} &=& 4xc - 4d^2 \\ 
d^2(x-c)^2 + d^2y^2 &=& x^2c^2-2xcd^2+d^4 \\ 
x^2d^2 -2xcd^2 +c^2d^2 + d^2y^2 &=& x^2c^2-2xcd^2+d^4 \\ 
x^2 (c^2-d^2) - y^2d^2 &=& d^2(c^2 - d^2)
\end{array}
$$

$$
\frac{x^2}{d^2} - \frac{y^2}{d^2-c^2} = 1
$$

That is, again the canonical parameters $a^2 = d^2$ and $b^2 = d^2-c^2$. 

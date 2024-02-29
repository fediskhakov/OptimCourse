This is a creative problem which has many possible correct answers.

As always, start with the definitions---in this case definitions of maximizer and minimizer.

Here is one possible solution:

(a) any linear (affine) function $f(x)=ax+b$, $a \ne 0$ on any _close_ interval $[A,B]$ has no stationary points, and therefore exactly one maximizer and one minimizer at the edges of the interval.
(b) any linear (affine) function $f(x)=ax+b$, $a \ne 0$ on any _open_ interval $(A,B)$ has no maximizer and no minimizer similarly to the no existence example in the lecture notes.  A different idea would be to rely on positive and negative infinity in the domain $D$, for example, let $f(x) = \tan(\pi x)$ which takes values $0$ on all integer points, and approaches a vertical line at every half-integer point.
(c) A constant function $f(x) = C$ should immediately come to mind.  Another possibility is the cyclic trigonometric functions like $f(x) = \sin(x)$ or $f(x) = \cos(x)$ on the entire real line.  The latter only return values between -1 and 1, and attain these two values infinitely many times.
(d) This is the most tricky question, but one solution is to adjust the domain of the trig function such as $f(x) = \cos(\pi x)$.  This function attains 1 at $x=\{...,-2,0,2,4,...\}$ and attains 0 at $x=\{...,-3,-1,1,3,5,...\}$. Therefore, it has exactly $n$ maximizers and $n$ minimizers if we define $D = [0,2n+1]$.


Let $T \colon \mathbb{R}^N \to \mathbb{R}^N$ be nonsingular and let $T^{-1}$
be its inverse. To see that $T^{-1}$ is linear we need to show that for any
pair ${\bf x}, {\bf y}$ in $\mathbb{R}^N$ (which is the domain of $T^{-1}$) and any
scalars $\alpha$ and $\beta$, the following equality holds:
%
$$
T^{-1}(\alpha {\bf x} + \beta {\bf y}) = \alpha T^{-1}{\bf x} + \beta T^{-1} {\bf y}.
$$ 
%
In the proof we will exploit the fact that $T$ is by assumption a linear
bijection.

So pick any vectors ${\bf x}, {\bf y} \in \mathbb{R}^N$ and any two scalars $\alpha,
\beta$. Since $T$ is a bijection, we know that ${\bf x}$ and ${\bf y}$ have
unique preimages under $T$. In particular, there exist unique vectors
${\bf u}$ and ${\bf v}$ such that
%
$$
%
T{\bf u} = {\bf x} 
\quad \text{and} \quad
T{\bf v} = {\bf y} 
%
$$
%
Using these definitions, linearity of $T$ and the fact that $T^{-1}$ is the
inverse of $T$, we have
%
$$
%
T^{-1}(\alpha {\bf x} + \beta {\bf y})
= T^{-1}(\alpha T{\bf u} + \beta T {\bf v}) \\
= T^{-1}(T(\alpha {\bf u} + \beta {\bf v})) \\
= \alpha {\bf u} + \beta {\bf v} \\
= \alpha T^{-1} {\bf x} + \beta T^{-1} {\bf y}.
%
$$
%
This chain of equalities confirms
%
$$
T^{-1}(\alpha {\bf x} + \beta {\bf y}) = \alpha T^{-1}{\bf x} + \beta T^{-1} {\bf y}.
$$
%
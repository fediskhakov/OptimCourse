1. $f(x) = 3x-7$
  - Domain: $\mathbb{R}$
  - Range: $\mathbb{R}$
  - One-to-one? `Yes`
  - Onto? `Yes`
  - Bijective? `Yes`
  - Inverse: $f^{-1}(y) = \frac{y+7}{3}$

2. $f(x) = e^x$
  - Domain: $\mathbb{R}$
  - Range: $\mathbb{R}_{++} = \{x \in \mathbb{R}: x>0\}$
  - One-to-one? `Yes`
  - Onto? `No`, not on $\mathbb{R}$, but if we restrict the domain to $\mathbb{R}_{++}$, then `Yes`, we can think of $f(x)$ as a surjection (onto) from $\mathbb{R}$ to $\mathbb{R}_{++}$
  - Bijective? `No` for $f(x): \mathbb{R} \to \mathbb{R}$, `Yes` for $f(x): \mathbb{R} \to \mathbb{R}_{++}$
  - Inverse: $f^{-1}: \mathbb{R}_{++} \ni y \mapsto \ln(y) \in \mathbb{R}$

3. $f(x) = \ln(x)$
  - Domain: $\mathbb{R}_{++} = \{x \in \mathbb{R}: x>0\}$
  - Range: $\mathbb{R}$
  - One-to-one? `Yes`
  - Onto? `Yes`
  - Bijective? `Yes`
  - Inverse: $f^{-1}: \mathbb{R} \ni y \mapsto e^y \in \mathbb{R}_{++}$

4. $f(x) = \sqrt{x-1}$
  - Domain: $\mathbb{R}_{+} = [1,\infty) = \{x \in \mathbb{R}: x \ge 1\}$
  - Range: $\mathbb{R}_{+}$
  - One-to-one? `Yes`
  - Onto? `Yes` for $f: \mathbb{R}_{+} \to \mathbb{R}_{+}$
  - Bijective? `Yes`
  - Inverse: $f^{-1}(y) = y^2+1$

5. $f(x) = x^2-1$
  - Domain: $\mathbb{R}$
  - Range: $[-1,\infty) = \{x \in \mathbb{R}: x \ge -1\}$
  - One-to-one? `No`
  - Onto? `Yes` for $f: \mathbb{R} \to [-1,\infty) \subset \mathbb{R}$, `No` for $f: \mathbb{R} \to \mathbb{R}$
  - Bijective? `No` because it is not injection (one-to-one)
  - Inverse: undefined because $f$ is not bijective

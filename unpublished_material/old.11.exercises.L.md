---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{admonition} EXTRA MATERIAL
:class: danger

Material in this section is optional and will not be part of the course assessment.

```

# ☕️ Cake eating problem

<<<<<<<< HEAD:12.dynamic_cake_eating.md
<small>⏱ <span class="eta"></span> | <span class="words"></span> words</small>

```{image} _static/img/cake.png
:width: 25%
:align: center
```
<div style="clear: both"></div>


## Question 1
========
## Question L.1
>>>>>>>> 118f83b2d83dbf867cab54275e5f4cf3e007c45b:unpublished_material/old.11.exercises.L.md

Consider the dynamic optimization problem of dividing a fixed amount of resource over time to maximize the discounted sum of utilities in each period, which can be represented by a simple process of eating a cake over time. (This type of problems is known as `cake eating`). 

Assume that:

- The initial size of the cake be $m_0$
- The cake has to be eaten within $T=3$ days
- The choice is how much cake to eat each day, denoted $0 \le c_t \le m_t$, where $m_t$ is the size of the cake in the morning of day $t$
- Naturally, what is not eaten in period $t$ is left for the future, so $m_{t+1}=m_t-c_t$
- Let the utility be additively separable, i.e. the total utility represented by a sum of per-day utilities denoted $u(c_t)$
- Assume that each day the cake becomes less tasty, so that from the point of view of day $t$ the utility of eating the cake the next day is discounted by (i.e. multiplied with) a coefficient $0 < \beta < 1$

Tasks:

1. Write down the dynamic optimization problem in the form of *Bellman equation*
2. Derive the value function and the policy function in each period starting from the last, i.e. performing by-hand backwards induction, when $u(c_t)=\log(c_t)$

````{admonition} Answer
:class: dropdown

Overall goal is to maximize the discounted expected utility
%
$$
\sum_{t=1}^T\beta^{t-1}u(c_{t}) 
\to \max_{\{c_{t}\}_{t=1}^T}
$$
%
The *Bellman equation* is given by
%
$$
V_t(m_t) = 
\begin{cases}
\max_{0 \le c_t \le m_t} \big( u(c_t) + \beta V(m_t-c_t) \big)
&,\text{ if } t<T=3\\
\max_{0 \le c_t \le m_t} u(c_t) 
&,\text{ if } t=T=3
\end{cases}
$$
%
- the state space is given by one variable $m_t$
- the choice space is given by one variable $c_t$
- the preferences are given by the utility function $u(c_t)=\log(c_t)$ and the discount factor $\beta$
- the beliefs are given by the transition rule $m_{t+1}=m_t-c_t$

---

Performing backwards induction by hand:

In the terminal period $t=T=3$ the problem is
%
$$
\max_{0 \le c_T \le m_T} \log(c_T),
$$
logarithm is continuous, feasible set is a closed interval (closed and bounded), so the solution exists by the Weierrstrass theorem. There are no stationary points (FOC $1/c_T = 0$ does not have solutions), so only have to look at the bondary points. Thus, the solution is given by 
%
$$
\begin{array}{l}
c_3^\star=m_3 \\
V_3(m_3) = \log(m_3)
\end{array}
$$
%
In the period $t=T-1=2$ the optimization problem takes the form
%
$$
\max_{0 \le c_2 \le m_2} \big( \log(c_2) + \beta \log(m_2 - c_2) \big)
$$
%
Solving FOC gives $c_2^\star = \frac{m_2}{1+\beta}$, which after noting that the objective function is strictly concave, is the global maximum. Thus, the solution is given by
%
$$
\begin{array}{l}
c_2^\star=\frac{m_2}{1+\beta} \\
V_2(m_2) = \log(c_2^\star) + \beta \log(m_2 - c_2^\star) = (1+\beta)\log(\frac{m_2}{1+\beta} ) + \beta \log(\beta)
\end{array}
$$
%
In the period $t=T-2=1$ the optimization problem takes the form
%
$$
\max_{0 \le c_1 \le m_1} \Big( \log(c_1) + \beta \Big[ (1+\beta)\log(\frac{m_1-c_1}{1+\beta} ) + \beta \log(\beta) \Big] \Big)
$$
%
FOC for this problems is similar to the case of $t=2$, and again it is not hard to show that the objective function is strictly concave, making the FOC a sufficient condition for maximum.  The solution is given by
%
$$
\begin{array}{l}
c_1^\star=\frac{m_1}{1+\beta(1+\beta)} \\
V_1(m_1) = \big(1+\beta(1+\beta)\big)\log(\frac{m_1}{1+\beta(1+\beta)} ) + \big(\beta(1+\beta)+\beta^2\big) \log(\beta)
\end{array}
$$

Obviously, this approach can be continued and is thus applicable for any $T$, although the algebra becomes more and more tedious. In practice, after a few steps one can guess the general form of a solution (involving $t$) and verify it by plugging it into the Bellman equation.

````


## Question 2

Now consider the infinite horizon version of the cake eating problem. The only difference from your formulation in the previous question is that $T=\infty$ and the termination condition in the *Bellman equation* disappears.

The *Bellman equation* is now a functional equation which solution is given by a fixed point of the contracting Bellman operator in the functional space.
The only by-hand solution in this case is to guess the solution and verify it.

Find the solution (value and policy functions) of the problem by guessing a functional form, and then verifying that it satisfies the *Bellman equation*.

```{hint}
By guessing a functional form we mean that you should guess the form of the value function as function of the state variables and some intermediate parameters, which can be determined during the verification step.
```

````{admonition} Answer
:class: dropdown

The main change for the infinite horizon is that the Bellman equation does not have a special termination condition for $t=T$, and that the time subscripts can be dropped. The later is due to the fact that the maximum attainable utility can be achieved in any period, so the optimal choice is the same in all periods, making the value function also time-invariant.

Let's find the solution by guessing a functional form for the value function: $V(m)=A+B\log(m)$ where $A$ and $B$ are some parameters to be determined. Then the Bellman equation becomes
%
$$
\begin{array}{rcl}
V(m) & = & \max_{c}\big\{u(c)+\beta V(m-c)\big\} \\
A+B\log(m) & = & \max_{c} \big\{\log(c)+\beta[A+B\log(()m-c)] \big\}
\end{array}
$$
%
Now we can determine $A$ and $B$ and find the optimal rule for cake consumption.

F.O.C. for $c$
%
$$
\frac{1}{c} - \frac{\beta B}{m - c} = 0 \implies c = \frac {m} {1 + \beta B}, \; m - c = \frac {\beta B m} {1 + \beta B}
$$
%
Then we have
%
$$
A + B\log(m) = \log(m) + \log\frac{1}{1+\beta B} + 
\beta A + \beta B \log(m) + \beta B \log\frac{\beta B}{1+\beta B}
$$
%
Making sure the coefficient with $\log(m)$ and the constants are the same on both RHS and LHS of the equality, we have
%
$$
\left\{
\begin{array}{rcl}
A &=& \beta A + \log\frac{1}{1+\beta B} + \beta B \log\frac{\beta B}{1+\beta B} \\
B &=& 1 + \beta B
\end{array}
\right.
$$
%
After some algebra
%
$$
c^{\star}(m) = \frac {m} {1 + \beta B} = \frac {m} {1 + \frac{\beta}{1-\beta}} = (1-\beta)m \\
V(m) = \frac{\log(m)}{1-\beta} + \frac{\log(1-\beta)}{1-\beta} + \frac{\beta \log(\beta)}{(1-\beta)^2}
$$

````

## Question 3

The first order condition for the cake eating problem is given by a so-called Euler equation which links the optimal consumption level in any period to the optimal consumption level in the next period, and is given by
%
$$
\frac{d u}{d c}\big(c^\star(m)\big) = \beta \frac{d u}{d c}\big(c^\star(m')\big)
$$
where $m' = m-c^\star(m)$ the size of the cake in the next time period under the optimal consumption.


1. Derive this equation
2. Verify that solving it for the infinite horizon case with $u(c)=\log(c)$ gives the same solution as in the previous question.

```{hint}
Euler equation is a combination of the first order conditions *and* the envelope theorem applied to the value function.
```

````{admonition} Answer
:class: dropdown

We start from the Bellman equation for the infinite horizon version of cake eating problem
%
$$
V(m)=\max_{0 \le c \le m}\big\{u(c)+\beta V(m-c)\big\}
$$
%
Assuming the interior solution, the optimal consumption $c^\star(m)$ satisfies for all $m$ the FOC condition
%
$$
\frac{d u}{d c}\big(c^\star(m)\big) - \beta \frac{d V}{d m}\big(m-c^\star(m)\big) = 0
$$
%
On the other hand, if we denote $G(m,c) = u(c)+\beta V(m-c)$ the maximand on the RHS, the envelope theorem states that
%
$$
\frac{d V}{d m}(m) = 
\frac{\partial G}{\partial m}(m,c) \Big|_{c=c^\star(m)}= 
\frac{d}{d m} \big(u(c)+\beta V(m-c)\big) \Big|_{c=c^\star(m)} =
\beta \frac{d V}{d m}(m-c^\star(m))
$$
%
Combining the two expressions we have $\frac{d u}{d c}\big(c^\star(m)\big) = \frac{d V}{d m}(m)$, and after plugging this expression back to the FOC, we derive the required expression
%
$$
\frac{d u}{d c}\big(c^\star(m)\big) = \beta \frac{d u}{d c}\Big(c^\star\big(m-c^\star(m)\big)\Big)
$$

---

Euler equation above is another functional equation, as the unknown is a function $c^\star(m)$. 
Solving it requires a guess-and-verify approach again.

Given the series of finite horizon solutions (which are constructive) we can guess that $c^\star(m)$ is a linear function of $m$, i.e. $c^\star(m) = \gamma m$. Then for $u(c)=\log(c)$ we have
%
$$
\frac{1}{\gamma m} = \beta \frac{1}{\gamma (m - \gamma m)} \implies
1 = \frac{\beta}{1-\gamma} \implies
\gamma = 1-\beta
$$
%
Thus, we have $c^\star(m) = (1-\beta) m$ which matches the solution we got above!


````

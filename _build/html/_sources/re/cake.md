

Cake eating problem
~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/img/cake.png
:width: 128px

- Cake of initial size $W_0$
- How much of the cake to eat each period $t$, $c_t$?
- Time is discrete, $t=1,2,\dots,\infty$ 
- What is not eaten in period $t$ is left for the future $W_{t+1}=W_t-c_t$

Model specification and parametrization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Choices of the decision maker**
- How much cake to eat

- **State space of the problem**
- A full list of variables that are relevant to the choices in question

- **Preferences of the decision maker**
- Utility flow from cake consumption
- Discount factor

- **Beliefs of the decision agents about how the state will evolve**
- Transition density/probabilities of the states
- May be conditional on the choices

Preferences in the cake eating
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let the flow utility be given by

.. math::

 u(c_{t})=\log(c_t)

Overall goal is to maximize the discounted expected utility

.. math::

 \max_{\{c_{t}\}_{0}^{\infty}}\sum_{t=0}^{\infty}\beta^{t}u(c_{t})
 \longrightarrow \max

Value function
~~~~~~~~~~~~~~

**Value function** $V(W_t)$ = the maximum attainable 
value given the size of cake $W_t$ (in period $t$)

- State space is given by single variable $W_t$
- Transition of the variable (**rather, beliefs**) depends on the choice

.. math::

W_{t+1}=W_t-c_t

Bellman equation (recursive problem)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

 \begin{eqnarray*}
  V(W_{0}) & = & \max_{\{c_{t}\}_{0}^{\infty}}\sum_{t=0}^{\infty}\beta^{t}u(c_{t}) \\
  & = & \max_{0 \le c_{0}\le W_0}\{u(c_{0})+\beta\max_{\{c_{t}\}_{1}^{\infty}}\sum_{t=1}^{\infty}\beta^{t-1}u(c_{t})\} \\
  & = & \max_{0 \le c_{0}\le W_0}\{u(c_{0})+\beta V(W_{1})\}
 \end{eqnarray*}

.. math::

 V(W_{t})=\max_{0 \le c_{t} \le W_t}\big\{u(c_{t})+\beta V(\underset{=W_{t}-c_{t}}{\underbrace{W_{t+1}}})\big\}

Recap: components of the dynamic model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **State variables** — vector of variables that describe all relevant
 information about the modeled decision process, $W_t$
- **Decision variables** — vector of variables describing the choices,
 $c_t$
- **Instantaneous payoff** — utility function, $u(c_t)$, with
 time separable discounted utility
- **Motion rules** — agent’s beliefs of how state variable evolve
 through time, conditional on choices, $W_{t+1}=W_t-c_t$
- **Value function** — maximum attainable utility, $V(W_t)$
- **Policy function** — mapping from state space to action space that
 returns the optimal choice, $c^{\star}(W_t)$

Maybe we can find analytic solution?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Start with a (good) guess of $V(W)=A+B\log W$

 .. math::
  \begin{eqnarray*}
  V(W) & = & \max_{c}\big\{u(c)+\beta V(W-c)\big\} \\
  A+B\log W & = & \max_{c} \big\{\log c+\beta(A+B\log (W-c)) \big\}
  \end{eqnarray*}

- Determine $A$ and $B$ and find the optimal rule for cake
 consumption.
- This is only possible in **few** models!

.. jupyter::
 :cell-break:

F.O.C. for $c$

.. math::
\frac{1}{c} - \frac{\beta B}{W - c} = 0, \quad c = \frac {W} {1 + \beta B}, W - c = \frac {\beta B W} {1 + \beta B}

Then we have

.. math::
A + B\log W = \log W + \log\frac{1}{1+\beta B} + 
\beta A + \beta B \log W + \beta B \log\frac{\beta B}{1+\beta B}

.. math::
\begin{eqnarray*}
A &=& \beta A + \log\frac{1}{1+\beta B} + \beta B \log\frac{\beta B}{1+\beta B} \\
B &=& 1 + \beta B
\end{eqnarray*}

.. jupyter::
 :cell-break:

After some algebra

.. math::
c^{\star}(W) = \frac {W} {1 + \beta B} = \frac {W} {1 + \frac{\beta}{1-\beta}} = (1-\beta)W

.. math::
V(W) = \frac{\log(W)}{1-\beta} + \frac{\log(1-\beta)}{1-\beta} + \frac{\beta \log(\beta)}{(1-\beta)^2}

Bellman operator
~~~~~~~~~~~~~~~~

The Bellman equation becomes operator in functional space

.. math::

T(V)(W) \equiv \max_{0 \le c \le W} \big[u(c)+\beta V(W-c)\big]

The Bellman equations is then $V(W) = T({V})(W)$, with the
solution given by the fixed point (solution to $T({V}) = V$)

Value function iterations (VFI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Start with an arbitrary guess $V_0(W)$ 
(will see next time that the initial guess is not important)
- At each iteration $i$ compute

.. math::

 \begin{eqnarray*}
 V_i(W) = T(V_{i-1})(W) &=& 
 \max_{0 \le c \le W} \big\{u(c)+\beta V_{i-1}(W-c) \big \} \\
 c_{i-1}(W) &=& 
 \underset{0 \le c \le W}{\arg\max} \big\{u(c)+\beta V_{i-1}(W-c) \big \} 
 \end{eqnarray*}

- Repeat until convergence

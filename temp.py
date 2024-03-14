import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

def fx(n):
    return 1 + 1/(n**(0.7))
def subplots(fs):
    "Custom subplots with axes throught the origin"
    fig, ax = plt.subplots(figsize=fs)
    # Set the axes through the origin
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none')
    return fig, ax
def plot_seq(N,epsilon,a,fn):
    fig, ax = subplots((9, 5))  
    xmin, xmax = 0.5, N+1
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(0, 2.1)
    n = np.arange(1, N+1)
    ax.set_xticks([])
    ax.plot(n, fn(n), 'ko', label=r'$x_n$', alpha=0.8)
    ax.hlines(a, xmin, xmax, color='k', lw=0.5, label='$a$')
    ax.hlines([a - epsilon, a + epsilon], xmin, xmax, color='k', lw=0.5, linestyles='dashed')
    ax.fill_between((xmin, xmax), a - epsilon, a + epsilon, facecolor='blue', alpha=0.1)
    ax.set_yticks((a - epsilon, a, a + epsilon))
    ax.set_yticklabels((r'$a - \epsilon$', r'$a$', r'$a + \epsilon$'))
    ax.legend(loc='upper right', frameon=False, fontsize=14)
    plt.show()

N = 50
a = 1

plot_seq(N,0.30,a,fx)
plot_seq(N,0.15,a,fx)
plot_seq(N,0.08,a,fx)


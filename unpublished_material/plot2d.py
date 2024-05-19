# this module is drawing a simple 2d matplot figure 

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

if __name__ == '__main__':
    
    alpha = 1
    beta = 3
    m = 10
    # f = lambda x: alpha * np.log( alpha * m / ( (alpha+beta)*x[0] )) + beta * np.log( beta * m / ( (alpha+beta)*x[1] ))
    cond = lambda p1: p1/m <= alpha/beta
    f1 = lambda x: cond(x)*(m/x - beta/alpha) + (1-cond(x))*0
    # f2 = lambda x: cond(x)*(beta*/alpha) + (1-cond(x))*0

    lb,ub = .5,10
    x = np.linspace(lb,ub, 100)

    fig = plt.figure(dpi=160)
    ax = fig.add_subplot(111)
    # ax.set_aspect('equal', 'box')
    ax.plot(x,f1(x),label=r"$x_1^\star(p_1)$")
    # ax.plot(x,f2(x),label=r"$x_2^\star(p_2)$")
    # plt.setp(ax, xticks=[],yticks=[])
    # plt.xlabel(r'p_i')
    plt.legend(loc='upper right', frameon=False)
    plt.show()



# this module is drawing a simple 3d matplot figure 
# to illustrate a quadratic form

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def f(x,y):
    return -x**2 - 2* y**2 

if __name__ == '__main__':
    A = np.array([[1,.5],[.5,1.5]])
    # A = np.array([[2,0],[0,1]])
    f = lambda x: -(x@A@x)
    x = y = np.linspace(-5.0, 5.0, 100)
    X, Y = np.meshgrid(x, y)
    zs = np.array([f((x,y)) for x,y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    fig = plt.figure(dpi=160)
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.plot_surface(X, Y, Z, 
                rstride=2, 
                cstride=2,
                cmap=cm.jet,
                alpha=0.7,
                linewidth=0.25)
    plt.setp(ax1,xticks=[],yticks=[],zticks=[])

    fig = plt.figure(dpi=160)
    ax2 = fig.add_subplot(111)
    ax2.set_aspect('equal', 'box')
    ax2.contour(X, Y, Z, 50,
                cmap=cm.jet)
    plt.setp(ax2, xticks=[],yticks=[])

    fig = plt.figure(dpi=160)
    ax3 = fig.add_subplot(111, projection='3d')
    ax3.plot_wireframe(X, Y, Z, 
                rstride=2, 
                cstride=2,
                alpha=0.7,
                linewidth=0.25)
    f0 = f(np.zeros((2)))+0.1
    ax3.scatter(0, 0, f0, c='black', marker='o', s=10)
    ax3.plot([-3,3],[0,0],[f0,f0],color='black')
    ax3.plot([0,0],[-3,3],[f0,f0],color='black')
    plt.setp(ax3,xticks=[],yticks=[],zticks=[])

    plt.show()



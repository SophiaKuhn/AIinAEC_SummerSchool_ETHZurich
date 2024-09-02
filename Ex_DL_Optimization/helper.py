from typing import Union

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# Rosenbrock Funktion
def f(x0, x1):
    return 100 * (x0**2 - x1)**2 + (x0 - 1)**2

def f_prime_x0(x0, x1):
    return 2 * (200 * x0 * (x0**2 - x1) + x0 - 1)

def f_prime_x1(x0, x1):
    return -200 * (x0**2 - x1)

def plot_rosenbrock(downhill=False, x0=-1, x1=-1):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(projection='3d')
    # ax = fig.gca(projection='3d')

    s = 0.3
    X = np.arange(-2, 2.+s, s)
    Y = np.arange(-2, 3.+s, s)
        
    #Create the mesh grid(s) for all X/Y combos.
    X, Y = np.meshgrid(X, Y)
    #Rosenbrock function w/ two parameters using numpy Arrays
    Z = f(X, Y)

    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, alpha=0.5)
    # Global minimum
    ax.scatter(1, 1, f(1, 1), color="red", marker="*", s=200)
    # Starting point
    ax.scatter(x0, x1, f(x0, x1), color="green", marker="o", s=200)

    if downhill:
        eps = 50
        # Plot Updated Points
        for (x0, x1) in downhill:
            ax.scatter(x0, x1, f(x0, x1)+eps, color="green", marker="o", s=50)
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()
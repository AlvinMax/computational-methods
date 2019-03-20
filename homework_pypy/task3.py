import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.utils import shuffle

def phi(z):
    return z - (z ** 3 - 1) / (3 * (z ** 2))

def drawCircle():
    X = []
    Y = []
    for i in range(0, 361):
        X.append(math.cos(math.radians(i)))
        Y.append(math.sin(math.radians(i)))
    plt.plot(X, Y, linewidth=0.5)


def findNearestId(array, value):
    idx = (np.abs(array-value)).argmin()
    return idx


r = np.array([-0.5 + 0.8660j,
              -0.5 - 0.8660j,
              1 + 0j])
colors = ["red", "blue", "green"]

def plotLines(fragments=50, eps = 0.1):
    x = np.linspace(-1, 1, fragments)
    y = np.linspace(-1, 1, fragments)
    x, y = np.meshgrid(x, y)
    x, y = shuffle(x, y)
    for i in range(fragments):
        for j in range(fragments):
            z = x[i][j] + y[i][j] * 1j
            Z = []
            while abs(z ** 3 - 1) > eps:
                Z.append(z)
                z = phi(z)
            id = findNearestId(r, z)
            Z = np.array(Z)
            plt.plot(Z.real, Z.imag, c=colors[id], alpha=0.1)

def plotPoints(fragments=400, eps = 0.01):
    x = np.linspace(-2, 2, fragments)
    y = np.linspace(-2, 2, fragments)
    x, y = np.meshgrid(x, y)
    X, Y, C = [], [] ,[]
    for i in range(fragments):
        for j in range(fragments):
            z = x[i][j] + y[i][j] * 1j
            while abs(z**3 - 1) > eps:
                z = phi(z)
            id = findNearestId(r, z)
            X.append(x[i][j])
            Y.append(y[i][j])
            C.append(colors[id])
    plt.scatter(X, Y, c=C, s=2)

print("running")
plotPoints()
# plotLines()
drawCircle()

plt.axis('equal')
plt.axis([-2, 2, -2, 2])
plt.grid()
plt.show()

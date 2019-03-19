import matplotlib.pyplot as plt
import numpy as np

def phi(x, r):
    return r * x * (1 - x)

def derivPhi(x, r):
    return r - 2 * r * x


def plotApprox(x0, r, q, eps=0.000001, c="red", a=0.1, stepHeight=1):
    X = []
    x = x0
    eps *= (1 - q) / q
    finished = False
    while not finished:
        X.append(x)
        x = phi(x, r)
        finished = abs(x - X[-1]) < eps

    if len(X) > 1:
        plt.plot(X, range((len(X) - 1) * stepHeight, -stepHeight, -stepHeight), c=c, alpha=a)
    else:
        print(x0, r, q, eps, X)
        plt.scatter(x0, 0, c="red", alpha=a, s=1)

def plotFirstRange():
    for i in range(1, 20):
        x = 0.1
        r = i * 0.05
        q = max(abs(derivPhi(x, r)), abs(derivPhi(0, r)))
        plotApprox(x, r, q, eps=1e-10,c="green", a=0.4)

def plotSecondRange():
    for i in range(101, 200):
        r = i * 0.01
        x = (3 * r - 3) / (4 * r)
        q = abs(derivPhi(x, r))
        plotApprox(x, r, q, c="cyan", a=0.9)

def plotThirdRange():
    for i in range(21, 30):
        r = i * 0.1
        x = (3 * r - 1) / (4 * r)
        q = abs(derivPhi(x, r))
        plotApprox(x, r, q, c="blue", stepHeight = 10, a=0.9)

def plotInf():
    for i in range(301, 303):
        r = i * 0.1
        x = 1 - 1 / r + 0.1
        q = 0.9
        plotApprox(x, r, q, c="blue", stepHeight=10, a=0.9)


def plotRoot(x0, r, eps=0.0001, c="red", a=1):
    X = []
    x = x0
    finished = False
    while not finished:
        X.append(x)
        x = phi(x, r)
        xPrev = X[len(X) // 2]
        finished = abs(x - xPrev) < eps and len(X) > 2
        if (finished):
            X = X[len(X) // 2:]

    plt.scatter([r]*len(X), X, c=c, alpha=a, s=1)

def plotBifurcation():
    for i in range(1, 800):
        r = i * 0.005
        x = 1 - 1 / r + 0.1
        plotRoot(x, r, c="blue")

# plotFirstRange()
# plotSecondRange()
plotThirdRange()

# plotBifurcation()

plt.show()

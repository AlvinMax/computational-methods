from utils import minus, plus, subst, split_at
from copy import deepcopy

def jacobi (m, eps):
    (A, f) = split_at(m)
    (B, c) = to_iter(A, f)
    prev = c
    x = plus(subst(B, prev), c)
    cnt = 1
    n = norma(B)
    if (n >= 1):
        print("norma > 1, Jacobi error")
        return ([[]], 0)
    e1 = (1 - n) / n * eps
    while (myNorm(minus(x, prev)) > e1):
        cnt += 1
        prev = x
        x = plus(subst(B, prev), c)
    return (x, cnt)

def myNorm(x):
    max1 = 0
    for i in range (0, len(x)):
        if (max1) < abs(x[i]):
            max1 = abs(x[i])
    return max1

def norma (m):
    max1 = 0
    for i in range (0, len(m)):
        for j in range (0, len(m)):
            if max1 < abs(m[i][j]):
                max1 = abs(m[i][j])
    return max1


def to_iter (A, F):
    B = deepcopy(A)
    C = [0] * len(F)
    for i in range (0, len(B)):
        for j in range (0, len(B)):
            if (i == j):
                B[i][j] = 0
            else:
                B[i][j] = - A[i][j] / A[i][i]
                C[i] = F[i] / A[i][i]
    return (B, C)

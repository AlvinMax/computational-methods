from utils import minus, plus, subst

def jacobi (m, eps):
    (A, f) = split_at(m)
    (B, c) = to_iter(A, f)
    prev = c
    x = plus(subst(B, prev), c)
    cnt = 1
    n = norma(B)
    if (n >= 1):
        print("Норма матрицы > 1, метод не сойдется")
    e1 = (1 - n) / n * eps
    while (minus(x, prev) > e1):
        cnt++
        prev = x
        x = plus(subst(B, prev), c)
    print("Количество шагов Якоби: ")
    print(cnt)
    return x

def norma (m):
    max = 0
    for i in range (0, len(m)):
        for j in range (0, len(m)):
            if max < abs(m[i][j])
            max = abs(m[i][j])
    return max


def to_iter (A, F):
    B = A
    C = [0] * len(F)
    for i in range (0, len(B)):
        for j in range (0, len(B)):
            if (i == j):
                B[i][j] = 0
            else:
                B[i][j] = - A[i][j] / A[i][i]
                C[i] = F[i] / A[i][i]
    return (B, C)

import numpy as np


def inverse_matrix(m):
    return np.linalg.inv(m)


def matrix_rate(m):
    return np.linalg.norm(m)


def conv(m):
    return matrix_rate(m) * matrix_rate(inverse_matrix(m))
import numpy as np
from utils import inverse_matrix


def matrix_rate(m):
    return np.linalg.norm(np.array(m))


def condition_number(m):
    return matrix_rate(m) * matrix_rate(inverse_matrix(m))

import numpy as np


def inverse_matrix(m):
    return np.linalg.inv(np.array(m)).tolist()


def transpose_matrix(m):
	return np.array(m).T.tolist()


def matrix_rate(m):
    return np.linalg.norm(np.array(m))


def condition_number(m):
    return matrix_rate(m) * matrix_rate(inverse_matrix(m))
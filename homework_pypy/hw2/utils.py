from math import sqrt
import numpy as np


def inverse_matrix(m):
    return np.linalg.inv(np.array(m)).tolist()


def transpose_matrix(m):
	return np.array(m).T.tolist()


def split_at(m):
	r = []
	for l in m:
		r.append(l.pop())
	return (m, r)

def subst(A, x):
	return [sum(e_x * e_r for e_x, e_r in zip(row_A, x)) for row_A in A]

def minus(b, r):
	return [e_b - e_r for e_b, e_r in zip (b, r)]

def plus(b, r):
	return [e_b + e_r for e_b, e_r in zip (b, r)]

def mul(k, l):
	return [e_l * k for e_l in l]

def scalar_product(a, b):
	return sum(e_a * e_b for e_a, e_b in zip(a, b))

def norm(l):
	return sqrt(sum(e_l * e_l for e_l in l))

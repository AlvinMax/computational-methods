import numpy as np

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

def gradient_it(m, eps):
	cnt = 0

	(A, b) = split_at(m)
	x0 = [0] * len(b)
	r0 = minus(b, subst(A, x0))
	p0 = r0
	z0 = r0
	s0 = r0

	for i in range(0, len(b)):
		sub = subst(A, z0)
		prev_p = p0
		prev_r = r0

		a  = scalar_product(p0, r0) / scalar_product(s0, sub)
		x0 = plus(x0, mul(a, z0))
		r0 = minus(r0, mul(a, sub))
		p0 = minus(p0, mul(a, sub(A.transpose(), s0)))
		b  = scalar_product(p0, r0) / scalar_product(prev_p, prev_r)
		z0 = plus(r0, mul(b, z0))
		s0 = plus(p0, mul(b, s0))

		cnt += 1

	return (r0, cnt)
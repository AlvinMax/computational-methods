from math import sqrt
import utils

def gradient_it(m, eps):
	cnt = 0

	(A, B) = split_at(m)
	x0 = [0] * len(B)
	r0 = minus(B, subst(A, x0))
	p0 = r0
	z0 = r0
	s0 = r0

	for i in range(0, len(B)):
		sub = subst(A, z0)
		prev_p = p0
		prev_r = r0
		At = transpose_matrix(A)
		# print(At)

		a  = scalar_product(p0, r0) / scalar_product(s0, sub)
		x0 = plus(x0, mul(a, z0))
		r0 = minus(r0, mul(a, sub))
		p0 = minus(p0, mul(a, subst(At, s0)))
		b  = scalar_product(p0, r0) / scalar_product(prev_p, prev_r)
		z0 = plus(r0, mul(b, z0))
		s0 = plus(p0, mul(b, s0))

		if abs(norm(r0) / norm(B)) < eps:
			break
		cnt += 1

	return (x0, cnt)

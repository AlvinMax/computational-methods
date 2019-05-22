import utils as ut

def gradient_it(m, eps):
	cnt = 0

	(A, B) = ut.split_at(m)
	x0 = [0] * len(B)
	r0 = ut.minus(B, ut.subst(A, x0))
	p0 = r0
	z0 = r0
	s0 = r0

	for i in range(0, 2 * len(B)):
		sub = ut.subst(A, z0)
		prev_p = p0
		prev_r = r0
		At = ut.transpose_matrix(A)
		# print(At)

		a  = ut.scalar_product(p0, r0) / ut.scalar_product(s0, sub)
		x0 = ut.plus(x0, ut.mul(a, z0))
		r0 = ut.minus(r0, ut.mul(a, sub))
		p0 = ut.minus(p0, ut.mul(a, ut.subst(At, s0)))
		b  = ut.scalar_product(p0, r0) / ut.scalar_product(prev_p, prev_r)
		z0 = ut.plus(r0, ut.mul(b, z0))
		s0 = ut.plus(p0, ut.mul(b, s0))

		if abs(ut.norm(r0) / ut.norm(B)) < eps:
			break
		cnt += 1

	return (x0, cnt)
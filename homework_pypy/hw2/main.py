import copy
import task5
import task1
import utils

def read_matrix(path):
	f = open(path, 'r')
	m = []
	for line in f:
		m.append([float(x) for x in line.split()])
	return m

eps = 0.00001
m = read_matrix("./tests/test3.in")
m_g = copy.copy(m)

gauss_res = task1.gauss(m_g)
print("".join(["Gauss Result==", str(gauss_res)]))

(gr_res, gr_it) = task5.gradient_it(m, eps)
print("".join(["Gradient Result==", str(gr_res), " with eps==", str(eps), " count of iteration==", str(gr_it)]))
# print("Result== ", gr_res, " with eps==", eps, " count of iteration==", gr_it)
# print(utils.subst(m, gr_res))
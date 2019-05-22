import copy
import task5
import task1
import task2
import utils

def read_matrix(path):
	f = open(path, 'r')
	m = []
	for line in f:
		m.append([float(x) for x in line.split()])
	return m

eps = 0.00001
m = read_matrix("./tests/test2.in")
# m = utils.gilbert_matrix(5)
m_g = copy.copy(m)
m_test = copy.copy(m)
m_j = copy.copy(m)

gauss_res = task1.gauss(m_g)
print("".join(["Gauss Result==", str(gauss_res)]))

(jacob_res, j_it) = task2.jacobi(m_j, eps)
print("".join(["Jacobi Result==", str(jacob_res), " with eps==", str(eps), " count of iteration==", str(j_it)]))


(gr_res, gr_it) = task5.gradient_it(m, eps)
print("".join(["Gradient Result==", str(gr_res), " with eps==", str(eps), " count of iteration==", str(gr_it)]))
# print("Result== ", gr_res, " with eps==", eps, " count of iteration==", gr_it)
print(utils.subst(m_test, gr_res))
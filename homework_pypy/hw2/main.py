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
m = read_matrix("./tests/test5.in")
# m = utils.gilbert_test(5)
m_g = copy.deepcopy(m)
m_test = copy.deepcopy(m)
m_j = copy.deepcopy(m)
m_gr = copy.deepcopy(m)

gauss_res = task1.gauss(m_g)
print("".join(["Gauss Result==", str(gauss_res)]))


# print(m_g)
# print(m_j)
(jacob_res, j_it) = task2.jacobi(m_j, eps)
print("".join(["Jacobi Result==", str(jacob_res), " with eps==", str(eps), " count of iteration==", str(j_it)]))


(gr_res, gr_it) = task5.gradient_it(m_gr, eps)
print("".join(["Gradient Result==", str(gr_res), " with eps==", str(eps), " count of iteration==", str(gr_it)]))
# print(utils.subst(m_test, gr_res))
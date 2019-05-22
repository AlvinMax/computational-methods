import copy
import task5
import task1
import task6
import task2
import utils

def read_matrix(path):
	f = open(path, 'r')
	m = []
	for line in f:
		m.append([float(x) for x in line.split()])
	return m

eps = 0.00001
# m = read_matrix("./tests/test4.in")
m = utils.gilbert_test(10)
m_g = copy.deepcopy(m)
m_j = copy.deepcopy(m)
m_gr = copy.deepcopy(m)
m_test = copy.deepcopy(m)

(clean_m, ldsfj) = utils.split_at(m)
print("".join(["Rank matrix ", str(task6.matrix_rate(clean_m)), ", condition_number ", str(task6.condition_number(clean_m))]))

gauss_res = task1.gauss(m_g)
print("".join(["Gauss Result==", str(gauss_res)]))


# print(m_g)
# print(m_j)split_at
(jacob_res, j_it) = task2.jacobi(m_j, eps)
print("".join(["Jacobi Result==", str(jacob_res), " with eps==", str(eps), " count of iteration==", str(j_it)]))


(gr_res, gr_it) = task5.gradient_it(m_gr, eps)
print("".join(["Gradient Result==", str(gr_res), " with eps==", str(eps), " count of iteration==", str(gr_it)]))
# print(utils.subst(m_test, gauss_res))
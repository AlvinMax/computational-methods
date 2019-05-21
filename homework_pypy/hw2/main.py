import task5

def read_matrix(path):
	f = open(path, 'r')
	m = []
	for line in f:
		m.append([float(x) for x in line.split()])
	return m

eps = 0.00001
m = read_matrix("./tests/test3.in")

(gr_res, gr_it) = task5.gradient_it(m, eps)
print("".join(["Result==", str(gr_res), " with eps==", str(eps), " count of iteration==", str(gr_it)]))
# print("Result== ", gr_res, " with eps==", eps, " count of iteration==", gr_it)
print(task5.subst(m, gr_res))
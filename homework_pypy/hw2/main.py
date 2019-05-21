import task5

def read_matrix(path):
	f = open(path, 'r')
	m = []
	for line in f:
		m.append([float(x) for x in line.split()])
	return m

m = read_matrix("./tests/test1.in")

(gr_res, gr_it) = task5.gradient_it(m, 0.00001)
print("Результат вычислений:: ", gr_res, " при eps=", eps, " и количестве итераций::", gr_it)
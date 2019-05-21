import task5

def read_matrix(path):
	f = open(path, 'r')
	m = []
	for line in f:
		m.append([float(x) for x in line.split()])
	return m

m = read_matrix("/home/artem/Projects/CM/computational-methods/homework_pypy/hw2/tests/test1.in")
print(task5.gradient_it(m, 0.00001))
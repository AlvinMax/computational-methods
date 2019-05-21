
def read_matrix(path):
	f = open('text.txt', 'r')
	m = []
	for line in f:
		m.append([float(x) for x in line.split()])
	return m
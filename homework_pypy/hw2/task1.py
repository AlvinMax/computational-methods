from utils import mul, minus 

def swap_str(m, i, j):
    tmp = m[i]
    m[i] = m[j]
    m[j] = tmp
    return m


def gauss(m):
    for i in range(len(m) - 1):
        max_el = 0
        ind = i

        for j in range(i, len(m[0]) - 1):
            if m[j][i] > max_el:
                max_el = m[j][i]
                ind = j

        swap_str(m, ind, i)
        for j in range(i + 1, len(m)):
            if m[i][i] == 0:
                return []

            mul_str = mul(m[j][i] / m[i][i], m[i])
            m[j] = minus(m[j], mul_str)
            for k in range(len(m[j]) - 1):
                if m[j][k] < 0.0001:
                    m[j][k] = 0

    # print(m)
    x = [0] * len(m)
    for i in range(len(m) - 1, -1, -1):
        a = 0

        for j in range(i + 1, (len(m))):
            a = a + m[i][j] * x[j]

        if m[i][i] != 0:
            x[i] = (m[i][len(m[0]) - 1] - a) / m[i][i]
        else:
            x[i] = 100000000

    return x


print(gauss([[2, 5, 1, 4], [3, 1, -2, -5], [1, 1, 1, 6]]))
print(gauss([[-1, -1, 3], [-0.3333, -1, 2.3333]]))
print(gauss([[-1, 0.5, -1.5, -1, -0.5], [-3, -1, -2, -3, -1], [-0.25, -0.75, -1, -0.25, -0.25], [-0.25, -0.5, -0.25, -1, -0.25]]))

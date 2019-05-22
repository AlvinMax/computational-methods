from utils import minus, mul

def swap_str(m, i, j):
    tmp = m[i]
    m[i] = m[j]
    m[j] = tmp
    return m


def gauss(m):
    for i in range(len(m) - 1):
        # print(m)
        max_el = 0
        ind = i

        for j in range(i, len(m[0]) - 1):
            # print(abs(m[j][i]))
            if abs(m[j][i]) > max_el:
                max_el = abs(m[j][i])
                ind = j

        # print(max_el)
        swap_str(m, ind, i)
        for j in range(i + 1, len(m)):
            # c = m[j][i] / m[i][i]

            if m[i][i] == 0:
                continue

            # print(m[j][i])
            # print(m[i][i])
            # print(m[j][i] / m[i][i])
            mul_str = mul(m[j][i] / m[i][i], m[i])
            m[j] = minus(m[j], mul_str)
            for k in range(len(m[j]) - 1):
                if m[j][k] < 0.000001:
                    m[j][k] = 0

    # print(m)
    x = [0] * len(m)
    for i in range(len(m) - 1, -1, -1):
        a = 0

        for j in range(i + 1, (len(m))):
            a = a + m[i][j] * x[j]

        b = m[i][len(m[0]) - 1] - a

        if m[i][i] != 0:
            x[i] = b / m[i][i]
        else:
            x[i] = 0
            # if b == 0:
            #     x[i] = 0
            # else:
            #     return []

    return x


# print(gauss([[2, 5, 1, 4], [3, 1, -2, -5], [1, 1, 1, 6]]))
# print(gauss([[-1, -1, 3], [-0.3333, -1, 2.3333]]))
# print(gauss([[-1, 0.5, -1.5, -1, -0.5], [-3, -1, -2, -3, -1], [-0.25, -0.75, -1, -0.25, -0.25], [-0.25, -0.5, -0.25, -1, -0.25]]))
# print(gauss([[-1, -0.666666, -0.5, -0.4, -0.333334, -6], [-1.33333, -1, -0.8, -0.666668, -0.571428, -16], [-1.5, -1.2, -1, -0.85714, -0.749999, -59.9999], [-1.6, -1.33334, -1.14286, -1, -0.888888, -24], [-1.66667, -1.42857, -1.25, -1.11111, -1, -550]]))
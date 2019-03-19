from math import sqrt


def count_function(x, a, b, c, d):
    a = a * x * x * x
    b = b * x * x
    c = c * x
    return a + b + c + d


def count_extremum(a, b, c):
    a = 3 * a
    b = 2 * b
    D = b * b - 4 * a * c

    if D < 0:
        return 10000, 10000

    if D == 0:
        ans = (- b) / (2 * a)
        return ans, ans

    D = sqrt(D)

    return (-b - D) / (2 * a), (-b + D) / (2 * a)


def non_recursion_localize(l_x, r_x, a, b, c, d):
    l_y = count_function(l_x, a, b, c, d)
    r_y = count_function(r_x, a, b, c, d)

    while l_y * r_y >= 0:
        if l_y >= 0:
            r_x = l_x
            r_y = l_y
            l_x = l_x - 1
            l_y = count_function(l_x, a, b, c, d)
        if r_y <= 0:
            l_x = r_x
            l_y = r_y
            r_x = r_x + 1
            r_y = count_function(r_x, a, b, c, d)

    return l_x, r_x


def localize(a, b, c, d):
    x1, x2 = count_extremum(a, b, c)
    if x1 == 1000:
        l, r = non_recursion_localize(-10, 10, a, b, c, d)
        return (l, r), (0, 0), (0, 0)
    else:
        if x1 == x2:
            l1, r1 = non_recursion_localize(x1 - 10, x1, a, b, c, d)
            l2, r2 = non_recursion_localize(x1, x1 + 10, a, b, c, d)

            if l2 < r1:
                return (l2, r2), (0, 0)

            return (l1, r1), (l2, r2), (0, 0)
        else:
            l1, r1 = non_recursion_localize(x1 - 10, x1, a, b, c, d)
            l2, r2 = x1, x2
            l3, r3 = non_recursion_localize(x2, x2 + 10, a, b, c, d)

            if l2 < r1:
                if l3 < r2:
                    return (l2, r2), (0, 0), (0, 0)
                else:
                    return (l2, r2), (l3, r3), (0, 0)

            return (l1, r1), (l2, r2), (l3, r3)


def half_division(eps, l, r, a, b, c, d):
    while abs(r - l) > eps:
        fl = count_function(l, a, b, c, d)
        m = (r + l) / 2
        fm = count_function(m, a, b, c, d)
        if fl < 0:
            if fm < 0:
                l = m
            else:
                r = m
        else:
            if fm < 0:
                r = m
            else:
                l = m

    return l, r


#(l1, r1), (l2, r2), (l3, r3) = localize(1, 2, -13, 10)
#print(l2, r2)
#print(half_division(0.1, l2, r2, 1, 2, -13, 10))

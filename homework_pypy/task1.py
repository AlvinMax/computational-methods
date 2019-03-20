from math import sqrt


def count_function(x, a, b, c, d):
    a = a * (x ** 3)
    b = b * (x ** 2)
    c = c * x
    return a + b + c + d + .0

def diff(x, a, b, c, d):
    a = 3 * a * (x ** 2)
    b = 2 * b * x
    return a + b + c + .0

def count_extremum(a, b, c):
    a = 3 * a
    b = 2 * b
    D = b * b - 4 * a * c

    if D < 0.0:
        return 10000.0, 10000.0

    if D == 0.0:
        ans = (- b + .0) / (2 * a)
        return ans, ans

    D = sqrt(D)

    return (-b - D) / (2 * a), (-b + D) / (2 * a)


def non_recursion_localize(l_x, r_x, a, b, c, d):
    l_y = count_function(l_x, a, b, c, d)
    r_y = count_function(r_x, a, b, c, d)

    while l_y * r_y >= 0:
        if l_y >= 0:
            if l_y == 0:
                l_x = l_x - 1
                l_y = count_function(l_x, a, b, c, d)
            else:
                r_x = l_x
                r_y = l_y
                l_x = l_x - 1
                l_y = count_function(l_x, a, b, c, d)
        if r_y <= 0:
            if r_y == 0:
                r_x = r_x + 1
                r_y = count_function(r_x, a, b, c, d)
            else:
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
                return (l2, r2), (0, 0), (0, 0)

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
    cnt = 0
    while abs(r - l) > eps:
        fl = count_function(l, a, b, c, d)
        m = (r + l) / 2.0
        fm = count_function(m, a, b, c, d)
        if (fl * fm < 0):
            r = m
        else:
            l = m  

    return l, r


def newton(eps, x, a, b, c, d):
    f = count_function(x, a, b, c, d)

    while abs(f) > eps:
        x = x - (f + .0)/diff(x, a, b, c, d)
        f = count_function(x, a, b, c, d)
    return x

def simple_iterations(eps, x, a, b, c, d):
    f = count_function(x, a, b, c, d)
    l0 = diff(x, a, b, c, d)
    l0 = l0 * 2.0
    while abs(f) > eps:
        x = x - (f + .0)/l0
        f = count_function(x, a, b, c, d)
    return x

print("a * x^3 + b * x^2 + c * x + d = 0")
print("a = 1, b = 2, c = -13, d = 10")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
d = int(input("d:"))
eps = 0.00001

(l1, r1), (l2, r2), (l3, r3) = localize(a, b, c, d)

print("")
print("localize 1")
print(l1, r1)
print("half_division 1")
print(half_division(eps, l1, r1, a, b, c, d))
print("simple_iterations 1")
print(simple_iterations(eps, (r1 + l1)/2, a, b, c, d))
print("newton 1")
print(newton(eps, (r1 + l1)/2, a, b, c, d))

# print("")
# print("localize 2")
# print(l2, r2)
# print("half_division 2")
# print(half_division(eps, l2, r2, a, b, c, d))
# print("simple_iterations 2")
# print(simple_iterations(eps, (r2 + l2)/2, a, b, c, d))
# print("newton 2")
# print(newton(eps, (r2 + l2)/2 , a, b, c, d))

# print("")
# print("localize 3")
# print(l3, r3)
# print("half_division 3")
# print(half_division(eps, l3, r3, a, b, c, d))
# print("simple_iterations 3")
# print(simple_iterations(eps, (r3 + l3)/2, a, b, c, d))
# print("newton 3")
# print(newton(eps, (r3 + l3)/2, a, b, c, d))

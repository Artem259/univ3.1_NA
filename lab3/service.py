import numpy as np
from matplotlib import pyplot as plt
from numpy.polynomial import Polynomial


def divided_differences(x_vector, f_vector):
    dd = [f_vector.copy()]
    size = len(x_vector)
    for i in range(size-1):
        d = []
        for j in range(size-i-1):
            a = dd[-1][j+1] - dd[-1][j]
            b = x_vector[j+i+1] - x_vector[j]
            d.append(a/b)
        dd.append(d)
    return dd


def build_polynomial(x_vector, f):
    size = len(x_vector)
    f_vector = []
    for i in range(size):
        f_vector.append(f(x_vector[i]))
    dd = divided_differences(x_vector, f_vector)

    polynomial = Polynomial([dd[0][0]])
    current = Polynomial([1])
    for i in range(1, size):
        current *= Polynomial([-x_vector[i-1], 1])
        polynomial += dd[i][0] * current
    return polynomial


def solve_polynomial(polynomial, a, b):
    roots = polynomial.roots()
    root = None
    for e in roots:
        if a < e < b and ((not isinstance(e, complex)) or e.imag == 0.0):
            root = e.real
            break
    if root is None:
        raise Exception("Root is None")
    return root


def show_plot(f, polynomial, a, b, title):
    copy = polynomial.convert(domain=[a, b])
    x = copy.linspace()[0]
    fv = np.vectorize(f)

    plt.plot(x, fv(np.linspace(a, b, len(x))), label="f", color="orange")
    plt.plot(*copy.linspace(), label="f*", color="blue", linestyle="--")

    plt.legend()
    plt.title(title)
    plt.autoscale()
    plt.grid(True)
    plt.show()

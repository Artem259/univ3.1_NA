from math import cos, pi

import input
from service import *


def chebyshev_nodes_vector(a, b, nodes):
    x_vector = []
    for i in range(nodes):
        x = (a+b)/2 + ((b-a)/2) * cos((2*i+1)*pi / (2*nodes))
        x_vector.append(x)
    return x_vector


def task_1(f, a, b, nodes):
    if f(a) * f(b) >= 0:
        raise Exception("Invalid interval")
    x_vector = chebyshev_nodes_vector(a, b, nodes)
    print("Nodes = \n", x_vector, "\n")
    polynomial = build_polynomial(x_vector, f)
    print("Polynomial = \n", polynomial, "\n")
    root = solve_polynomial(polynomial, a, b)
    print("x = \n", root)
    show_plot(f, polynomial, a, b, "Task 2")


if __name__ == '__main__':
    print("\n--- Task 2 ---\n")
    task_1(input.f, input.interval[0], input.interval[1], input.nodes)

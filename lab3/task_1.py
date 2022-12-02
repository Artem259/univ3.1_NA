import input
from service import *


def equidistant_nodes_vector(a, b, nodes):
    x_vector = []
    step = (b-a) / (nodes-1)
    for i in range(nodes):
        x_vector.append(a + i*step)
    return x_vector


def task_1(f, a, b, nodes):
    if f(a) * f(b) >= 0:
        raise Exception("Invalid interval")
    x_vector = equidistant_nodes_vector(a, b, nodes)
    polynomial = build_polynomial(x_vector, f)
    print(polynomial, "\n")
    root = solve_polynomial(polynomial, a, b)
    print(root)
    show_plot(f, polynomial, a, b, "Task 1")


if __name__ == '__main__':
    print("\n--- First method ---\n")
    task_1(input.f, input.interval[0], input.interval[1], input.nodes)

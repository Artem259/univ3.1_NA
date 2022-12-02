from math import cos, pi

import input
from task import task


def chebyshev_nodes_vector(a, b, nodes):
    x_vector = []
    for i in range(nodes):
        x = (a+b)/2 + ((b-a)/2) * cos((2*i+1)*pi / (2*nodes))
        x_vector.append(x)
    return x_vector


if __name__ == '__main__':
    print("\n--- Task 2 ---\n")
    task(input.f, input.interval[0], input.interval[1], input.nodes, chebyshev_nodes_vector, "Task 2")

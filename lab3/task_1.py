import input
from task import task


def equidistant_nodes_vector(a, b, nodes):
    x_vector = []
    step = (b-a) / (nodes-1)
    for i in range(nodes):
        x_vector.append(a + i*step)
    return x_vector


if __name__ == '__main__':
    print("\n--- Task 1 ---\n")
    task(input.f, input.interval[0], input.interval[1], input.nodes, equidistant_nodes_vector, "Task 1")

from service import build_polynomial, solve_polynomial, show_plot


def task(f, a, b, nodes, f_nodes, label):
    if f(a) * f(b) >= 0:
        raise Exception("Invalid interval")
    x_vector = f_nodes(a, b, nodes)
    print("Nodes = \n", x_vector, "\n")
    polynomial = build_polynomial(x_vector, f)
    print("Polynomial = \n", polynomial, "\n")
    root = solve_polynomial(polynomial, a, b)
    print("x = \n", root)
    show_plot(f, polynomial, a, b, label)

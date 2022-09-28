from math import log, log10, floor


def my_phi(x):
    return -log(2-x**2)


def simple_iteration(func_phi, x0, q, e):
    n0 = floor(log(abs(func_phi(x0)-x0)/((1-q)*e)) / log(1/q)) + 1
    print("n0(e) >= " + str(n0))
    print("-------------------------------------------------")

    x_curr = x0
    while True:
        x_next = func_phi(x_curr)
        print("phi(" + str(x_curr) + ") = " + str(x_next))
        if abs(x_next-x_curr) < (1-q)*e/q:
            break
        x_curr = x_next
    x_next = int(x_next*(10**int(log10(1/e))))*e
    print("-------------------------------------------------")
    print("Result is " + str(x_next))


if __name__ == '__main__':
    simple_iteration(my_phi, -1/5, 30/41, 10**(-4))

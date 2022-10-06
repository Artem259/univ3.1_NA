from math import log, log10, floor


def my_phi(x):
    return -log(2-x**2)


def simple_iteration(func_phi, x0, q, eps):
    n0 = floor(log(abs(func_phi(x0)-x0) / ((1-q) * eps)) / log(1 / q)) + 1
    print("n0(e) >= " + str(n0))
    print("-------------------------------------------------")

    x_curr = x0
    i = 1
    while True:
        x_next = func_phi(x_curr)
        print(str(i) + ": " + str(x_curr) + " ==> " + str(x_next))
        if abs(x_next-x_curr) < (1-q)*eps/q:
            break
        x_curr = x_next
        i += 1
    x_next = int(x_next * (10 ** int(log10(1 / eps)))) * eps
    print("-------------------------------------------------")
    print("Result is " + str(x_next))


if __name__ == '__main__':
    print("\n--- Simple Iteration method ---\n")
    simple_iteration(my_phi, -3/5, 30/41, 10**(-4))

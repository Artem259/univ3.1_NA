from math import e, log, log2, log10, floor


def my_func(x):
    return e**(-x)+x**2-2


def my_func_derivative(x):
    return -e**(-x)+2*x


def modified_newton(func, x0, f_der_x0, eps):
    x_curr = x0
    i = 1
    while True:
        x_next = x_curr - func(x_curr)/f_der_x0
        print(str(i) + ": " + str(x_curr) + " ==> " + str(x_next))
        if abs(x_next - x_curr) <= eps:
            break
        x_curr = x_next
        i += 1
    x_next = int(x_next * (10 ** int(log10(1 / eps)))) * eps
    print("-------------------------------------------------")
    print("Result is " + str(x_next))


if __name__ == '__main__':
    print("\n--- Newton's Modified method ---\n")
    my_x0 = -3/5
    modified_newton(my_func, my_x0, my_func_derivative(my_x0), 10**(-4))

import numpy as np
import input


def jacobi(A, b, e):
    np.set_printoptions(precision=4, floatmode='fixed')
    print("A = \n", A, "\n")
    print("b = \n", b, "\n")
    print("e =", e, "\n")
    print("--------------------------\n")
    N = len(A)
    flag = True
    for i in range(N):
        string = ""
        string += "|" + str(A[i][i]) + "| >= "
        row_sum = 0
        for j in range(N):
            if j == i:
                continue
            if string[-2] != "=":
                string += " + "
            row_sum += abs(A[i][j])
            string += "|" + str(A[i][j]) + "|"
        if abs(A[i][i]) >= row_sum:
            string = "(TRUE) " + string
        else:
            string = "(FALSE)" + string
            flag = False
        print(string)
    if flag:
        print("\n[TRUE]\n")
    else:
        print("\n[FALSE]\n")
    print("--------------------------\n")

    x_next = np.array([0] * N, float)
    iteration = 1
    while True:
        x_curr = x_next.copy()
        for i in range(N):
            x_next[i] = -np.sum([A[i][j]*x_curr[j]/A[i][i] for j in range(i)])
            x_next[i] -= np.sum([A[i][j]*x_curr[j]/A[i][i] for j in range(i+1, N)])
            x_next[i] += b[i]/A[i][i]
        norm = np.max(abs(x_next - x_curr))
        if norm <= e or iteration == 1:
            print("[" + str(iteration) + "] norm (inf) =", norm)
            if norm <= e:
                break
        iteration += 1
    np.set_printoptions(precision=8, floatmode='fixed')
    print("\nx = \n", x_next, "\n")


if __name__ == '__main__':
    print("\n--- Jacobi method ---\n")

    jacobi(input.A_, input.b_, 0.001)
    # jacobi(np.array([[3, -1, 1], [-1, 2, 0.5], [1, 0.5, 3]]),
    #        np.array([1, 1.75, 2.5]), 0.9)

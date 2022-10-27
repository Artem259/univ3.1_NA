import numpy as np
import input


def matrix_norm(M):
    res = 0
    for row in M:
        res = max(res, sum(abs(row)))
    return res


def condition_number(A):
    print("A = \n", A, "\n")
    print("--------------------------\n")

    inv_A = np.linalg.inv(A)
    print("A^(-1) = \n", inv_A, "\n")

    norm_A = matrix_norm(A)
    norm_inv_A = matrix_norm(inv_A)
    print("|| A || = ", norm_A, "\n")
    print("|| A^(-1) || = ", norm_inv_A, "\n")

    cond = norm_A * norm_inv_A
    print("cond(A) = ", cond, "\n")


if __name__ == '__main__':
    print("\n--- Condition Number ---\n")
    np.set_printoptions(precision=4, floatmode='fixed')

    condition_number(input.A_)
    # condition_number(np.array([[1, 0.99], [0.99, 0.98]]))

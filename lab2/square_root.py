from input import *
import input


def square_root(A, b):
    print("A = \n", A, "\n")
    print("b = \n", b, "\n")
    print("--------------------------\n")
    if not np.array_equal(A, A.transpose()):
        raise Exception("Matrix A is not symmetric")
    N = len(A)
    S = np.array([0] * (N**2), float).reshape(N, N)
    D = np.array([0] * (N**2), float).reshape(N, N)

    for i in range(N):
        D[i][i] = np.sign(A[i][i] - np.sum(
            [D[p][p] * S[p][i]**2 for p in range(i)]))
        S[i][i] = np.sqrt(abs(A[i][i] - np.sum(
            [D[p][p] * S[p][i]**2 for p in range(i)])))
        for j in range(i+1, N):
            S[i][j] = A[i][j] - np.sum(
                [S[p][i]*D[p][p]*S[p][j] for p in range(i)])
            S[i][j] /= D[i][i] * S[i][i]
    print("S = \n", S, "\n")
    print("D = \n", D, "\n")

    STD = np.array(np.matrix(S).transpose() * D)
    print("STD = \n", STD, "\n")

    y = np.array([0] * N, float)
    for i in range(N):
        y[i] = b[i] - np.sum(
            [STD[i][j]*y[j] for j in range(i)])
        y[i] /= STD[i][i]
    print("y = \n", y, "\n")

    x = np.array([0] * N, float)
    for i in reversed(range(N)):
        x[i] = y[i] - np.sum(
            [S[i][j] * x[j] for j in reversed(range(N)[i+1:])])
        x[i] /= S[i][i]
    print("x = \n", x, "\n")


if __name__ == '__main__':
    print("\n--- Square Root method ---\n")
    np.set_printoptions(precision=4, floatmode='fixed')
    square_root(input.A_, input.b_)

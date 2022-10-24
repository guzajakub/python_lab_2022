import numpy as np


def sum_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1))] for i in range(len(matrix1))]


if __name__ == "__main__":
    dim = 128
    A = np.random.rand(dim, dim)
    B = np.random.rand(dim, dim)

    if np.allclose(sum_matrices(A, B), np.add(A, B)):
        print("Proper implementation of custom adding method")
    else:
        print("Wrong implementation of custom adding method")

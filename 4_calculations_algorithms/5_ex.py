import numpy as np


def mult_matrices(matrix1, matrix2):
    if len(matrix1[0]) == len(matrix2):
        result = np.zeros(shape=(len(matrix1[0]), len(matrix2)))
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += A[i][k] * B[k][j]
        return result
    else:
        print("Lengths of matrices doesn't match")


if __name__ == "__main__":
    dim = 8
    A = np.random.rand(dim, dim)
    B = np.random.rand(dim, dim)

    if np.allclose(mult_matrices(A, B), np.array(A) @ np.array(B)):
        print("Proper implementation of custom multiplying method")
    else:
        print("Wrong implementation of custom multiplying method")

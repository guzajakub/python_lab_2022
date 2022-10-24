import numpy as np
import copy


def smaller_matrix(bigger_matrix, row, col):
    small_matrix = copy.deepcopy(bigger_matrix)
    small_matrix = np.delete(small_matrix, row, 0)  # remove rows
    small_matrix = np.delete(small_matrix, col, 1)  # remove rows
    return small_matrix


def determinant(matrix):
    matrix_cols, matrix_rows = len(matrix[0]), len(matrix)

    if matrix_rows != matrix_cols:
        raise ValueError("It is impossible to calculate a determinant from that matrix")

    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return det
    else:
        det = 0
        # iterate over rows
        for idx in range(matrix_cols):
            det += ((-1) ** idx) * matrix[0][idx] * determinant(smaller_matrix(matrix, 0, idx))
        return det


if __name__ == "__main__":
    dim = 8
    A = np.random.randint(10, size=(dim, dim))

    if np.allclose(determinant(A), np.linalg.det(A)):
        print("Proper implementation of custom determinant method")
    else:
        print("Wrong implementation of custom determinant method")


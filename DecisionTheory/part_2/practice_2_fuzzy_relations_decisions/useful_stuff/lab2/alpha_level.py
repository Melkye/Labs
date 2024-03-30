import numpy as np


def alpha_cut_matrix(matrix, alpha):
    alpha_level = np.where(matrix >= alpha, 1, 0)
    return alpha_level


def alpha_cut(matrix, alpha):
    alpha_level = []
    n = matrix.shape[0]
    for i in range(n):
        for j in range(n):
            if matrix[i, j] >= alpha:
                alpha_level.append((i+1, j+1))
    return alpha_level

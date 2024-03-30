import numpy as np


def strict_preference_relation(matrix):
    n = matrix.shape[0]
    preference_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i, j] > matrix[j, i]:
                preference_matrix[i, j] = matrix[i, j] - matrix[j, i]
    return preference_matrix


def indifference_relation(matrix):
    n = matrix.shape[0]
    indifference_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            max_value = max(1 - max(matrix[i, j], matrix[j, i]), min(matrix[i, j], matrix[j, i]))
            indifference_matrix[i, j] = max_value
    return indifference_matrix


def quasi_equivalence_relation(matrix):
    n = matrix.shape[0]
    quasi_equivalence_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            quasi_equivalence_matrix[i, j] = min(matrix[i, j], matrix[j, i])
    return quasi_equivalence_matrix

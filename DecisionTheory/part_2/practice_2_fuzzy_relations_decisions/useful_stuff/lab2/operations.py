import numpy as np


def fuzzy_union(set1, set2):
    return np.maximum(set1, set2)


def fuzzy_intersection(set1, set2):
    return np.minimum(set1, set2)


def fuzzy_complement(set1):
    return 1 - set1


def fuzzy_composition(matrix1, matrix2):
    result = np.zeros_like(matrix1)
    for i in range(matrix1.shape[0]):
        for j in range(matrix1.shape[1]):
            min_values = []
            for k in range(matrix1.shape[0]):
                min_values.append(min(matrix1[i, k], matrix2[k, j]))
            result[i, j] = max(min_values)
    return result

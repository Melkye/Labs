import numpy as np


def max_col(matrix):
    max_values = np.max(matrix, axis=0)
    return 1 - max_values


def rank_list(result):
    sorted_indices = np.argsort(result)[::-1]
    ranks = np.arange(len(result))[sorted_indices]
    ranked_list = [(i + 1, rank + 1) for rank, i in enumerate(sorted_indices)]
    return ranked_list


def rank_list_range(result):
    sorted_indices = np.argsort(result)[::-1]
    ranks = np.arange(len(result))[sorted_indices]
    ranked_list = [(i + 1) for i in enumerate(sorted_indices)]
    return ranked_list

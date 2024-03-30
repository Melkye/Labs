from operations import fuzzy_intersection
import numpy as np


def P_solution(expert_data):
    n = expert_data[1].shape[0]
    P = np.ones((n, n))
    for i in range(len(expert_data)):
        P=fuzzy_intersection(P, expert_data[i+1])
    return P


def Q_solution(expert_data, weights):
    n = expert_data[1].shape[0]
    Q = np.zeros((n, n))
    total_weight = sum(weights)
    normalized_weights = [weight / total_weight for weight in weights]
    for i in range(len(expert_data)):
        multiple = expert_data[i+1]*normalized_weights[i]
        Q = Q+multiple
    return Q
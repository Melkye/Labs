# expert_1_weight = 0.2
# expert_2_weight = 0.42
# expert_3_weight = 0.11
# expert_4_weight = 0.07
# expert_5_weight = 0.2


def get_R_s(relation):
    R_s = [[0 for _ in range(len(relation))] for _ in range(len(relation))]
    for i in range(len(relation)):
        for j in range(len(relation)):
            if (relation[i][j] > relation[j][i]):
                R_s[i][j] = relation[i][j] - relation[j][i]
            else:
                R_s[i][j] = 0
    return R_s


quasi_inf = 100


def get_mu_nd(R_s):
    mu_nd = [quasi_inf for _ in range(len(R_s))]
    for j in range(len(R_s)):
        for i in range(len(R_s)):
            if 1 - R_s[i][j] < mu_nd[j]:
                mu_nd[j] = 1 - R_s[i][j]
    return mu_nd


def select_best(alternatives_marks):
    alternative_index = -1
    alternative_mark = 0
    for index, mark in enumerate(alternatives_marks):
        if mark > alternative_mark:
            alternative_mark = mark
            alternative_index = index
    return alternative_index + 1

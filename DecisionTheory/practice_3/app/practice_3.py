# def get_delta(x, y):
#     delta = []
#     for i in range(len(x)):
#         delta.append(x[i] - y[i])
#     return delta


# def get_sigma(delta):
#     sigma = []
#     for i in range(len(delta)):
#         if delta[i] > 0:
#             sigma.append(1)
#         elif delta[i] < 0:
#             sigma.append(-1)
#         else:
#             sigma.append(0)
#     return sigma


def get_sigma(x, y):
    sigma = []
    for i in range(len(x)):
        delta_i = x[i] - y[i]
        if delta_i > 0:
            sigma.append(1)
        elif delta_i < 0:
            sigma.append(-1)
        else:
            sigma.append(0)
    return sigma


def get_sigma_matrix(alternatives_ratings_by_criteria):
    sigma_matrix = []

    # num of rows = num of alternatives
    for x in range(len(alternatives_ratings_by_criteria)):
        sigma_matrix.append([])
        for y in range(len(alternatives_ratings_by_criteria)):
            sigma = get_sigma(
                alternatives_ratings_by_criteria[x], alternatives_ratings_by_criteria[y])
            sigma_matrix[x].append(sigma)

# ---


def get_pareto_relation(alternatives_ratings_by_criteria):
    sigma_matrix = get_sigma_matrix(alternatives_ratings_by_criteria)

    pareto_relation = []
    for x in range(len(alternatives_ratings_by_criteria)):
        pareto_relation.append([])

        for y in range(len(alternatives_ratings_by_criteria)):
            is_added = False

            for i in range(len(sigma_matrix[x][y])):
                if sigma_matrix[x][y][i] < 0:
                    pareto_relation[x].append(0)
                    is_added = True
                    break
            if not is_added:
                pareto_relation[x].append(1)

    return pareto_relation


def get_majoritar_relation(alternatives_ratings_by_criteria):
    sigma_matrix = get_sigma_matrix(alternatives_ratings_by_criteria)

    majoritar_relation = []
    for x in range(len(alternatives_ratings_by_criteria)):
        majoritar_relation.append([])

        for y in range(len(alternatives_ratings_by_criteria)):
            sum_sigma = 0
            for i in range(len(sigma_matrix[x][y])):
                sum_sigma += sigma_matrix[x][y][i]

            if sum_sigma > 0:
                majoritar_relation[x].append(1)
            else:
                majoritar_relation[x].append(0)

    return majoritar_relation


def get_lexicographic_relation(alternatives_ratings_by_criteria, criteria_importance_desc):

    alternatives_ratings_by_criteria_ordered_by_desc_importance = alternatives_ratings_by_criteria[
        :]

    for i in range(len(criteria_importance_desc)):
        alternatives_ratings_by_criteria_ordered_by_desc_importance[
            i] = alternatives_ratings_by_criteria[criteria_importance_desc[i]]

    sigma_matrix_ordered_by_criteria_desc_importance = get_sigma_matrix(
        alternatives_ratings_by_criteria_ordered_by_desc_importance)

    lexicographic_relation = []

    for x in range(len(alternatives_ratings_by_criteria)):
        lexicographic_relation.append([])

        for y in range(len(alternatives_ratings_by_criteria)):

            is_added = False
            for i in range(len(sigma_matrix_ordered_by_criteria_desc_importance[x][y])):

                if sigma_matrix_ordered_by_criteria_desc_importance[x][y][i] > 0:
                    lexicographic_relation[x].append(1)
                    is_added = True
                    break
                elif sigma_matrix_ordered_by_criteria_desc_importance[x][y][i] == 0:
                    pass
                else:
                    lexicographic_relation[x].append(0)
                    is_added = True
                    break
            if is_added:
                break

    return lexicographic_relation

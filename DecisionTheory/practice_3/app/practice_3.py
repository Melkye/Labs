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

    return sigma_matrix

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

    sigma_matrix = get_sigma_matrix(alternatives_ratings_by_criteria)

    lexicographic_relation = []

    for x in range(len(alternatives_ratings_by_criteria)):
        lexicographic_relation.append([])

        for y in range(len(alternatives_ratings_by_criteria)):

            is_added = False

            for i in range(len(criteria_importance_desc)):
                if sigma_matrix[x][y][criteria_importance_desc[i]] > 0:
                    lexicographic_relation[x].append(1)
                    is_added = True
                    break
                elif sigma_matrix[x][y][criteria_importance_desc[i]] == 0:
                    pass
                else:
                    lexicographic_relation[x].append(0)
                    is_added = True
                    break
            if not is_added:
                lexicographic_relation[x].append(0)

    return lexicographic_relation


def get_berezosky_relation(alternatives_ratings_by_criteria, quasi_groups):

    def get_i_matrix_pareto(sigma_matrix):
        i_matrix_pareto = []

        for i in range(len(sigma_matrix)):
            i_matrix_pareto.append([])

            for j in range(len(sigma_matrix)):
                sigma = sigma_matrix[i][j]
                if all(sigma_k == 0 for sigma_k in sigma):
                    i_matrix_pareto[i].append(1)
                else:
                    i_matrix_pareto[i].append(0)
        return i_matrix_pareto

    def get_p_matrix_pareto(sigma_matrix):
        p_matrix_pareto = []

        for i in range(len(sigma_matrix)):
            p_matrix_pareto.append([])

            for j in range(len(sigma_matrix)):
                sigma = sigma_matrix[i][j]
                is_greater = False
                is_lower = False
                for sigma_k in sigma:
                    if sigma_k == 1:
                        is_greater = True
                    elif sigma_k == -1:
                        is_lower = True
                if is_greater and not is_lower:
                    p_matrix_pareto[i].append(1)
                else:
                    p_matrix_pareto[i].append(0)
        return p_matrix_pareto

    def get_n_matrix_pareto(sigma_matrix):
        n_matrix_pareto = []

        for i in range(len(sigma_matrix)):
            n_matrix_pareto.append([])

            for j in range(len(sigma_matrix)):
                sigma = sigma_matrix[i][j]
                is_greater = False
                is_lower = False
                for sigma_k in sigma:
                    if sigma_k == 1:
                        is_greater = True
                    elif sigma_k == -1:
                        is_lower = True
                if is_greater and is_lower:
                    n_matrix_pareto[i].append(1)
                else:
                    n_matrix_pareto[i].append(0)
        return n_matrix_pareto

    p_matrix_prev = []
    i_matrix_prev = []
    n_matrix_prev = []

    for l in range(len(quasi_groups)):
        current_criteria = quasi_groups[l]
        quasi_system = []

        for i in range(len(alternatives_ratings_by_criteria)):
            quasi_system.append([])

            for j in range(len(current_criteria)):
                quasi_system[i].append(
                    alternatives_ratings_by_criteria[i][current_criteria[j]])

        # print(f"Ітерація {l+1}")
        # print_array(quasi_system)

        sigma_matrix = get_sigma_matrix(quasi_system)

        i_matrix = get_i_matrix_pareto(sigma_matrix)
        # print(f"I0{l+1} таблиця")
        # print_relation(i_matrix)

        p_matrix = get_p_matrix_pareto(sigma_matrix)
        # print(f"P0{l+1} таблиця")
        # print_relation(p_matrix)

        n_matrix = get_n_matrix_pareto(sigma_matrix)
        # print(f"N0{l+1} таблиця")
        # print_relation(n_matrix)

        if l == 0:
            i_matrix_prev = i_matrix
            n_matrix_prev = n_matrix
            p_matrix_prev = p_matrix
            continue

        berezovsky_relation = []

        for i in range(len(alternatives_ratings_by_criteria)):
            berezovsky_relation.append([])

            for j in range(len(alternatives_ratings_by_criteria)):
                if p_matrix[i][j] == 1 and (p_matrix_prev[i][j] == 1 or n_matrix_prev[i][j] == 1 or i_matrix_prev[i][j] == 1):
                    berezovsky_relation[i].append(1)
                elif i_matrix[i][j] == 1 and p_matrix_prev[i][j] == 1:
                    berezovsky_relation[i].append(1)
                else:
                    berezovsky_relation[i].append(0)

        i_matrix = []
        for i in range(len(alternatives_ratings_by_criteria)):
            i_matrix.append([])
            for j in range(len(alternatives_ratings_by_criteria)):
                if i_matrix[i][j] == 1 and i_matrix_prev[i][j] == 1:
                    i_matrix[i].append(1)
                else:
                    i_matrix[i].append(0)

        n_matrix = []
        for i in range(len(alternatives_ratings_by_criteria)):
            n_matrix.append([])
            for j in range(len(alternatives_ratings_by_criteria)):
                if not (berezovsky_relation[i][j] == 1 or berezovsky_relation[j][i] == 1 or i_matrix[i][j] == 1):
                    n_matrix[i].append(1)
                else:
                    n_matrix[i].append(0)

        # print(f"RB{l+1}")
        # print_relation(berezovsky_relation)

        # print(f"NB{l+1}")
        # print_relation(n_matrix)

        # print(f"IB{l+1}")
        # print_relation(i_matrix)

        n_matrix_prev = n_matrix
        i_matrix_prev = i_matrix
        p_matrix_prev = berezovsky_relation

    return berezovsky_relation


def print_relation(relation):
    for row in relation:
        for element in row:
            if isinstance(element, int) or isinstance(element, float):
                print_to_file("{:.0f}".format(element) + "  ", end="")
            else:
                print_to_file(element + "  ", end="")
        print_to_file()


def print_to_file(data="", end="\n"):
    with open("Var-01-АдамовДенис.txt", "a") as file:
        file.write(str(data))
        file.write(end)


def main():
    pareto_relation = get_pareto_relation(alternatives_ratings_by_criteria)
    majoritar_relation = get_majoritar_relation(
        alternatives_ratings_by_criteria)
    lexicographic_relation = get_lexicographic_relation(
        alternatives_ratings_by_criteria, criteria_importance_desc)
    berezosky_relation = get_berezosky_relation(
        alternatives_ratings_by_criteria, quasi_groups)

    with open("Var-01-АдамовДенис.txt", "w") as file:
        file.truncate()
    print_to_file(1)
    print_relation(pareto_relation)
    print_to_file(2)
    print_relation(majoritar_relation)
    print_to_file(3)
    print_relation(lexicographic_relation)
    print_to_file(4)
    print_relation(berezosky_relation)
# ---

# yulia's


# alternatives_ratings_by_criteria = [
#     [3, 1, 7, 2, 3, 9, 8, 5, 2, 8, 5, 7],
#     [9, 1, 7, 5, 9, 9, 8, 5, 2, 8, 7, 7],
#     [9, 5, 7, 7, 9, 9, 8, 5, 2, 8, 7, 7],
#     [9, 9, 7, 7, 9, 9, 8, 5, 5, 8, 7, 7],
#     [9, 9, 7, 8, 9, 9, 10, 8, 9, 10, 7, 7],
#     [3, 4, 3, 2, 6, 3, 5, 6, 7, 9, 3, 7],
#     [9, 9, 7, 8, 9, 9, 10, 8, 10, 10, 10, 7],
#     [3, 9, 7, 8, 3, 2, 9, 1, 6, 9, 6, 5],
#     [3, 1, 1, 1, 3, 2, 5, 1, 2, 8, 6, 5],
#     [10, 5, 6, 1, 9, 9, 5, 8, 5, 8, 10, 7],

#     [2, 3, 3, 1, 4, 2, 4, 5, 5, 2, 2, 4],
#     [8, 9, 3, 3, 8, 7, 4, 5, 6, 9, 2, 4],
#     [3, 1, 3, 3, 7, 5, 4, 5, 2, 5, 2, 4],
#     [3, 1, 2, 3, 7, 5, 4, 3, 2, 1, 2, 4],
#     [3, 1, 2, 2, 3, 5, 4, 3, 2, 1, 2, 4],
#     [9, 7, 3, 2, 4, 5, 10, 3, 6, 3, 6, 5],
#     [9, 9, 8, 8, 9, 9, 10, 8, 9, 10, 7, 7],
#     [9, 9, 8, 8, 9, 9, 10, 8, 9, 10, 7, 7],
#     [9, 9, 8, 8, 9, 9, 10, 8, 9, 10, 8, 7],
#     [9, 9, 8, 8, 9, 9, 10, 10, 9, 10, 8, 7]
# ]

# criteria_importance_desc = [10, 2, 8, 9, 7, 4, 12, 3, 5, 1, 11, 6]

# nastia's

alternatives_ratings_by_criteria = [
    [8, 8, 10, 1, 3, 2, 1, 9, 4, 6, 5, 9],
    [8, 6, 9, 1, 3, 2, 1, 6, 4, 1, 5, 6],
    [6, 4, 4, 1, 3, 2, 1, 4, 4, 1, 5, 5],
    [5, 4, 4, 1, 2, 2, 1, 2, 4, 1, 4, 5],
    [8, 8, 10, 9, 8, 6, 2, 9, 4, 10, 5, 9],
    [8, 7, 7, 8, 6, 5, 2, 4, 2, 5, 2, 9],
    [2, 4, 6, 4, 2, 5, 2, 3, 1, 5, 2, 9],
    [2, 4, 6, 4, 2, 4, 2, 3, 1, 4, 2, 8],
    [6, 10, 6, 6, 7, 5, 3, 10, 6, 5, 10, 9],
    [10, 10, 6, 6, 10, 8, 3, 10, 6, 6, 10, 9],
    [2, 1, 6, 4, 2, 2, 2, 3, 1, 4, 2, 8],
    [5, 2, 10, 4, 3, 2, 8, 6, 4, 4, 10, 8],
    [5, 2, 6, 4, 1, 2, 1, 6, 4, 2, 7, 3],
    [9, 2, 6, 4, 1, 6, 5, 8, 4, 10, 7, 3],
    [9, 6, 9, 4, 9, 6, 8, 8, 4, 10, 7, 9],
    [9, 6, 9, 4, 9, 6, 8, 9, 4, 10, 7, 9],
    [8, 3, 2, 1, 6, 6, 8, 3, 4, 10, 7, 9],
    [8, 1, 2, 1, 6, 4, 8, 3, 1, 2, 3, 4],
    [8, 10, 6, 9, 7, 5, 8, 10, 6, 7, 10, 9],
    [10, 10, 6, 9, 7, 10, 8, 10, 8, 7, 10, 9]
]

criteria_importance_desc = [8, 10, 3, 0, 4, 5, 11, 2, 1, 7, 9, 6]
quasi_groups = [[1, 3, 5, 8], [6, 7, 10], [0, 2, 4, 9, 11]]


# mine

# alternatives_ratings_by_criteria = [
#     [4, 6, 9,  4, 6,  5,  7, 10,  6,  8,  8,  9],
#     [4,  6,  9,  4,  6,  6,  7, 10,  6,  9,  8,  9],
#     [2,  6,  9,  4,  6,  5,  6, 10,  1,  5,  8,  6],
#     [2,  8, 10,  9,  6,  8,  6, 10,  7, 10,  8,  8],
#     [10,  8, 10,  9,  7,  8,  6, 10,  7, 10,  8,  8],
#     [6,  6,  3,  6,  7,  1,  3,  5,  7,  5,  2,  5],
#     [2,  6,  2,  6,  6,  1,  2,  5,  6,  1,  2,  5],
#     [2,  2,  2,  6,  2,  1,  2,  4,  6,  1,  2,  2],
#     [6,  8,  4,  8,  7,  3,  5,  5,  7,  6,  5,  8],
#     [6,  4,  4,  7,  3,  3,  5,  1,  3,  5,  3,  2],
#     [7,  6,  9, 10,  6,  5,  7, 10,  6,  8,  8,  9],
#     [7,  6,  9, 10,  9,  5,  7, 10, 10,  8,  8,  9],
#     [6,  2,  4,  2,  3,  3,  1,  1,  2,  4,  3,  2],
#     [6,  1,  3,  2,  3,  3,  1,  1,  2,  4,  3,  2],
#     [6,  1,  3,  2,  3,  1,  1,  1,  2,  4,  2,  2],
#     [6,  1,  3,  2,  3,  1,  1,  1,  2,  2,  2,  1],
#     [10, 10,  6,  6,  4,  7,  7,  5,  8,  8, 9,  5],
#     [6,  4,  6,  5,  4,  1,  1,  5,  3,  8,  9,  5],
#     [6,  4,  4,  3,  3,  1, 1,  1,  3,  5,  3,  2],
#     [6, 10,  8,  9,  3,  3,  1,  8,  3,  7,  9,  6]
# ]
# criteria_importance_desc = [5, 3, 9, 1, 10, 2,, 7, 11, 0, 4, 8, 6]
# quasi_groups = [[2, 7, 10], [3, 4, 11], [0, 1, 5, 6, 8, 9]]
main()

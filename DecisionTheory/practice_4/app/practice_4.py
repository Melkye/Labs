import numpy as np


def print_relation(relation):
    for row in relation:
        for element in row:
            if isinstance(element, int) or isinstance(element, float):
                print_to_file("{:.0f}".format(element) + "  ", end="")
            else:
                print_to_file(element + "  ", end="")
        print_to_file()


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print_to_file("{:.3f}".format(element) + "  ", end="")
        print_to_file()


def print_to_file(data="", filename="Var-01-АдамовДенис.txt", end="\n"):
    with open(filename, "a") as file:
        file.write(str(data))
        file.write(end)


def calc_concordance(alternatives_ratings_by_criteria, criteria_weights):

    def calc_one_concordance_index(a, b):
        num = 0
        for column in range(len(criteria_weights)):
            if alternatives_ratings_by_criteria[a][column] \
                    >= alternatives_ratings_by_criteria[b][column]:
                num += criteria_weights[column]

        return round(num / sum(criteria_weights), 3)

    c_matrix = []

    for row in range(len(alternatives_ratings_by_criteria)):
        c_matrix.append([])

        for column in range(len(alternatives_ratings_by_criteria)):
            value = 0
            if row != column:
                value = calc_one_concordance_index(row, column)

            c_matrix[row].append(value)

    print_to_file("Concordance indexes matrix")
    print_matrix(c_matrix)
    return c_matrix


def calc_discordance(alternatives_ratings_by_criteria, criteria_weights):

    def calc_one_discordance_index(a, b):
        max_num = 0
        max_denom = 0

        for column in range(len(criteria_weights)):
            if alternatives_ratings_by_criteria[a][column] >= alternatives_ratings_by_criteria[b][column]:
                pass
                # return 0
            else:
                k_max = alternatives_ratings_by_criteria[0][column]
                k_min = alternatives_ratings_by_criteria[0][column]

                for i in range(len(alternatives_ratings_by_criteria)):
                    if alternatives_ratings_by_criteria[i][column] > k_max:
                        k_max = alternatives_ratings_by_criteria[i][column]

                    if alternatives_ratings_by_criteria[i][column] < k_min:
                        k_min = alternatives_ratings_by_criteria[i][column]

                rate_range = k_max - k_min

                num = criteria_weights[column] * \
                    (alternatives_ratings_by_criteria[b][column] -
                     alternatives_ratings_by_criteria[a][column])

                denom = criteria_weights[column] * rate_range

                if max_num < num:
                    max_num = num

                if max_denom < denom:
                    max_denom = denom

        if max_num == 0:
            return 0
        else:
            return round(max_num / max_denom, 3)

    d_matrix = []
    for row in range((len(alternatives_ratings_by_criteria))):
        d_matrix.append([])

        for column in range(len(alternatives_ratings_by_criteria)):
            value = 1
            if row != column:
                value = calc_one_discordance_index(row, column)

            d_matrix[row].append(value)

    print_to_file("Discordance indexes matrix")
    print_matrix(d_matrix)
    return d_matrix


def get_relation(alternatives_ratings_by_criteria,
                 criteria_weights,
                 c,
                 d):

    c_matrix = calc_concordance(
        alternatives_ratings_by_criteria, criteria_weights)
    d_matrix = calc_discordance(
        alternatives_ratings_by_criteria, criteria_weights)

    relation = [[0] * len(alternatives_ratings_by_criteria)
                for _ in range(len(alternatives_ratings_by_criteria))]

    for row in range(len(alternatives_ratings_by_criteria)):
        # TODO check if it is the right len()
        for column in range(len(alternatives_ratings_by_criteria)):
            if row == column:
                relation[row][column] = 0
            elif c_matrix[row][column] >= c and d_matrix[row][column] <= d:
                relation[row][column] = 1
            else:
                relation[row][column] = 0

    print_to_file(f"c = {c}     d = {d}")
    print_to_file("Relation:")
    print_relation(relation)

    return relation


def has_cycle(relation):

    def does_vertex_has_cycle(vertex_index):
        reachable_vertexes = set()
        visited_vertexes = set()

        for (index, value) in enumerate(relation[vertex_index]):
            if value == 1:
                reachable_vertexes.add(index)

        visited_vertexes.add(vertex_index)

        if reachable_vertexes.__contains__(vertex_index):
            return True

        while len(visited_vertexes) != len(relation) and len(reachable_vertexes) > 0:
            unvisited_reachable_vertexes = reachable_vertexes.difference(
                visited_vertexes)
            if len(unvisited_reachable_vertexes) == 0:
                return False
            current_vertex = unvisited_reachable_vertexes.pop()
            visited_vertexes.add(current_vertex)

            for (index, value) in enumerate(relation[current_vertex]):
                if value == 1:
                    if index == vertex_index:
                        return True
                    reachable_vertexes.add(index)

            visited_vertexes.add(current_vertex)

        return False

    for vertex_index in range(len(relation)):
        if does_vertex_has_cycle(vertex_index):
            return True
    return False


def solve_NM(relation):

    def get_upper_cut(vertex):
        vertexes = set()

        for row in range(len(relation)):
            if relation[row][vertex] == 1:
                vertexes.add(row)

        return vertexes

        # return set(index for (index, value) in enumerate(relation[:, vertex]) if value == 1)

    def get_S_sets():
        all_S_sets = [set()]

        # S[0]
        for vertex in range(len(relation)):
            if len(get_upper_cut(vertex)) == 0:
                all_S_sets[0].add(vertex)

        # S[k]
        while len(all_S_sets[-1]) != len(relation):
            vertexes_dominated_only_by_prev_S = set(vertex for vertex in range(len(relation))
                                                    if get_upper_cut(vertex).issubset(all_S_sets[-1]))

            all_S_sets.append(
                all_S_sets[-1].union(vertexes_dominated_only_by_prev_S))

        return all_S_sets

    def get_Q_sets(all_S_sets):
        all_Q_sets = [all_S_sets[0]]
        for i in range(1, len(all_S_sets)):
            diff_S_curr_and_S_prev = all_S_sets[i].difference(all_S_sets[i-1])

            just_the_required_condition = set(vertex for vertex in diff_S_curr_and_S_prev
                                              if len(get_upper_cut(vertex).intersection(all_Q_sets[-1])) == 0)

            all_Q_sets.append(
                all_Q_sets[-1].union(just_the_required_condition))
        return all_Q_sets

    def check_internal_stability(vertexes):
        for row in vertexes:
            for column in vertexes:
                if relation[row][column] == 1:
                    return False
        return True

    def check_external_stability(vertexes):
        other_vertexes = set(range(len(relation))).difference(vertexes)
        for column in other_vertexes:
            found_better_in_set = False
            for row in vertexes:
                if relation[row][column] == 1:
                    found_better_in_set = True
                    break
            if found_better_in_set == False:
                return False
        return True

    S_sets = get_S_sets()

    Q_sets = get_Q_sets(S_sets)
    solution = Q_sets[-1]

    int_stab = check_internal_stability(solution)
    ext_stab = check_external_stability(solution)

    print_to_file(f"Neumann-Morgenstern solution: {solution}")
    print_to_file(f"Internal stability: {int_stab}")
    print_to_file(f"External stability: {ext_stab}")
    print_to_file()


def main():

    with open("Var-01-АдамовДенис.txt", "w") as file:
        file.truncate()

    relation = get_relation(
        alternatives_ratings_by_criteria, criteria_weights, c, d)

    if not has_cycle(relation):
        print_to_file(
            f"Relation is acyclic. Neumann-Morgenstern optimization will be used.")
        solve_NM(relation)
    else:
        print_to_file(
            f"Relation contains a cycle.")


alternatives_ratings_by_criteria = [
    [9, 3, 3, 7, 7, 3, 2, 9, 7, 6, 9, 10],
    [1, 5, 10, 4, 5, 6, 5, 10, 10, 4, 6, 7],
    [9, 4, 3, 6, 4, 4, 8, 3, 6, 6, 8, 9],
    [4, 9, 9, 3, 6, 9, 7, 7, 4, 1, 7, 4],
    [10, 8, 10, 10, 1, 8, 5, 8, 10, 2, 5, 2],
    [2, 6, 10, 10, 3, 8, 2, 10, 8, 8, 1, 7],
    [6, 5, 10, 5, 2, 8, 5, 3, 3, 9, 7, 1],
    [4, 9, 5, 4, 6, 10, 5, 5, 6, 4, 1, 8],
    [1, 10, 7, 2, 4, 1, 2, 5, 3, 3, 4, 4],
    [10, 10, 9, 4, 8, 3, 2, 5, 1, 6, 9, 9],
    [5, 2, 4, 4, 6, 4, 7, 8, 7, 8, 10, 5],
    [2, 5, 8, 4, 4, 3, 4, 4, 1, 7, 9, 2],
    [3, 5, 7, 3, 1, 5, 1, 8, 9, 3, 8, 2],
    [10, 2, 10, 4, 6, 2, 2, 10, 10, 4, 5, 7],
    [10, 6, 9, 8, 5, 6, 5, 3, 8, 6, 9, 9]
]

criteria_weights = [6, 3, 7, 6, 7, 2, 6, 2, 5, 2, 3, 7]
# c = 0.657
# d = 0.356

c = 0
d = 1

main()

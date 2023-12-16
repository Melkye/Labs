import numpy as np
from typing import List, Set


def read_relations(filename, size, count):
    relations = [np.zeros((size, size)) for _ in range(count)]

    def read_one_relation(file):
        # skip first row of a relation because it only contains name and dashes (---)
        file.readline()

        for row in range(size):
            line = file.readline()
            column = 0
            for char in line:
                if char != ' ' and (char == '1' or char == '0'):
                    relations[num_rel][row][column] = int(char)
                    column += 1

    with open(filename, "r") as file:
        for num_rel in range(count):
            read_one_relation(file)

    return relations


def print_relation(relation, num_rel=0):
    if num_rel != 0:
        print_to_file(f"Relation #{num_rel}")
    for row in relation:
        for element in row:
            if isinstance(element, int) or isinstance(element, float):
                print_to_file("{:.0f}".format(element) + " ", end="")
            else:
                print_to_file(element + " ", end="")
        print_to_file()
    print_to_file()


def print_to_file(data="", end="\n"):
    with open("results.txt", "a") as file:
        file.write(str(data))
        file.write(end)
# ----------


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
        return set(index for (index, value) in enumerate(relation[:, vertex]) if value == 1)

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

    def get_Q_sets(all_S_sets: List[Set]):
        all_Q_sets = [all_S_sets[0]]  # need to make a copy explicitly?
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

    def print_sets(sets, type):
        for (index, set) in enumerate(sets):
            print_to_file(f"{type}{index}: {set}")
        print_to_file()

    S_sets = get_S_sets()
    # print_sets(S_sets, "S")

    Q_sets = get_Q_sets(S_sets)
    solution = Q_sets[-1]
    # print_sets(Q_sets, "Q")

    int_stab = check_internal_stability(solution)
    ext_stab = check_external_stability(solution)

    print_to_file(f"Neumann-Morgenstern solution: {solution}")
    print_to_file(f"Internal stability: {int_stab}")
    print_to_file(f"External stability: {ext_stab}")
    print_to_file()


def solve_k_optimization(relation):

    def get_PIN_matrix():
        PIN_matrix = [[] for _ in range(len(relation))]

        for row in range(len(relation)):
            for column in range(len(relation)):
                if relation[row][column] == 1 and relation[column][row] == 0:
                    PIN_matrix[row].append("P")
                elif relation[row][column] == 1 and relation[column][row] == 1:
                    PIN_matrix[row].append("I")
                elif relation[row][column] == 0 and relation[column][row] == 0:
                    PIN_matrix[row].append("N")
                else:
                    PIN_matrix[row].append(" ")
        return PIN_matrix

    def get_H_matrix(k):
        H_matrix = []
        PIN_matrix = get_PIN_matrix()

        for row in range(len(relation)):
            H_matrix.append([0 for _ in range(len(relation))])
            for column in range(len(relation)):
                if k == 1 and (PIN_matrix[row][column] == "P" or PIN_matrix[row][column] == "I" or PIN_matrix[row][column] == "N"):
                    H_matrix[row][column] = 1
                elif k == 2 and (PIN_matrix[row][column] == "P" or PIN_matrix[row][column] == "N"):
                    H_matrix[row][column] = 1
                elif k == 3 and (PIN_matrix[row][column] == "P" or PIN_matrix[row][column] == "I"):
                    H_matrix[row][column] = 1
                elif k == 4 and (PIN_matrix[row][column] == "P"):
                    H_matrix[row][column] = 1
                else:
                    H_matrix[row][column] = 0
        return H_matrix

    def is_subset_or_equal(list1, list2):
        for i in range(len(list1)):
            if list1[i] == 1 and list2[i] == 0:
                return False
        return True

    def get_max_and_opt(k):
        max_alts = set()
        max_alt_size = 0
        opt_alts = set()

        H_matrix = get_H_matrix(k)

        for vertex in range(len(relation)):

            if H_matrix[vertex].count(1) > 0:
                if len(max_alts) == 0:
                    max_alts.add(vertex)
                    max_alt_size = H_matrix[vertex].count(1)

                elif H_matrix[vertex].count(1) > max_alt_size:
                    max_alts = set([vertex])
                    max_alt_size = H_matrix[vertex].count(1)

                elif H_matrix[vertex].count(1) == max_alt_size:

                    if is_subset_or_equal(H_matrix[vertex],  H_matrix[list(max_alts)[0]]):
                        max_alts.add(vertex)

        if max_alt_size > 0:
            for H_row in H_matrix:
                if not is_subset_or_equal(H_row, H_matrix[list(max_alts)[0]]):
                    max_alts = set()
                    max_alt_size = 0
                    break

        if max_alt_size == len(relation):
            opt_alts = max_alts

        return max_alts, opt_alts

    # print_to_file("PIN matrix:")
    # print_relation(get_PIN_matrix())

    for i in range(1, 5):
        print_to_file(f"k{i}")
        # print_relation(get_H_matrix(i))
        max_alts, opt_alts = get_max_and_opt(i)
        print_to_file(f"k{i} max elements: {max_alts}")
        print_to_file(f"k{i} opt elements: {opt_alts}")
        print_to_file()


def main():
    size = 20
    count = 5

    with open("results.txt", "w") as file:
        file.truncate()

    relations = read_relations(
        "../../practice_3/app/Var-01-АдамовДенис.txt", size, count)

    for (index, relation) in enumerate(relations):

        print_relation(relation, index+1)
        if has_cycle(relation):
            print_to_file(
                f"Relation #{index+1} has a cycle. k-optimization will be used.")
            solve_k_optimization(relation)
        else:
            print_to_file(
                f"Relation #{index+1} is acyclic. Neumann-Morgenstern optimization will be used.")
            solve_NM(relation)


# --------------------------------
main()

from typing import List

a_count = 15
k_count = 12

matrix = [[]]
weights = []

weights_sum = sum(weights)

max_dif = 0  # ???

C = 0
D = 0


def print_array(array):
    print('\n'.join([''.join(['{:3}'.format(item)
          for item in row]) for row in array]))


class Concordance:

    @staticmethod
    def solve():
        concordance = []

        for row in range(a_count):
            concordance.append([])
            for col in range(a_count):
                if row != col:
                    res = Concordance.calc_concordance(row, col)
                else:
                    res = 1
                concordance[row].append(res)
        print('Матриця iндексiв узгодження С')
        print_array(concordance)

        return concordance

    @staticmethod
    def calc_concordance(a: int, b: int):
        numerator = 0
        for col in range(k_count):
            if matrix[a][col] >= matrix[b][col]:
                numerator += weights[col]

        return round(numerator / weights_sum, 3)


class Discordance:
    @staticmethod
    def solve():
        discordance = []

        for row in range(a_count):
            discordance.append([])
            for col in range(a_count):
                if row != col:
                    res = Discordance.calc_discordance(row, col)
                else:
                    res = 0
                discordance[row].append(res)

        print('Матриця iндексiв неузгодження D')
        print_array(discordance)
        return discordance

    @staticmethod
    def calc_discordance(a: int, b: int):
        max_numerator = 0
        max_denumerator = 0
        for col in range(k_count):
            diff = matrix[b][col] - matrix[a][col]
            if matrix[a][col] < matrix[b][col] and max_numerator < diff * weights[col]:
                max_numerator = diff * weights[col]
            if matrix[a][col] < matrix[b][col] and max_denumerator < max_dif[col] * weights[col]:
                max_denumerator = max_dif[col] * weights[col]

        if max_numerator == 0:
            return 0
        else:
            return round(max_numerator / max_denumerator, 3)


class Relation:
    @staticmethod
    def solve():
        relation = []
        matrix_C = Concordance.solve()
        matrix_D = Discordance.solve()

        for row in range(a_count):
            relation.append([])
            for col in range(a_count):
                if row == col:
                    relation[row].append(0)
                elif matrix_C[row][col] >= C and matrix_D[row][col] <= D:
                    relation[row].append(1)
                else:
                    relation[row].append(0)

        print('Порiг:')
        print('c =', C, ' d =', D, '\n')

        print('Вiдношення:')
        for row in relation:
            print(row)

        return relation


size = a_count


class Optimum:
    # dfs
    @staticmethod
    def dfs(used, checked, row, matrix):
        checked.append(row)
        for col in range(size):
            if matrix[row][col] == 0:
                continue
            if matrix[row][col] == 1 and checked.count(col) == 0:
                if Optimum.dfs(used, checked, col, matrix):
                    return True
            else:
                return True
        checked.remove(row)
        used.append(row)
        return False

    @staticmethod
    def check_acyclic(matrix):
        used = []
        for node in range(size):
            if used.count(node) == 0:
                if Optimum.dfs(used, [], node, matrix):
                    return True
        return False

    # Neumann-Morgenstern solution

    # upper contour set for node

    @staticmethod
    def get_upper_contour_set(matrix, node):
        up_set = set()
        for i in range(size):
            if matrix[i][node] == 1:
                up_set.add(i)
        return up_set

    # get S sets

    @staticmethod
    def get_Neumann_Morgenstern_S(matrix: List):
        S = []
        up_sets = []
        for i in range(size):
            s = Optimum.get_upper_contour_set(matrix, i)
            up_sets.append(s)
        S0 = []
        for i in range(size):
            if len(up_sets[i]) == 0:
                S0.append(i)
        S.append(S0)
        while S[-1] != list(range(size)):
            Si = []
            for i in range(size):
                if up_sets[i].issubset(S[-1]):
                    Si.append(i)
            S.append(Si)
        return S

    # get Q sets

    @staticmethod
    def get_Neumann_Morgenstern_Q(matrix: List, S: List):
        Q = [S[0]]
        up_sets = []
        for i in range(size):
            s = Optimum.get_upper_contour_set(matrix, i)
            up_sets.append(s)
        for i in range(1, len(S)):
            Q.append(Q[-1].copy())
            dif = list(set(S[i]) - set(S[i-1]))
            for j in dif:
                if len(set(up_sets[j]).intersection(Q[i-1])) == 0:
                    Q[i].append(j)
        return Q

    @staticmethod
    def check_internal_stability(matrix: List, arr: List):
        for row in arr:
            for col in arr:
                if matrix[row][col] == 1:
                    return False
        return True

    @staticmethod
    def check_external_stability(matrix: List, arr: List):
        for col in range(size):
            if (col in arr):
                continue
            res = False
            for row in arr:
                if matrix[row][col] == 1:
                    res = True
                    break
            if not res:
                return False
        return True

    @staticmethod
    def solve(matrix):
        is_relation_cyclic = Optimum.check_acyclic(matrix)
        if not is_relation_cyclic:
            print("\nВідношення: ациклічне")
            print('Оптимізація за Нейманом-Моргенштерном\n')
            S = Optimum.get_Neumann_Morgenstern_S(matrix)
            Q = Optimum.get_Neumann_Morgenstern_Q(matrix, S)

            int_stab = Optimum.check_internal_stability(matrix, Q[-1])
            ext_stab = Optimum.check_external_stability(matrix, Q[-1])
            print('Внутрішня стійкість: ', int_stab)
            print('Зовнішня стійкість: ', ext_stab)
            print("Розв'язок Неймана-Моргенштерна: ",
                  Q[-1])  # last Q is solution
        else:
            print("\nВідношення: неациклічне")

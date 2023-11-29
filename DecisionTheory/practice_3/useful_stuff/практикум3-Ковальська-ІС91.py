# {k2,k4,k6,k9} < {k7,k8,k11} < {k1,k3,k5,k10,k12}
kvazi_groups = [[1, 3, 5, 8], [6, 7, 10], [0, 2, 4, 9, 11]]

# k9>k11>k4>k1>k5>k6>k12>k3>k2>k8>k10>k7
str_order = [8, 10, 3, 0, 4, 5, 11, 2, 1, 7, 9, 6]

k_count = 12  # кількість критеріїв
a_count = 20  # кількість альтернатив

matrix = [[8, 8, 10, 1, 3, 2, 1, 9, 4, 6, 5, 9],
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
          [10, 10, 6, 9, 7, 10, 8, 10, 8, 7, 10, 9]]


def print_array(array):
    print('\n'.join([''.join(['{:3}'.format(item)
          for item in row]) for row in array]))


def get_delta(x, y):
    result = []
    for i in range(len(x)):
        result.append(x[i] - y[i])
    return result


def get_sigma_table(array):
    sigma_table = []
    for i in range(len(array)):
        sigma_table.append([])
        for j in range(len(array)):
            delta = get_delta(array[i], array[j])
            sigma = get_sigma(delta)
            sigma_table[i].append(sigma)

    print("Вектор різниці оцінок")
    for i in range(len(array)):
        for j in range(len(array)):
            print(f"{sigma_table[i][j]}  ", end='')
        print()

    return sigma_table


def get_sigma(delta):
    result = []
    for i in range(len(delta)):
        if delta[i] > 0:
            result.append(1)
        elif delta[i] < 0:
            result.append(-1)
        else:
            result.append(0)
    return result

    # Pareto


def solve_Pareto(array):
    print("алгоритм Парето")
    sigma_table = get_sigma_table(array)

    R0 = []
    for i in range(a_count):
        R0.append([])
        for j in range(a_count):
            is_added = False
            for index in range(len(sigma_table[i][j])):
                if sigma_table[i][j][index] < 0:
                    R0[i].append(0)
                    is_added = True
                    break
            if not is_added:
                R0[i].append(1)

    print("R0")
    print_array(R0)

    return R0
    # Magoritar


def solve_Magoritar(array):
    print("Мажоритарний алгоритм")
    sigma_table = get_sigma_table(array)

    vector_sum_table = []
    for i in range(a_count):
        vector_sum_table.append([])
        for j in range(a_count):
            vector_sum = 0
            for index in range(len(sigma_table[i][j])):
                vector_sum = vector_sum + sigma_table[i][j][index]
            vector_sum_table[i].append(vector_sum)

    print("Таблиця сум векторів")
    print_array(vector_sum_table)

    RM = []
    for i in range(a_count):
        RM.append([])
        for j in range(a_count):
            if vector_sum_table[i][j] > 0:
                RM[i].append(1)
            else:
                RM[i].append(0)

    print("Rm")
    print_array(RM)

    return RM
    # Lecsicolograph


def solve_Lecsicolograph(array):
    print("Лексографічний алгоритм")
    sigma_table = get_sigma_table(array)
    RL = []
    for i in range(a_count):
        RL.append([])
        for j in range(a_count):
            is_found = False
            check_sigma_vector = sigma_table[i][j]
            for k_index in range(len(str_order)):
                if check_sigma_vector[str_order[k_index]] < 0:
                    is_found = True
                    RL[i].append(0)
                elif check_sigma_vector[str_order[k_index]] > 0:
                    is_found = True
                    RL[i].append(1)
                if is_found:
                    break
            if not is_found:
                RL[i].append(0)

    print("RL")
    print_array(RL)

    return RL

    # Berezovski


def solve_Berezovski(array):
    print("Алгоритм Березовського")

    p_prev = []
    i_prev = []
    n_prev = []

    p = []

    for l in range(len(kvazi_groups)):
        index_array = kvazi_groups[l]
        kvazi_system = []
        for i in range(a_count):
            kvazi_system.append([])
            for j in range(len(index_array)):
                kvazi_system[i].append(array[i][index_array[j]])
        print(f"Ітерація {l+1}")
        print_array(kvazi_system)

        sigma_table = get_sigma_table(kvazi_system)
        i_system = get_i_system(sigma_table)
        print(f"I0{l+1} таблиця")
        print_array(i_system)

        p_system = get_p_system(sigma_table)
        print(f"P0{l+1} таблиця")
        print_array(p_system)

        n_system = get_n_system(sigma_table)
        print(f"N0{l+1} таблиця")
        print_array(n_system)

        if l == 0:
            i_prev = i_system
            n_prev = n_system
            p_prev = p_system
            continue

        p_b = []
        for i in range(a_count):
            p_b.append([])
            for j in range(a_count):
                if p_system[i][j] == 1 and (p_prev[i][j] == 1 or n_prev[i][j] == 1 or i_prev[i][j] == 1):
                    p_b[i].append(1)
                elif i_system[i][j] == 1 and p_prev[i][j] == 1:
                    p_b[i].append(1)
                else:
                    p_b[i].append(0)

        i_b = []
        for i in range(a_count):
            i_b.append([])
            for j in range(a_count):
                if i_system[i][j] == 1 and i_prev[i][j] == 1:
                    i_b[i].append(1)
                else:
                    i_b[i].append(0)

        n_b = []
        for i in range(a_count):
            n_b.append([])
            for j in range(a_count):
                if not (p_b[i][j] == 1 or p_b[j][i] == 1 or i_b[i][j] == 1):
                    n_b[i].append(1)
                else:
                    n_b[i].append(0)

        print(f"RB{l+1}")
        print_array(p_b)

        print(f"NB{l+1}")
        print_array(n_b)

        print(f"IB{l+1}")
        print_array(i_b)

        n_prev = n_b
        i_prev = i_b
        p_prev = p_b

    return p_b


def get_p_system(array):
    result = []
    for i in range(len(array)):
        result.append([])
        for j in range(len(array)):
            sigma = array[i][j]
            is_greater = False
            is_lower = False
            for index in range(len(sigma)):
                if sigma[index] == 1:
                    is_greater = True
                elif sigma[index] == -1:
                    is_lower = True
            if is_greater and not is_lower:
                result[i].append(1)
            else:
                result[i].append(0)
    return result


def get_i_system(array):
    result = []
    for i in range(len(array)):
        result.append([])
        for j in range(len(array)):
            sigma = array[i][j]
            if all(v == 0 for v in sigma):
                result[i].append(1)
            else:
                result[i].append(0)
    return result


def get_n_system(array):
    result = []
    for i in range(len(array)):
        result.append([])
        for j in range(len(array)):
            sigma = array[i][j]
            is_greater = False
            is_lower = False
            for index in range(len(sigma)):
                if sigma[index] == 1:
                    is_greater = True
                elif sigma[index] == -1:
                    is_lower = True
            if is_greater and is_lower:
                result[i].append(1)
            else:
                result[i].append(0)
    return result

    # Podinovski


def solve_Podinovski(array):
    print("Алгоритм Подиновського")
    omega = get_omega(array)
    print("Вектор-функція")
    print_array(omega)

    RP = solve_Pareto(omega)
    return RP


def get_omega(array):
    result = []
    for i in range(a_count):
        result.append(sorted(array[i], reverse=True))
    return result


solve_Pareto(matrix)
# solve_Magoritar(matrix)
# solve_Lecsicolograph(matrix)
# solve_Berezovski(matrix)
# solve_Podinovski(matrix)

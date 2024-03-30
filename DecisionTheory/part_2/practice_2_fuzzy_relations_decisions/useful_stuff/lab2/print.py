def print_matrix(matrix):
    for row in matrix:
        print(" ", end="")
        for val in row:
            print("{:.2f}".format(val), end=" ")
        print("")


def print_set(matrix):
    print(" ", end="")
    for val in matrix:
        print("{:.2f}".format(val), end=" ")
    print("")


def print_rank(matrix):
    print(" ", end="")
    for val in matrix:
        print("{:1d}".format(val[0]), end=" ")
    print("")
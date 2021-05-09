import numpy as np

def chained_hash_func_div(key, m):
    return key % m


def chained_hash_insert_div(table, key):        # additionally returns number if there is a collision
    collisions = 0;
    table[chained_hash_func_div(key, len(table))].append(key)
    if len(table[chained_hash_func_div(key, len(table))]) > 1:
        collisions += 1
    return collisions

def chained_hash_search_div(table, key):
    if key in table[chained_hash_func_div(key, len(table))]:
        return True
    return False


def chained_hash_func_mult(key, m): 
    return int(np.floor((key*((np.sqrt(5)-1)/2)%1)*m))

def chained_hash_insert_mult(table, key):       # additionally returns number if there is a collision
    collisions = 0;
    table[chained_hash_func_mult(key, len(table))].append(key)
    if len(table[chained_hash_func_mult(key, len(table))]) > 1:
        collisions += 1
    return collisions

def chained_hash_search_mult(table, key):
    if key in table[chained_hash_func_mult(key, len(table))]:
        return True
    return False


def read_data(filename):
    with open(filename, "r") as file:
        first_line = list(map(int, file.readline().split()))
        A = [0]*first_line[0]
        sums = [0]*first_line[1]
        for i in range(len(A)):
            A[i] = int(file.readline())
        for i in range(len(sums)):
            sums[i] = int(file.readline())
    return A, sums

def write_line(filename, line):
    file = open(filename, "a")
    file.writelines([line, '\n']) # []?
    file.close()

def sum_search_div(table, sums, file):
    for sum in sums:
        found = False
        for cell in table:
            if found:
                break
            else:
                for x in cell:
                    y = sum - x
                    if chained_hash_search_div(table, y):
                        write_line(file, str(x) + ' ' + str(y))
                        found = True
                        break
        if not found:
            write_line(file, "0 0")

def sum_search_mult(table, sums, file):
    for sum in sums:
        found = False
        for cell in table:
            if found:
                break
            else:
                for x in cell:
                    y = sum - x
                    if chained_hash_search_mult(table, y):
                        write_line(file, str(x) + ' ' + str(y))
                        found = True
                        break
        if not found:
            write_line(file, "0 0")
import random

def generate_data(n_digits):
    cardinality = 10**(n_digits)
    array = [i for i in range(cardinality)] + [i for i in range(0, cardinality, 2)]
    random.shuffle(array)
    return array

def get_digit(number, n_digit):
    return number // 10**n_digit % 10

def radix_sort(array, n_digits):
    array_output = array[:]
    for i in range(n_digits):
        C = [0]*10
        for j in range(len(array)):
            C[get_digit(array[j], i)] += 1
        for j in range(1, 10):
            C[j] += C[j-1]
        for j in range(len(array) - 1, -1, -1):
            C[get_digit(array[j], i)] -= 1
            array_output[C[get_digit(array[j], i)]] = array[j]
        array = array_output[:]
    return array_output

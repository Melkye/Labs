import random

def generate_data(n, gen_type ="random"):
    if gen_type=="best":
        array = [i+1 for i in range(n)]
        return array
    elif gen_type=="worst":
        array = [i+1 for i in reversed(range(n))]
        return array
    else:
        array = [i+1 for i in range(n)]
        random.shuffle(array)
        return array

def bubble_sort(array):
    comparisons = 0
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            comparisons += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return comparisons

def improved_bubble_sort(array):
    comparisons = 0
    changed = True
    end = len(array) - 1
    while changed:
        changed = False
        for j in range(end):
            comparisons += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                changed = True
        end-=1
    return comparisons

def insertion_sort(array):
    comparisons = 0
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        comparisons += 1
        while key < array[j] and j >= 0:
            comparisons += 1
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
    return comparisons
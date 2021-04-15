import math

def quicksort(array, start, end):
    counter = 0
    if start < end:
        border, add_counter = partition(array, start, end)
        counter += add_counter
        counter += quicksort(array, start, border - 1)
        counter += quicksort(array, border + 1, end)
    return counter

def partition(array, start, end):
    pivot = array[end]
    i = start - 1
    counter = 0
    for j in range(start, end):
        counter+=1
        if array[j] <= pivot:
            i+=1
            array[i], array[j] = array[j], array[i]
    array[end], array[i+1] = array[i+1], array[end]
    return i + 1, counter

def mid_3_quicksort(array, start, end):
    counter = 0
    if start < end:
        border, add_counter = mid_3_partition(array, start, end)
        counter += add_counter
        counter += mid_3_quicksort(array, start, border - 1)
        counter += mid_3_quicksort(array, border + 1, end)
    return counter

def mid_3_partition(array, start, end):
    median = math.floor((start+end)/2)
    pivot_index = order_indexes_by_values(array, start, median, end)[1]
    array[pivot_index], array[end] = array[end], array[pivot_index]

    return partition(array, start, end)

def order_indexes_by_values(array, first, second, third):
    if array[first] <= array[second]:
        if array[second] <= array[third]:
            return [first, second, third]
        elif array[first] <= array[third]:
            return [first, third, second]
        else:
            return [third, first, second]
    else:
        if array[first] <= array[third]:
            return [second, first, third]
        elif array[second] <= array[third]:
            return [second, third, first]
        else:
            return [third, second, first]

def quicksort3(array, start, end):
    counter = 0
    if start < end:
        pivots_indexes = order_indexes_by_values(array, start, start+1, end)
        pivots = [array[pivots_indexes[0]], array[pivots_indexes[1]], array[pivots_indexes[2]]]
        array[start], array[start+1], array[end] = pivots[0], pivots[1], pivots[2]
    
        p, q, r, add_counter = partition3(array, start, end)
        counter+= add_counter
        counter+= quicksort3(array, start, p - 1)
        counter+= quicksort3(array, p + 1 , q - 1)
        counter+= quicksort3(array, q + 1, r - 1)
        counter+= quicksort3(array, r + 1, end)

    return counter

def partition3(array, start, end):
    a = start + 2
    b = start + 2
    c = end - 1
    d = end - 1
    p = array[start]
    q = array[start + 1]
    r = array[end]

    counter = 0
    while b <= c:
        counter+=1
        while array[b] < q and b <= c:
            counter+=2
            if array[b] < p:
                array[a], array[b] = array[b], array[a]
                a+=1
            b+=1
        counter+=1
        while array[c] > q and b <= c:
            counter+=2
            if array[c] > r:
                array[c], array[d] = array[d], array[c]
                d-=1
            c-=1
        if b <= c:
            counter+=1
            if array[b] > r:
                counter+=1
                if array[c] < p:
                    array[b], array[a] = array[a], array[b]
                    array[a], array[c] = array[c], array[a]
                else:
                    array[b], array[c] = array[c], array[b]
                array[c], array[d] = array[d], array[c]
                b+=1
                c-=1
                d-=1
            else:
                counter+=1
                if array[c] < p:
                    array[b], array[a] = array[a], array[b]
                    array[a], array[c] = array[c], array[a]
                    a+=1
                else:
                    array[b], array[c] = array[c], array[b]
                b+=1
                c-=1
    a-=1
    b-=1
    c+=1
    d+=1
    array[start + 1], array[a] = array[a], array[start + 1]
    array[a], array[b] = array[b], array[a]
    a-=1
    array[start], array[a] = array[a], array[start]
    array[end], array[d] = array[d], array[end]
    return a, b, d, counter                             # returns indexes of pivots & number of comparisons

def read_data(filename):
    data = []
    row = 0
    with open(filename, "r") as file:
        size = int(file.readline())
        while row < size:
            data.append(file.readline())
            row+=1
    data = list(map(int, data))
    return data

def write_data(filename, result1, result2, result3):
    output_file = open(filename, "w")
    output_file.writelines([str(result1), ' ', str(result2), ' ', str(result3)])
    output_file.close()
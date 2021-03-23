import math

def merge_sort(array, left_bound, right_bound):
    if left_bound < right_bound:
        middle_bound = math.floor((left_bound + right_bound)/2)
        merge_sort(array, left_bound, middle_bound)
        merge_sort(array, middle_bound + 1, right_bound)
        merge(array, left_bound, middle_bound, right_bound)

def merge(array, left_bound, middle_bound, right_bound):
    temp_left = []
    temp_right = []
    temp_left.append(list(array[0][left_bound : middle_bound + 1]))
    temp_left.append(list(array[1][left_bound : middle_bound + 1]))
    temp_right.append(list(array[0][middle_bound + 1 : right_bound + 1]))
    temp_right.append(list(array[1][middle_bound + 1 : right_bound + 1]))

    i = 0
    j = 0
    for k in range(left_bound, right_bound):
        if (temp_left[1][i] <= temp_right[1][j]):
            array[0][k] = temp_left[0][i]
            array[1][k] = temp_left[1][i]
            i+=1
            if (i == len(temp_left[0])):
                array[0][k + 1 : right_bound + 1] = temp_right[0][j:]
                array[1][k + 1 : right_bound + 1] = temp_right[1][j:]
                break
        else:
            array[0][k] = temp_right[0][j]
            array[1][k] = temp_right[1][j]
            j+=1
            if (j == len(temp_right[0])):
                array[0][k + 1 : right_bound + 1] = temp_left[0][i:]
                array[1][k + 1 : right_bound + 1] = temp_left[1][i:]
                break



def count_inv(array, left_bound, right_bound):
    inversions = 0
    if left_bound < right_bound:
        middle_bound = math.floor((left_bound + right_bound)/2)
        inversions += count_inv(array, left_bound, middle_bound)
        inversions += count_inv(array, middle_bound + 1, right_bound)
        inversions += count_split_inv(array, left_bound, middle_bound, right_bound)
    return inversions


def count_split_inv(array, left_bound, middle_bound, right_bound):
    temp_left = array[left_bound : middle_bound + 1]
    temp_right = array[middle_bound + 1 : right_bound + 1]

    i = 0
    j = 0
    split_inversions = 0
    for k in range(left_bound, right_bound):
        if (temp_left[i] <= temp_right[j]):
            array[k] = temp_left[i]
            i+=1
            if (i == len(temp_left)):
                array[k + 1 : right_bound + 1] = temp_right[j:]
                break
        else:
            array[k] = temp_right[j]
            split_inversions += len(temp_left) - i
            j+=1
            if (j == len(temp_right)):
                array[k + 1 : right_bound + 1] = temp_left[i:]
                break
    return split_inversions


def read_first_row(filename):
    data = []
    with open(filename, "r") as file_object:
         data = file_object.readline().split(' ')
         data = list(map(int, data))
    return data

def read_comp_row(filename, user_index):
    user_data = []
    row = 0
    with open(filename, "r") as file_object:
         while (row != user_index):
             file_object.readline()
             row+=1
         user_data = file_object.readline().split(' ')
         user_data = list(map(int, user_data))
         user_data = user_data[1:]
    return user_data

def read_row(filename, user_index, order_user_data):
    user_data = []
    row = 0
    with open(filename, "r") as file_object:
         while (row != user_index):
             file_object.readline()
             row+=1
         user_data = file_object.readline().split(' ')
         user_data = list(map(int, user_data))
         user_data = user_data[1:]
    temp_data = user_data[:]
    for i in range(len(user_data)):
        user_data[order_user_data[i]-1] = temp_data[i]
    return user_data

def write_results(filename, user_index, inversions_array):
    output_file = open(filename, "w");
    output_file.writelines([str(user_index), '\n'])
    for i in range(0, len(inversions_array[0])):
        output_file.writelines([str(inversions_array[0][i]), ' ',
                                str(inversions_array[1][i]), '\n'])
    output_file.close()
import fun

filename = "mydata.txt"
compared_user_index = int(input("Enter the number of the user to check: "))
compared_user_data = fun.read_comp_row(filename, compared_user_index)
number_of_users = fun.read_first_row(filename)[0]
number_of_movies = fun.read_first_row(filename)[1]

inversions_data = [[], []]
for i in range(1, number_of_users + 1):
    if i != compared_user_index:
        user_data = fun.read_row(filename, i, compared_user_data)
        inversions_data[0].append(i)
        inversions_data[1].append(fun.count_inv(user_data, 0, number_of_movies - 1))

fun.merge_sort(inversions_data, 0, (number_of_users-1) -1) #not including the compared one
fun.write_results("output.txt", compared_user_index, inversions_data)
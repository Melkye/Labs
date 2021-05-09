import hashing

input_files = ["input_data\\input_10.txt",
               "input_data\\input_1000.txt",
               "input_data\\input_100000.txt"]

output_files_1 = ["my_output_data\\my_output_10_1.txt",
                  "my_output_data\\my_output_1000_1.txt",
                  "my_output_data\\my_output_100000_1.txt"]

output_files_2 = ["my_output_data\\my_output_10_2.txt",
                  "my_output_data\\my_output_1000_2.txt",
                  "my_output_data\\my_output_100000_2.txt"]



for r_file, w_file_1, w_file_2 in zip(input_files, output_files_1, output_files_2):
    A, sums = hashing.read_data(r_file)

    m1 = len(A)*3
    m2 = len(A)*3

    T1 = [[] for i in range(m1)]
    T2 = [[] for i in range(m2)]

    coll1 = 0
    coll2 = 0

    for key in A:
        coll1 += hashing.chained_hash_insert_div(T1, key)
        coll2 += hashing.chained_hash_insert_mult(T2, key)

    with open(w_file_1, "w"):
        pass
    with open(w_file_2, "w"):
        pass

    hashing.write_line(w_file_1, str(coll1))
    hashing.write_line(w_file_2, str(coll2))

    hashing.sum_search_div(T1, sums, w_file_1)
    hashing.sum_search_mult(T2, sums, w_file_2)


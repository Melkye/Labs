import trees

search_sums = [9, 7, 9, 51, 78, 103, 501, 1025, 513]

input_filenames = ["input_data//input_10a.txt", "input_data//input_10b.txt", "input_data//input_10c.txt",
                   "input_data//input_100a.txt", "input_data//input_100b.txt", "input_data//input_100c.txt",
                   "input_data//input_1000a.txt", "input_data//input_1000b.txt", "input_data//input_1000c.txt"]

output_filenames = ["my_output_data//my_output_10a_9.txt", "my_output_data//my_output_10b_7.txt", "my_output_data//my_output_10c_9.txt",
                    "my_output_data//my_output_100a_51.txt", "my_output_data//my_output_100b_78.txt", "my_output_data//my_output_100c_103.txt",
                    "my_output_data//my_output_1000a_501.txt", "my_output_data//my_output_1000b_1025.txt", "my_output_data//my_output_1000c_513.txt"]

for r_filename, w_filename, sum in zip(input_filenames, output_filenames, search_sums):
    tree_data = trees.read_tree_data(r_filename)
    tree = trees.BinarySearchTree(tree_data)

    array = tree.get_array_in_order_walk(tree.root)
    array.sort();
    tree.change_values_in_order_walk(tree.root, array)

    sums_list = trees.get_tree_sums_list(tree.root, sum)
    trees.write_sums_data(sums_list, w_filename)
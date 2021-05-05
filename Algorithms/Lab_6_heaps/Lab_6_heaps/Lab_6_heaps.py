import heap

input_filenames = \
    [f"input_data\\input_0{i}_10.txt" for i in range(1, 6)] + \
    [f"input_data\\input_0{i}_100.txt" for i in range(6, 10)] + \
    [f"input_data\\input_10_100.txt"] + \
    [f"input_data\\input_{i}_1000.txt" for i in range(11, 16)] + \
    [f"input_data\\input_{i}_10000.txt" for i in range(16, 21)]

output_filenames = \
    [f"my_output_data\\my_output_0{i}_10.txt" for i in range(1, 6)] + \
    [f"my_output_data\\my_output_0{i}_100.txt" for i in range(6, 10)] + \
    [f"my_output_data\\my_output_10_100.txt"] + \
    [f"my_output_data\\my_output_{i}_1000.txt" for i in range(11, 16)] + \
    [f"my_output_data\\my_output_{i}_10000.txt" for i in range(16, 21)]

max1 = heap.MaxHeap()
min1 = heap.MinHeap()


for r_filename, w_filename in zip(input_filenames, output_filenames):
    data = heap.read_data(r_filename)
    max1.clear()
    min1.clear()
    with open(w_filename, "w"):
        pass
    for element in data:
        m = heap.get_median(max1, min1, element)
        heap.write_data(w_filename, m)
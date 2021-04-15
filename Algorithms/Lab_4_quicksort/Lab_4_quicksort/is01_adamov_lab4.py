import quick

input_files = ["input_data\\input_01_10.txt",
               "input_data\\input_02_10.txt",
               "input_data\\input_03_10.txt",
               "input_data\\input_04_10.txt",
               "input_data\\input_05_10.txt",
               "input_data\\input_06_100.txt",
               "input_data\\input_07_100.txt",
               "input_data\\input_08_100.txt",
               "input_data\\input_09_100.txt",
               "input_data\\input_10_100.txt",
               "input_data\\input_11_1000.txt",
               "input_data\\input_12_1000.txt",
               "input_data\\input_13_1000.txt",
               "input_data\\input_14_1000.txt",
               "input_data\\input_15_1000.txt",
               "input_data\\input_16_10000.txt",
               "input_data\\input_17_10000.txt",
               "input_data\\input_18_10000.txt",
               "input_data\\input_19_10000.txt",
               "input_data\\input_20_10000.txt",]

output_files = ["my_output_data\\is01_adamov_output_01_10.txt",
                "my_output_data\\is01_adamov_output_02_10.txt",
                "my_output_data\\is01_adamov_output_03_10.txt",
                "my_output_data\\is01_adamov_output_04_10.txt",
                "my_output_data\\is01_adamov_output_05_10.txt",
                "my_output_data\\is01_adamov_output_06_100.txt",
                "my_output_data\\is01_adamov_output_07_100.txt",
                "my_output_data\\is01_adamov_output_08_100.txt",
                "my_output_data\\is01_adamov_output_09_100.txt",
                "my_output_data\\is01_adamov_output_10_100.txt",
                "my_output_data\\is01_adamov_output_11_1000.txt",
                "my_output_data\\is01_adamov_output_12_1000.txt",
                "my_output_data\\is01_adamov_output_13_1000.txt",
                "my_output_data\\is01_adamov_output_14_1000.txt",
                "my_output_data\\is01_adamov_output_15_1000.txt",
                "my_output_data\\is01_adamov_output_16_10000.txt",
                "my_output_data\\is01_adamov_output_17_10000.txt",
                "my_output_data\\is01_adamov_output_18_10000.txt",
                "my_output_data\\is01_adamov_output_19_10000.txt",
                "my_output_data\\is01_adamov_output_20_10000.txt",]

a1 = quick.read_data("input_data\\input_worst_worst_case.txt")
a2 = a1[:]
a3 = a1[:]

counter1 = quick.quicksort(a1, 0, len(a1)-1)
counter2 = quick.mid_3_quicksort(a2, 0, len(a2)-1)
counter3 = quick.quicksort3(a3, 0, len(a3)-1)

quick.write_data("output_data\\output_worst_worst_case.txt", counter1, counter2, counter3)

#for input_file, output_file in zip(input_files, output_files):
#    a1 = quick.read_data(input_file)
#    a2 = a1[:]
#    a3 = a1[:]

#    counter1 = quick.quicksort(a1, 0, len(a1)-1)
#    counter2 = quick.mid_3_quicksort(a2, 0, len(a2)-1)
#    counter3 = quick.quicksort3(a3, 0, len(a3)-1)

#    quick.write_data(output_file, counter1, counter2, counter3)

#my_big_output_file = open("my_output_data\\is01_adamov_big_output.txt", "w")
#for i in range(len(input_files)):
#    a1 = quick.read_data(input_files[i])
#    a2 = a1[:]
#    a3 = a1[:]

#    counter1 = quick.quicksort(a1, 0, len(a1)-1)
#    counter2 = quick.mid_3_quicksort(a2, 0, len(a2)-1)
#    counter3 = quick.quicksort3(a3, 0, len(a3)-1)

#    my_big_output_file.writelines([str(i+1), '. ', str(counter1), ' ', str(counter2), ' ', str(counter3), '\n'])
#my_big_output_file.close()

#standard_big_output_file = open("output_data\\standard_big_output.txt", "w")
#for i in range(1, 21):
#    if i <= 5:
#        small_output_filename = "output_data\\output_0" + str(i) + "_10.txt"
#    elif i <= 9:
#        small_output_filename = "output_data\\output_0" + str(i) + "_100.txt"
#    elif i == 10:
#        small_output_filename = "output_data\\output_10_100.txt"
#    elif i <= 15:
#        small_output_filename = "output_data\\output_" + str(i) + "_1000.txt"
#    elif i <= 20:
#        small_output_filename = "output_data\\output_" + str(i) + "_10000.txt"
#    small_output_file = open(small_output_filename, "r")

#    standard_big_output_file.writelines([str(i), '. ', small_output_file.readline(), '\n'])
#    small_output_file.close()
#standard_big_output_file.close()
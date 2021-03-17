import numpy as np
import plot_data
import sorting

sizes = [10, 100, 1000]
types = ["random", "best", "worst"]
data_plot = {'random': {'bubble':{}, 'insertion':{}, 'bubble_impr':{}}, 
             'best': {'bubble':{}, 'insertion':{}, 'bubble_impr':{}},
             'worst': {'bubble':{}, 'insertion':{}, 'bubble_impr':{}}}

for n in sizes:
    print("\nDATA SIZE: ", n)
    for gen_type in types:
        print("\n\tDATA TYPE:", gen_type)

        data = sorting.generate_data(n, gen_type)

        data_bubble = np.copy(data)
        bubble_comparisons = sorting.bubble_sort(data_bubble)
        print("\tBubble sort operation count:", int(bubble_comparisons))
        data_plot[gen_type]['bubble'][n] = bubble_comparisons

        data_bubble_impr = np.copy(data)
        bubble_impr_comparisons = sorting.improved_bubble_sort(data_bubble_impr)
        print("\tImproved bubble sort operation count:", int(bubble_impr_comparisons))
        data_plot[gen_type]['bubble_impr'][n] = bubble_impr_comparisons

        data_insertion = np.copy(data)
        insertion_comparisons = sorting.insertion_sort(data_insertion)
        print("\tInsertion sort operation count:", int(insertion_comparisons))
        data_plot[gen_type]['insertion'][n] = insertion_comparisons

plot_data.plot_data(data_plot, logarithmic=True, oneplot=True)


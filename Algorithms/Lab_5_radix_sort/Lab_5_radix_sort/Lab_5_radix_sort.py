import sorting

d = int(input("Set the number of digits: "))
A = sorting.generate_data(d) #[559, 645, 330, 214, 777, 900, 622] 
B = sorting.radix_sort(A, d)
print(B)
a = 0

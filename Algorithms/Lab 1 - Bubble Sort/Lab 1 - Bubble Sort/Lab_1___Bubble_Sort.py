import random

def list_generator(n):
    array = [ i+1 for i in range(n)]
   # for i in range(n):
    #    array.append(random.randrange(1, 99))
    return array

def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def modified_bubble_sort(array):    # even asc in the left, odd desc in the right
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if (array[j]%2 == 1 and array[j+1]%2 == 0) \
            or (array[j]%2 == 1 and array[j+1]%2 == 1 and array[j] < array[j+1]) \
            or (array[j]%2 == 0 and array[j+1]%2 == 0 and array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]

def improved_bubble_sort(array):
    changed = True
    end = len(array) - 1
    while changed:
        changed = False
        for j in range(end):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                changed = True
        end-=1

array_size = 10
x = list_generator(array_size)
y = x[:]
z = x[:]
print("Generated array:")
print(x, "\n")

print("Sorted array:")
bubble_sort(x)
print(x, "\n")

print("Modified sort:")
modified_bubble_sort(y)
print(y, "\n")

print("Improved sort:")
improved_bubble_sort(z)
print(z, "\n")
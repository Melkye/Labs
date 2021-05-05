import numpy as np

class MaxHeap:
    """ Implements a binary MaxHeap, elements is a list of values """

    def __init__(self):
        self.elements = []

    def size(self):
        return len(self.elements)

    def max_heapify(self, x):
        left = 2*x + 1
        right = 2*x + 2
        if left < self.size() and self.elements[left] > self.elements[x]:
            largest = left
        else:
            largest = x
        if right < self.size() and self.elements[right] > self.elements[largest]:
            largest = right
        if largest != x:
            self.elements[x], self.elements[largest] = self.elements[largest], self.elements[x]
            self.max_heapify(largest)
    
    def max(self):
        return self.elements[0]

    def extract_max(self):
        max = self.elements[0]
        self.elements[0] = self.elements[self.size() - 1]
        self.elements.pop()
        self.max_heapify(0)
        return max

    def change_value(self, x, value):
        self.elements[x] = value
        parent = (x-1)//2
        while x > 0 and self.elements[parent] < self.elements[x]:
            self.elements[parent], self.elements[x] = self.elements[x], self.elements[parent]
            x = parent
            parent = (x-1)//2

    def insert(self, value):
        self.elements.append(-np.inf)
        self.change_value(self.size() - 1, value)

    def clear(self):
        self.elements = []

class MinHeap:
    """ Implements a binary MinHeap, elements is a list of values """

    def __init__(self):
        self.elements = []

    def size(self):
        return len(self.elements)

    def min_heapify(self, x):
        left = 2*x + 1
        right = 2*x + 2
        if left < self.size() and self.elements[left] < self.elements[x]:
            smallest = left
        else:
            smallest = x
        if right < self.size() and self.elements[right] < self.elements[smallest]:
            smallest = right
        if smallest != x:
            self.elements[x], self.elements[smallest] = self.elements[smallest], self.elements[x]
            self.min_heapify(smallest)

    def min(self):
        return self.elements[0]

    def extract_min(self):
        min = self.elements[0]
        self.elements[0] = self.elements[self.size() - 1]
        self.elements.pop()
        self.min_heapify(0)
        return min
    
    def change_value(self, x, value):
        self.elements[x] = value
        parent = (x-1)//2
        while x > 0 and self.elements[parent] > self.elements[x]:
            self.elements[parent], self.elements[x] = self.elements[x], self.elements[parent]
            x = parent
            parent = (x-1)//2

    def insert(self, value):
        self.elements.append(-np.inf)
        self.change_value(self.size() - 1, value)

    def clear(self):
        self.elements = []

def get_median(h_low, h_high, value):
    if  h_low.size() == 0 or value <= h_low.max():
        h_low.insert(value)
    else:
        h_high.insert(value)

    if h_low.size() > h_high.size() + 1:
        h_high.insert(h_low.extract_max())
    elif h_high.size() > h_low.size() + 1:
        h_low.insert(h_high.extract_min())

    if (h_low.size() + h_high.size()) % 2 == 0:
        return [h_low.max(), h_high.min()]
    elif h_low.size() > h_high.size():
        return [h_low.max()]
    else:
        return [h_high.min()]

def read_data(filename):
    data = []
    row = 0
    with open(filename, "r") as file:
        size = int(file.readline())
        while row < size:
            data.append(file.readline())
            row += 1
        data = list(map(int, data))
    return data

def write_data(filename, line):
    file = open(filename, "a")
    file.writelines([' '.join(map(str, line)), "\n"])
    file.close()

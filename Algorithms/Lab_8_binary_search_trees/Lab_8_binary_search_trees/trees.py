class Node:
    """ Implements a binary search tree node """
    def __init__(self, value, parent = None, left = None, right = None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

class BinarySearchTree:
    """ Implements a binary search tree """
    def __init__(self, array):
        """Creates a bst using pre-order walk"""
        self.root = Node(array[0])
        curr_parent = self.root
        is_left = True
        for value in array[1:]:
           if value == 0:
               if is_left:
                   is_left = False
               else:
                   while curr_parent.parent != None and curr_parent.parent.right == curr_parent:
                       curr_parent = curr_parent.parent
                   curr_parent = curr_parent.parent
           else:
               if is_left:
                   curr_parent.left = Node(value, curr_parent)
                   curr_parent = curr_parent.left
               else:
                   curr_parent.right = Node(value, curr_parent)
                   curr_parent = curr_parent.right
                   is_left = True
                   
    #def get_array_pre_order_walk(self, node):
    #    array = []
    #    if node != None:
    #        array.append(node.value)
    #        array += self.get_array_pre_order_walk(node.left)
    #        array += self.get_array_pre_order_walk(node.right)
    #    return array

    def get_array_in_order_walk(self, node):
        array = []
        if node != None:
            array += self.get_array_in_order_walk(node.left)
            array.append(node.value)
            array += self.get_array_in_order_walk(node.right)
        return array

    def change_values_in_order_walk(self, node, array):
        if node != None:
            self.change_values_in_order_walk(node.left, array)
            node.value = array.pop(0)
            self.change_values_in_order_walk(node.right, array)

def get_tree_chains(node, chains_list):
    """ Fills passed chains_list with all possible chains(paths) from top to bottom"""
    if node != None:
        start_chain = [node.value]
        if not start_chain in chains_list:
            chains_list.append(start_chain)
        get_tree_chains_internal(node.left, start_chain, chains_list)
        get_tree_chains_internal(node.right, start_chain, chains_list)

def get_tree_chains_internal(node, prev_chain, chains_list):
    if node != None:
        curr_chain = prev_chain + [node.value]
        if not curr_chain in chains_list:
            chains_list.append(curr_chain)
        get_tree_chains(node, chains_list)
        get_tree_chains_internal(node.left, curr_chain, chains_list)
        get_tree_chains_internal(node.right, curr_chain, chains_list)

def find_sum(array):
    sum = 0
    for value in array:
        sum += value
    return sum

def get_tree_sums_list(node, sum_number):
    """ Returns a list containing all possible chains(paths) from top to bottom, if the chain's sum equals sum_number"""
    chains_list = []
    sums_list = []
    get_tree_chains(node, chains_list)
    for chain in chains_list:
        temp_sum = find_sum(chain)
        if sum_number == temp_sum:
            sums_list.append(chain)
    return sums_list

def read_tree_data(filename):
    with open(filename, "r") as file:
        line = file.readline()
        data = list(map(int, line.split(' ')))
    return data

def write_sums_data(sums_list, filename):
    with open(filename, "w") as file:
        for sum_chain in sums_list:
            file.writelines([' '.join(map(str, sum_chain)), "\n"])

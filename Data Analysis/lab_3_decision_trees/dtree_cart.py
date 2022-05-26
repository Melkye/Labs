# %%
import numpy as np
import pandas as pd

# %%
class Node():
    def __init__(self, attribute_index = None, condition_value = None, left = None, right = None, value = None, number_of_elements = None):

        self.attribute_index = attribute_index
        self.condition_value = condition_value
        self.left = left
        self.right = right

        self.value = value

        self.number_of_elements = number_of_elements
        self.traversed_for_prunning = False

# %%
class DecisionTreeCART():
    def __init__(self, data, data_labels, max_depth, min_leaf_objects):
        
        self.max_depth = max_depth
        self.min_leaf_objects = min_leaf_objects
        self.attribute_labels =  data_labels

        data = np.array(data)
        
        self.root = self.build(data, curr_depth = 0)

    def build(self, data, curr_depth):

        attributes_values = data[:,:-1]
        class_values = data[:,-1].reshape(-1, 1)
        
        objects_count, attribute_count = np.shape(attributes_values)

        if objects_count > self.min_leaf_objects and curr_depth < self.max_depth:
            best_split = self.get_best_split(data)
            left_subtree = self.build(best_split["data_left"], curr_depth+1)
            right_subtree = self.build(best_split["data_right"], curr_depth+1)
            return Node(best_split["attribute_index"], best_split["condition_value"], 
                left_subtree, right_subtree, number_of_elements = objects_count)
        
        value = self.get_leaf_value(class_values)
        return Node(value = value, number_of_elements = objects_count)
    
    def get_best_split(self, data):
        attributes_values = data[:,:-1]
        objects_count, attribute_count = np.shape(attributes_values)
        best_split = {}
        min_gini_index = np.inf

        for attribute_index in range(attribute_count):
            attribute_values = data[:, attribute_index]
            unique_attribute_values =  np.unique(attribute_values)
            for value in unique_attribute_values:
                data_left, data_right = self.split(data, attribute_index, value)
                if len(data_left) != 0 and len(data_right) != 0:
                    class_values = data[:,-1]
                    class_values_left = data_left[:,-1]
                    class_values_right = data_right[:,-1]
                    gini_index = self.get_gini_split(class_values, class_values_left, class_values_right)
                    if gini_index < min_gini_index:
                        min_gini_index = gini_index
                        best_split["attribute_index"] = attribute_index
                        best_split["condition_value"] = value
                        best_split["data_left"] = data_left
                        best_split["data_right"] = data_right
                        #best_split["gini_index"] = gini_index
        return best_split

    def split(self, data, attribute_index, condition_value):
        data_left = np.array([record for record in data \
            if record[attribute_index] <= condition_value])
        data_right = np.array([record for record in data \
            if record[attribute_index] > condition_value])
        return data_left, data_right
    
    def get_gini_split(self, parent, left, right):
        def get_gini(class_values):
            classes = np.unique(class_values)
            sum_of_p_squared = 0
            for category in classes:
                category_count = 0
                for value in class_values:
                    if value == category:
                        category_count += 1
                probability = category_count/len(class_values)
                sum_of_p_squared += probability**2
            gini = 1 - sum_of_p_squared
            return gini

        weight_left = len(left)/len(parent)
        weight_right = len(right)/len(parent)
        gini_split = weight_left*get_gini(left) + weight_right*get_gini(right)
        return gini_split

    def get_leaf_value(self, class_values):
        class_values = class_values.reshape(1, -1)[0]
        class_values_count = {}
        for class_value in class_values:
            if class_value not in class_values_count:
                class_values_count[class_value] = 1
            else:
                class_values_count[class_value] += 1
        return max(class_values_count) 

    def predict(self, data_attributes):

        def predict_one(sample_attributes, node=self.root):
            if node.value is None:
                attribute_value = sample_attributes[node.attribute_index]
                if attribute_value <= node.condition_value:
                    return predict_one(sample_attributes, node.left)
                else:
                    return predict_one(sample_attributes, node.right)
            else:
                return node.value

        return [predict_one(record_attributes) for record_attributes in data_attributes]

    def clean_one_layer(self, node=None):
        if node is None:
            node = self.root
        if node.left is not None \
        and node.right is not None:
            if node.left.value is not None \
            and node.right.value is not None \
            and node.left.value == node.right.value:
                node.value = node.left.value
                node.condition_value = None
                node.attribute_index = None
                node.left = None
                node.right = None
            else:
                self.clean_one_layer(node.left)
                self.clean_one_layer(node.right)
    
    def clean(self):
        for i in range(self.max_depth):
            self.clean_one_layer()

    def prune_one_layer(self, current_layer, prunning_goal_layer, node=None):
        if node is None:
                node = self.root
        if prunning_goal_layer < self.max_depth \
        and node.left is not None \
        and node.right is not None:
            if (node.left.value is not None or node.left.traversed_for_prunning == True) \
            and (node.right.value is not None or node.right.traversed_for_prunning == True):
            #if (node.left.value is not None and node.right.value is not None) or \
            # (node.left.traversed_for_prunning == True and node.right.traversed_for_prunning == True):
                if current_layer >= prunning_goal_layer:
                    if node.left.number_of_elements > node.right.number_of_elements:
                        node.value = node.left.value
                    else:
                        node.value = node.right.value
                    node.number_of_elements = node.left.number_of_elements + node.right.number_of_elements
                    node.condition_value = None
                    node.attribute_index = None
                    node.left = None
                    node.right = None
                else: #вийти
                    node.traversed_for_prunning = True
            else:
                self.prune_one_layer(current_layer+1, prunning_goal_layer, node.left)
                self.prune_one_layer(current_layer+1, prunning_goal_layer, node.right)
                self.prune_one_layer(current_layer, prunning_goal_layer, node)
            
    def prune(self, prunning_goal_layer):
        
            self.prune_one_layer(0, prunning_goal_layer) #or 1?
            self.clean()
        
    def print(self, node=None, depth = 1):
        indent = "-"
        if node is None:
            node = self.root

        if node.value is not None:
            if node.value == 1:
                print("[Class 1 - Potable]")
            else:
                print("[Class 0 - Unpotable]")
        else:
            from colorama import Fore
            colors = [Fore.WHITE, Fore.BLUE, Fore.GREEN, Fore.CYAN, Fore.RED, 
                Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.LIGHTBLUE_EX]
            attribute_label = str(self.attribute_labels[node.attribute_index])
            print(colors[depth%10] + '\n' + f"{indent*depth} level-{depth}: {attribute_label} <= {node.condition_value:.2f}: ", end='')
            self.print(node.left, depth+1)
            
            print(colors[depth%10] + '\n' + f"{indent*depth} level-{depth}: {attribute_label} > {node.condition_value:.2f}: ", end='')
            self.print(node.right, depth+1)
        


# %%
def test_accuracy(expected_results, real_results):
    correct_count = 0
    for exp, real in zip(expected_results, real_results):
        if exp == real:
            correct_count +=1
    return correct_count/len(expected_results)


# %%
def clear_data(data):
    cleared_data = []
    data_size = len(data)
    for i in range(1, data_size):
        record = data.iloc[i]
        if record.isnull().any():
            continue
        else:
            cleared_data.append(record)
    return np.array(cleared_data)

# %%
data = pd.read_csv('water_potability.csv')
data_labels = data.columns.values
data = clear_data(data)
data = data[:301]

train_percent = 0.7
data_train = data[:(int)(len(data)*train_percent)]
data_test = data[(int)(len(data)*train_percent):]

# %%
tree = DecisionTreeCART(data_train, data_labels, 10, 10)

# %%
tree.print()
tree.clean()
tree.print()

# %%
class_values_pred = tree.predict(data_test)
test_accuracy(data_test[:,-1], class_values_pred)

# %%
tree.prune(4)
tree.print()



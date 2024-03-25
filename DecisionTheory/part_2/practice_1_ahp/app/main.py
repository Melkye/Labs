from read_file import *
import numpy as np


def print_to_file(data="", filename="results.txt", end="\n"):
    with open(filename, "a") as file:
        file.write(str(data))
        file.write(end)


def clear_file(filename="results.txt"):
    with open(filename, "w"):
        pass


def simple_vector_iteration(A, max_iter=1000, accuracy=1e-6):
    """
    Calculate the maximum characteristic number of matrix A using simple vector iteration method.
    """
    n = A.shape[0]

    # Initialize a random non-zero vector
    x = np.random.rand(n)
    x /= np.linalg.norm(x)

    for _ in range(max_iter):
        Ax = np.dot(A, x)

        # Normalize the result
        x_new = Ax / np.linalg.norm(Ax)

        # Check for convergence
        if np.linalg.norm(x_new - x) < accuracy:
            break

        x = x_new

    # Calculate the maximum characteristic number
    max_char_num = np.dot(np.dot(x, A), x)  # Equivalent to x.T @ A @ x

    return max_char_num


def simple_vector_iteration_detalized(A, max_iter=1000, accuracy=1e-6):
    """
    Calculate the maximum characteristic number of matrix A using simple vector iteration method.

    Parameters:
        A (numpy.ndarray): Input square matrix.
        max_iter (int): Maximum number of iterations.
        tol (float): Convergence tolerance.

    Returns:
        float: Maximum characteristic number.
    """
    n = A.shape[0]

    x_iter = []
    vec_iter = []
    # Initialize a random non-zero vector
    x = np.random.rand(n)
    zvit_x = np.ones(n)
    x /= np.linalg.norm(x)

    for _ in range(max_iter):
        # Multiply A with x
        Ax = np.dot(A, x)
        zvit_Ax = np.dot(A, zvit_x)
        vec_iter.append(zvit_Ax)
        # Normalize the result
        x_new = Ax / np.linalg.norm(Ax)

        # Check for convergence
        if np.linalg.norm(x_new - x) < accuracy:
            break
        x_iter.append(zvit_Ax/zvit_x)
        zvit_x = zvit_Ax
        x = x_new

    print_to_file("Max characteristic number:")
    print_to_file("Vector sequence x(m)=Ax(m+1):")
    vec_iter = np.transpose(np.array(vec_iter))
    for row in vec_iter:
        for data in row:
            print_to_file('%12.2f' % round(data, 6), end=" ")
        print_to_file()

    print_to_file()
    print_to_file("Sequence x(m+1)/x(m):")
    x_iter = np.transpose(np.array(x_iter))
    for row in x_iter:
        for data in row:
            print_to_file('%4.6f' % round(data, 6), end=" ")
        print_to_file()

    # Calculate the maximum characteristic number
    max_char_num = np.dot(np.dot(x, A), x)  # Equivalent to x.T @ A @ x

    return max_char_num


def geometric_mean_method_detalized(A):
    n = len(A)
    w = np.zeros(n)

    # Calculating the geometric mean for each row
    prod = []
    for i in range(n):
        product = 1.0
        for j in range(n):
            product *= A[i][j]
        prod.append(product)
        w[i] = product ** (1 / n)
    print_to_file()
    print_to_file("Initial:")
    for data in prod:
        print_to_file('%4.6f' % round(data, 4), end=" ")
    # print_to_file()
    # print_to_file("Sqrt(n) from row product (v):")
    # for data in w: print_to_file('%4.6f' % round(data, 4), end=" ")
    # Normalizing the weights
    w /= np.sum(w)
    print_to_file()
    print_to_file("Geometric mean (weights):")
    for data in w:
        print_to_file('%4.6f' % round(data, 4), end=" ")

    return np.array(w)


def geometric_mean_method(A):
    n = len(A)
    w = np.zeros(n)

    # Calculating the geometric mean for each row
    for i in range(n):
        product = 1.0
        for j in range(n):
            product *= A[i][j]
        w[i] = product ** (1 / n)

    # Normalizing the weights
    w /= np.sum(w)

    return np.array(w)


################################################################################################################
clear_file()

# Known constants
CIS = [0, 0, 0.52, 0.89, 1.11, 1.25, 1.35, 1.4, 1.45, 1.49]

# Example usage:
max_char_num = simple_vector_iteration(np.array(mpp_experts))
CI = (max_char_num-experts)/(experts-1)
CR = CI/CIS[experts-1]

weights_exp = geometric_mean_method(mpp_experts)
print_to_file()
print_to_file("Experts:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_exp, 6)}")

# First Expert
print_to_file()
print_to_file("-----------------------------")
print_to_file()
print_to_file("1st expert:")
max_char_num = simple_vector_iteration(np.array(mpp_criteria_1_Expert))
CI = (max_char_num-criteria_num)/(criteria_num-1)
CR = CI/CIS[criteria_num-1]
weights_cr = geometric_mean_method(mpp_criteria_1_Expert)
print_to_file()
print_to_file("Criteria:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_cr, 6)}")

print_to_file()
print_to_file('----------------------')
print_to_file()
print_to_file("Pair-wise comparisons of 1st criterion for 1st expert:")
for row in mpp_alternatives_1_Criteria_1_Expert:
    for data in row:
        print_to_file('%4.2f' % round(data, 2), end=" ")
    print_to_file()
print_to_file()

max_char_num = simple_vector_iteration_detalized(
    np.array(mpp_alternatives_1_Criteria_1_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
print_to_file()
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI = (L_max-k)/(k-1): ({round(max_char_num, 6)}-" +
              f"{alternatives_num} / {alternatives_num}-1) = {np.round(CI, 6)}")
print_to_file(f"CIS: {CIS}")
print_to_file(f"CR = CI/CIS: {round(CI, 6)}/" +
              f"{CIS[alternatives_num-1]} = {round(CR, 6)}")
print_to_file()
print_to_file("Weights calculation:", end="")
weights_1 = geometric_mean_method_detalized(
    mpp_alternatives_1_Criteria_1_Expert)
# print_to_file()
# print_to_file("Weights:")
# for data in weights_1:
#     print_to_file('%4.6f' % round(data, 4), end=" ")
print_to_file()
print_to_file('-----------------------')

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_2_Criteria_1_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_2 = geometric_mean_method(mpp_alternatives_2_Criteria_1_Expert)
print_to_file()
print_to_file("Pair-wise comparisons of alternatives by criteria 2:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_2, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_3_Criteria_1_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_3 = geometric_mean_method(mpp_alternatives_3_Criteria_1_Expert)
print_to_file()
print_to_file("Pair-wise comparisons of alternatives by criteria 3:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_3, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_4_Criteria_1_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_4 = geometric_mean_method(mpp_alternatives_4_Criteria_1_Expert)
print_to_file()
print_to_file("Pair-wise comparisons of alternatives by criteria 4:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_4, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_5_Criteria_1_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_5 = geometric_mean_method(mpp_alternatives_5_Criteria_1_Expert)
print_to_file()
print_to_file("Pair-wise comparisons of alternatives by criteria 5:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_5, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_6_Criteria_1_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_6 = geometric_mean_method(mpp_alternatives_6_Criteria_1_Expert)
print_to_file()
print_to_file("Pair-wise comparisons of alternatives by criteria 6:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_6, 6)}")

weights = np.array([weights_1, weights_2, weights_3,
                   weights_4, weights_5, weights_6])
weights_1_Expert = np.dot(weights_cr, weights)
print_to_file()
print_to_file("Weights for criteria of 1st expert:")
print_to_file(np.round(weights_1_Expert, 6))
print_to_file()
print_to_file("-----------------------")
print_to_file()

# Second Expert
print_to_file("2nd expert:")
max_char_num = simple_vector_iteration(np.array(mpp_criteria_2_Expert))
CI = (max_char_num-criteria_num)/(criteria_num-1)
CR = CI/CIS[criteria_num-1]
weights_cr = geometric_mean_method(mpp_criteria_2_Expert)
print_to_file()
print_to_file("Criteria:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_cr, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_1_Criteria_2_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_1 = geometric_mean_method(mpp_alternatives_1_Criteria_2_Expert)
print_to_file()
print_to_file("Criterion 1:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_1, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_2_Criteria_2_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_2 = geometric_mean_method(mpp_alternatives_2_Criteria_2_Expert)
print_to_file()
print_to_file("Criterion 2:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_2, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_3_Criteria_2_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_3 = geometric_mean_method(mpp_alternatives_3_Criteria_2_Expert)
print_to_file()
print_to_file("Criterion 3:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_3, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_4_Criteria_2_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_4 = geometric_mean_method(mpp_alternatives_4_Criteria_2_Expert)
print_to_file()
print_to_file("Criterion 4:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_4, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_5_Criteria_2_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_5 = geometric_mean_method(mpp_alternatives_5_Criteria_2_Expert)
print_to_file()
print_to_file("Criterion 5:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_5, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_6_Criteria_2_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_6 = geometric_mean_method(mpp_alternatives_6_Criteria_2_Expert)
print_to_file()
print_to_file("Criterion 6:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_6, 6)}")


weights = np.array([weights_1, weights_2, weights_3,
                   weights_4, weights_5, weights_6])
weights_2_Expert = np.dot(weights_cr, weights)
print_to_file()
print_to_file("Weights for criteria of 2nd expert: ")
print_to_file(np.round(weights_2_Expert, 6))
print_to_file()
print_to_file("-----------------------")
print_to_file()

# Third Expert
print_to_file("3rd expert:")
max_char_num = simple_vector_iteration(np.array(mpp_criteria_3_Expert))
CI = (max_char_num-criteria_num)/(criteria_num-1)
CR = CI/CIS[criteria_num-1]
weights_cr = geometric_mean_method(mpp_criteria_3_Expert)
print_to_file()
print_to_file("Criteria:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_cr, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_1_Criteria_3_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_1 = geometric_mean_method(mpp_alternatives_1_Criteria_3_Expert)
print_to_file()
print_to_file("Criterion 1:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_1, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_2_Criteria_3_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_2 = geometric_mean_method(mpp_alternatives_2_Criteria_3_Expert)
print_to_file()
print_to_file("Criterion 2:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_2, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_3_Criteria_3_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_3 = geometric_mean_method(mpp_alternatives_3_Criteria_3_Expert)
print_to_file()
print_to_file("Criterion 3:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_3, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_4_Criteria_3_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_4 = geometric_mean_method(mpp_alternatives_4_Criteria_3_Expert)
print_to_file()
print_to_file("Criterion 4:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_4, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_5_Criteria_3_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_5 = geometric_mean_method(mpp_alternatives_5_Criteria_3_Expert)
print_to_file()
print_to_file("Criterion 5:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_5, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_6_Criteria_3_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_6 = geometric_mean_method(mpp_alternatives_6_Criteria_3_Expert)
print_to_file()
print_to_file("Criterion 6:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_6, 6)}")

weights = np.array([weights_1, weights_2, weights_3,
                   weights_4, weights_5, weights_6])
weights_3_Expert = np.dot(weights_cr, weights)
print_to_file()
print_to_file("Weights for criteria of 3rd expert: ")
print_to_file(np.round(weights_3_Expert, 6))
print_to_file()
print_to_file("-----------------------")
print_to_file()

# Fourth Expert
print_to_file("4th expert:")
max_char_num = simple_vector_iteration(np.array(mpp_criteria_4_Expert))
CI = (max_char_num-criteria_num)/(criteria_num-1)
CR = CI/CIS[criteria_num-1]
weights_cr = geometric_mean_method(mpp_criteria_4_Expert)
print_to_file()
print_to_file("Criteria:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_cr, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_1_Criteria_4_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_1 = geometric_mean_method(mpp_alternatives_1_Criteria_4_Expert)
print_to_file()
print_to_file("Criterion 1:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_1, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_2_Criteria_4_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_2 = geometric_mean_method(mpp_alternatives_2_Criteria_4_Expert)
print_to_file()
print_to_file("Criterion 2:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_2, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_3_Criteria_4_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_3 = geometric_mean_method(mpp_alternatives_3_Criteria_4_Expert)
print_to_file()
print_to_file("Criterion 3:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_3, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_4_Criteria_4_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_4 = geometric_mean_method(mpp_alternatives_4_Criteria_4_Expert)
print_to_file()
print_to_file("Criterion 4:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_4, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_5_Criteria_4_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_5 = geometric_mean_method(mpp_alternatives_5_Criteria_4_Expert)
print_to_file()
print_to_file("Criterion 5:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_5, 6)}")

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_6_Criteria_4_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_6 = geometric_mean_method(mpp_alternatives_6_Criteria_4_Expert)
print_to_file()
print_to_file("Criterion 6:")
print_to_file(f"Max characteristic number L_max: {np.round(max_char_num, 6)}")
print_to_file(f"CI: {np.round(CI, 6)}")
print_to_file(f"CR: {np.round(CR, 6)}")
print_to_file(f"Weights: {np.round(weights_6, 6)}")

weights = np.array([weights_1, weights_2, weights_3,
                   weights_4, weights_5, weights_6])
weights_4_Expert = np.dot(weights_cr, weights)
print_to_file()
print_to_file("Weights for criteria of 4th expert:")
print_to_file(np.round(weights_4_Expert, 6))

# Global weights
weights = np.array([weights_1_Expert, weights_2_Expert,
                   weights_3_Expert, weights_4_Expert])
weights_Global = np.dot(weights_exp, weights)
print_to_file()
print_to_file(f"Resulting weight coefficients: {np.round(weights_Global, 6)}")

alternatives = np.argsort(weights_Global)
alternatives = [x+1 for x in alternatives]
print_to_file()
print_to_file(f"Best alternative: {alternatives[len(alternatives)-1]}")
print_to_file(f"Sorted: {np.sort(weights_Global)[::-1]}")
print_to_file(f"Ranking: {alternatives[::-1]}")

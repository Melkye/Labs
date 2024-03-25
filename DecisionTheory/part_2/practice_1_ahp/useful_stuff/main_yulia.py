from read_file_yulia import *
import numpy as np


def simple_vector_iteration(A, max_iter=1000, tol=1e-6):
    """
    Calculate the maximum characteristic number of matrix A using simple vector iteration method.
    """
    n = A.shape[0]

    # Initialize a random non-zero vector
    x = np.random.rand(n)
    x /= np.linalg.norm(x)

    for _ in range(max_iter):
        # Multiply A with x
        Ax = np.dot(A, x)

        # Normalize the result
        x_new = Ax / np.linalg.norm(Ax)

        # Check for convergence
        if np.linalg.norm(x_new - x) < tol:
            break

        x = x_new

    # Calculate the maximum characteristic number
    max_char_num = np.dot(np.dot(x, A), x)  # Equivalent to x.T @ A @ x

    return max_char_num


def simple_vector_iteration_detalized(A, max_iter=1000, tol=1e-8):
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
        if np.linalg.norm(x_new - x) < tol:
            break
        x_iter.append(zvit_Ax/zvit_x)
        zvit_x = zvit_Ax
        x = x_new

    print("Розрахунок максимального характеристичного числа:")
    print("Векторна послідовність x(m)=Ax(m+1):")
    vec_iter = np.transpose(np.array(vec_iter))
    for row in vec_iter:
        for data in row:
            print('%12.2f' % round(data, 6), end=" ")
        print()

    print("\nПослідовність x(m+1)/x(m):")
    x_iter = np.transpose(np.array(x_iter))
    for row in x_iter:
        for data in row:
            print('%4.6f' % round(data, 6), end=" ")
        print()

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
    print("\nСпочатку:")
    for data in prod:
        print('%4.6f' % round(data, 4), end=" ")
    # print("\nSqrt(n) from row product (v):")
    # for data in w: print('%4.6f' % round(data, 4), end=" ")
    # Normalizing the weights
    w /= np.sum(w)
    print("\nСереднє геометричне (w):")
    for data in w:
        print('%4.6f' % round(data, 4), end=" ")

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


# Constants
CIS = [0, 0, 0.52, 0.89, 1.11, 1.25, 1.35, 1.4, 1.45, 1.49]

# Example usage:
max_char_num = simple_vector_iteration(np.array(mpp_experts))
CI = (max_char_num-experts)/(experts-1)
CR = CI/CIS[experts-1]

weights_exp = geometric_mean_method(mpp_experts)
print("\nЕксперти:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_exp, 6))

# First Expert
print("\n-----------------------------\nПерший експерт:")
max_char_num = simple_vector_iteration(np.array(mpp_criteria_1_Expert))
CI = (max_char_num-criteria_num)/(criteria_num-1)
CR = CI/CIS[criteria_num-1]
weights_cr = geometric_mean_method(mpp_criteria_1_Expert)
print("\nКритерії:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_cr, 6))

print('\n----------------------')
print("\nМПП 1-го критерія 1-го експерта:")
for row in mpp_alternatives_1_Criteria_1_Expert:
    for data in row:
        print('%4.6f' % round(data, 6), end=" ")
    print()
print()
max_char_num = simple_vector_iteration_detalized(
    np.array(mpp_alternatives_1_Criteria_1_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
print("\nМаксимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI = (L_max-k)/(k-1): (", round(max_char_num, 6), "-",
      alternatives_num, ")/(", alternatives_num, "-1) = ", np.round(CI, 6))
print("Значення CIS:", CIS)
print("CR = CI/CIS: ", round(CI, 6), "/",
      CIS[alternatives_num-1], " = ", round(CR, 6))
print("\nПідрахунок вагових коефіцієнтів:", end="")
weights_1 = geometric_mean_method_detalized(
    mpp_alternatives_1_Criteria_1_Expert)
print("\nВагові коефіцієнти:")
for data in weights_1:
    print('%4.6f' % round(data, 4), end=" ")
print('\n-----------------------')

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_2_Criteria_1_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_2 = geometric_mean_method(mpp_alternatives_2_Criteria_1_Expert)
print("\n\nМПП альтернатив за критерієм  2:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI number:", np.round(CI, 6))
print("CR number:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_2, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_3_Criteria_1_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_3 = geometric_mean_method(mpp_alternatives_3_Criteria_1_Expert)
print("\nМПП альтернатив за критерієм  3:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI number:", np.round(CI, 6))
print("CR number:", np.round(CR, 6))
print("Weighting coefficients:", np.round(weights_3, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_4_Criteria_1_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_4 = geometric_mean_method(mpp_alternatives_4_Criteria_1_Expert)
print("\nМПП альтернатив за критерієм  4:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI number:", np.round(CI, 6))
print("CR number:", np.round(CR, 6))
print("Weighting coefficients:", np.round(weights_4, 6))

weights = np.array([weights_1, weights_2, weights_3, weights_4])
weights_1_Expert = np.dot(weights_cr, weights)
print("\nГлобальні вагові коефіцієнти по МПП 1-го експерта: \n",
      np.round(weights_1_Expert, 6))

# Second Expert
print("\n\n\n-----------------------\nДругий експерт:")
max_char_num = simple_vector_iteration(np.array(mpp_criteria_2_Expert))
CI = (max_char_num-criteria_num)/(criteria_num-1)
CR = CI/CIS[criteria_num-1]
weights_cr = geometric_mean_method(mpp_criteria_2_Expert)
print("\nКритерії:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_cr, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_1_Criteria_2_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_1 = geometric_mean_method(mpp_alternatives_1_Criteria_2_Expert)
print("\nКритерій 1:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_1, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_2_Criteria_2_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_2 = geometric_mean_method(mpp_alternatives_2_Criteria_2_Expert)
print("\nКритерій 2:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_2, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_3_Criteria_2_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_3 = geometric_mean_method(mpp_alternatives_3_Criteria_2_Expert)
print("\nКритерій 3:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", weights_3)

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_4_Criteria_2_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_4 = geometric_mean_method(mpp_alternatives_4_Criteria_2_Expert)
print("\nКритерій 4:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_4, 6))


weights = np.array([weights_1, weights_2, weights_3, weights_4])
weights_2_Expert = np.dot(weights_cr, weights)
print("\nГлобальні вагові коефіцієнти для МПП 2-го експерта\n:", weights_2_Expert)

# Third Expert
print("\n\n\n-----------------------\nТретій експерт:")
max_char_num = simple_vector_iteration(np.array(mpp_criteria_3_Expert))
CI = (max_char_num-criteria_num)/(criteria_num-1)
CR = CI/CIS[criteria_num-1]
weights_cr = geometric_mean_method(mpp_criteria_3_Expert)
print("\nКритерії:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_cr, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_1_Criteria_3_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_1 = geometric_mean_method(mpp_alternatives_1_Criteria_3_Expert)
print("\nКритерій 1:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_1, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_2_Criteria_3_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_2 = geometric_mean_method(mpp_alternatives_2_Criteria_3_Expert)
print("\nКритерій 2:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_2, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_3_Criteria_3_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_3 = geometric_mean_method(mpp_alternatives_3_Criteria_3_Expert)
print("\nКритерій 3:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_3, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_4_Criteria_3_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_4 = geometric_mean_method(mpp_alternatives_4_Criteria_3_Expert)
print("\nКритерій 4:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_4, 6))

weights = np.array([weights_1, weights_2, weights_3, weights_4])
weights_3_Expert = np.dot(weights_cr, weights)
print("\nГлобальні коефіцієнти для МПП 3-го експерта:\n",
      np.round(weights_3_Expert, 6))

# Fourth Expert
print("\n\n\n-----------------------\nЧетвертий експерт:")
max_char_num = simple_vector_iteration(np.array(mpp_criteria_4_Expert))
CI = (max_char_num-criteria_num)/(criteria_num-1)
CR = CI/CIS[criteria_num-1]
weights_cr = geometric_mean_method(mpp_criteria_4_Expert)
print("\nКритерії:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_cr, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_1_Criteria_4_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_1 = geometric_mean_method(mpp_alternatives_1_Criteria_4_Expert)
print("\nКритерій 1:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_1, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_2_Criteria_4_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_2 = geometric_mean_method(mpp_alternatives_2_Criteria_4_Expert)
print("\nКритерій 2:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_2, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_3_Criteria_4_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_3 = geometric_mean_method(mpp_alternatives_3_Criteria_4_Expert)
print("\nКритерій 3:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_3, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_4_Criteria_4_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_4 = geometric_mean_method(mpp_alternatives_4_Criteria_4_Expert)
print("\nКритерій 4:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_4, 6))

weights = np.array([weights_1, weights_2, weights_3, weights_4])
weights_4_Expert = np.dot(weights_cr, weights)
print("\nГлобальні вагові коефіцієнти для МПП 4-го експерта\n:",
      np.round(weights_4_Expert, 6))


# Fifth Expert
print("\n\n\n-----------------------\nП'ятий експерт:")
max_char_num = simple_vector_iteration(np.array(mpp_criteria_5_Expert))
CI = (max_char_num-criteria_num)/(criteria_num-1)
CR = CI/CIS[criteria_num-1]
weights_cr = geometric_mean_method(mpp_criteria_5_Expert)
print("\nКритерії:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_cr, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_1_Criteria_5_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_1 = geometric_mean_method(mpp_alternatives_1_Criteria_5_Expert)
print("\nКритерій 1:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_1, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_2_Criteria_5_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_2 = geometric_mean_method(mpp_alternatives_2_Criteria_5_Expert)
print("\nКритерій 2:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_2, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_3_Criteria_5_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_3 = geometric_mean_method(mpp_alternatives_3_Criteria_5_Expert)
print("\nКритерій 3:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_3, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_4_Criteria_5_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_4 = geometric_mean_method(mpp_alternatives_4_Criteria_5_Expert)
print("\nКритерій 4:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_4, 6))

weights = np.array([weights_1, weights_2, weights_3, weights_4])
weights_5_Expert = np.dot(weights_cr, weights)
print("\nГлобальні вагові коефіцієнти для МПП 5-го експерта:\n",
      np.round(weights_5_Expert, 6))

# Sixth Expert
print("\n\n\n-----------------------\nШостий експерт:")
max_char_num = simple_vector_iteration(np.array(mpp_criteria_6_Expert))
CI = (max_char_num-criteria_num)/(criteria_num-1)
CR = CI/CIS[criteria_num-1]
weights_cr = geometric_mean_method(mpp_criteria_6_Expert)
print("\nКритерії:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_cr, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_1_Criteria_6_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_1 = geometric_mean_method(mpp_alternatives_1_Criteria_6_Expert)
print("\nКритерій 1:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_1, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_2_Criteria_6_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_2 = geometric_mean_method(mpp_alternatives_2_Criteria_6_Expert)
print("\nКритерій 2:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_2, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_3_Criteria_6_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_3 = geometric_mean_method(mpp_alternatives_3_Criteria_6_Expert)
print("\nКритерій 3:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_3, 6))

max_char_num = simple_vector_iteration(
    np.array(mpp_alternatives_4_Criteria_6_Expert))
CI = (max_char_num-alternatives_num)/(alternatives_num-1)
CR = CI/CIS[alternatives_num-1]
weights_4 = geometric_mean_method(mpp_alternatives_4_Criteria_6_Expert)
print("\nКритерій 4:")
print("Максимальне характеристичне число L_max:", np.round(max_char_num, 6))
print("CI:", np.round(CI, 6))
print("CR:", np.round(CR, 6))
print("Вагові коефіцієнти:", np.round(weights_4, 6))

weights = np.array([weights_1, weights_2, weights_3, weights_4])
weights_6_Expert = np.dot(weights_cr, weights)
print("\nГлобальні вагові коефіцієнти для МПП 6-го експерта\n:",
      np.round(weights_6_Expert, 6))

# Global weights
weights = np.array([weights_1_Expert, weights_2_Expert, weights_3_Expert, weights_4_Expert, weights_5_Expert,
                    weights_6_Expert])
weights_Global = np.dot(weights_exp, weights)
print("\nГлобальні вагові коефіцієнти:", np.round(weights_Global, 6))

alternatives = np.argsort(weights_Global)
alternatives = [x+1 for x in alternatives]
print("\n\nНайкраща альтернатива: ", (alternatives[len(alternatives)-1]))
print("Відсортовані: ", np.sort(weights_Global)[::-1])
print("Ранжування: ", alternatives[::-1])

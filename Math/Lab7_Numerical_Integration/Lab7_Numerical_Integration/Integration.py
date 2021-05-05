import numpy as np

def f(x):
    return np.cos(x)/(x+1)

def trapezoid(a, b, n):
    h = (b - a) / n
    x = a
    result = 0
    for i in range(n):
        result += (f(x) + f(x + h))/2
        x += h
    result *= h
    return result

def gaussian(a, b, n):
    if n == 1:
        A = [2]
        T = [0.5]
    elif n == 2:
        A = [1, 1]
        T = [-0.577350, 0.577350]
    elif n == 3:
        A = [0.555556, 0.888889, 0.555556]
        T = [-0.774597, 0, 0.774597]
    elif n == 4:
        A = [0.347855, 0.652145, 0.652145, 0.347855]
        T = [-0.861136, -0.339981, 0.339981, 0.861136]
    elif n == 5:
        A = [0.236927, 0.478629, 0.568889, 0.478629, 0.236927]
        T = [-0.906190, -0.538470, 0, 0.538470, 0.906180]

    result = 0
    for i in range(n):
        x = (a + b) / 2 + T[i] * (b - a) / 2;
        result += A[i]*f(x)
    result *= (b - a) / 2
    return result
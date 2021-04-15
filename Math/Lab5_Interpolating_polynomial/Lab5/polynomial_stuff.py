#polynomial_stuff.py

import numpy as np

def get_y_values(x):
    y = []
    for i in range(len(x)):
        y.append(np.sin(x[i]/2) + np.cbrt(x[i]))
    return y

def newtons_polinomial(x, y):
    div_diffs = [y]
    step = 0
    for j in range(1, len(x)):
        div_diffs.append([])
        for i in range(0, len(x) - 1 - step):
            div_diffs[j].append((div_diffs[j-1][i] - div_diffs[j-1][i+1])
                                 /(x[i] - x[i+j]))
        step+=1
    return div_diffs

def print_polynomial(div_diffs, x):
    print("Newton's polynomial:")
    for i in range(len(x)):
        print(f'{div_diffs[i][0]:.6f}', end = '')
        for j in range(i):
            if x[j] >= 0:
                print(f'*(x-{x[j]})', end = '')
            else:
                print(f'*(x+{abs(x[j])})', end = '')
        print(' ', end = '')
        if i != len(x)-1 and div_diffs[i+1][0] > 0:
            print('+', end = '')
    print()

def cub_spline(x, y, x0):
    a = []
    b = []
    d = []
    h = []
    for i in range(1, len(x)):
        a.append(y[i-1])
        h.append(x[i] - x[i-1])
    
    vector_b = []
    vector_d = []
    for i in range(1, len(x)-1):
        vector_b.append(2*(h[i-1]+h[i]))
        vector_d.append(6*((y[i+1]-y[i])/h[i] - (y[i]-y[i-1])/h[i-1]))
    vector_a = h[:len(x)-3]
    vector_a.insert(0, 0)
    vector_c = h[1:len(x)-2]
    vector_c.insert(len(h), 0)

    c = progon(vector_a, vector_b, vector_c, vector_d)
    c.insert(0, 0)
    c.insert(len(c), 0)
    for i in range(len(x) - 1):
        if i == len(x) - 2:
            d.append(-1*c[len(x)-2]/(3*h[i]))
            b.append(-2*h[i]*c[i]/3 + (y[i+1]-y[i])/h[i])
        else:
            d.append((c[i+1] - c[i])/(3*h[i]))
            b.append((y[i+1]-y[i])/h[i] - c[i]*h[i] - d[i]*h[i]*h[i])
    return a, b, c, d

def progon(a, b, c, d):
    A = []
    B = []
    A.append(-c[1]/b[1])
    B.append(d[1]/b[1])
    for i in range(1, len(d)):
        e = a[i]*A[i-1]+b[i]
        A.append(-c[i]/e)
        B.append((d[i]-a[i]*B[i-1])/e)
    x = []
    x.insert(0, B[len(d)-1])
    for i in range(len(d)-2, -1, -1):
            x.insert(0, A[i]*x[0] + B[i])
    return x

def print_splines(a, b, c, d, x):
    print("Cubic spline polynomials:")
    for i in range (len(a)):

        pars = f"(x-{x[i]})" if x[i] >= 0 else f"(x+{abs(x[i])})"
        print(f'{a[i]:-9.6f} ', end = '')

        print(f'+', end = '') if b[i] > 0 else print(f'-', end = '')
        print(f'{abs(b[i]):-9.6f}{pars} ', end = '')

        print(f'+', end = '') if c[i] > 0 else print(f'-', end = '')
        print(f'{abs(c[i]):-9.6f}{pars}^2 ', end = '')

        print(f'+', end = '') if d[i] > 0 else print(f'-', end = '')
        print(f'{abs(d[i]):-9.6f}{pars}^3 for x in [{x[i]:2};{x[i+1]:2}]')
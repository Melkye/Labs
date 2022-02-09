import matplotlib.pyplot as plt
import math


x_emp = [1.73, 2.56, 3.39, 4.22, 5.05, 5.89, 6.70, 7.53]
y_emp = [0.63, 1.11, 1.42, 1.96, 2.30, 2.89, 3.29, 3.87]

def compute_linear_coeffs(x, y):
    expected_x = 0
    expected_y = 0
    expected_xy = 0
    expected_x_sqr = 0
    n = len(x)
    for i in range(n):
        expected_x += x[i]
        expected_y += y[i]
        expected_xy += x[i]*y[i]
        expected_x_sqr += x[i]*x[i]
    expected_x = expected_x/n
    expected_y = expected_y/n
    expected_xy = expected_xy/n
    expected_x_sqr = expected_x_sqr/n
    a = (expected_xy - expected_x*expected_y)/(expected_x_sqr - expected_x**2)
    b = expected_y - a*expected_x
    return a, b

plt.figure(num='Regression v2')
plt.scatter(x_emp, y_emp)

def linear_fun(a, b, x):
    return a*x+b
def hyperbolic_fun(a, b, x):
    return a/x + b
def power_fun(a, b, x):
    return b*(x**a)
def exponential_fun(a, b, x):
    return b*math.exp(a*x)
def logarithmic_fun(a, b, x):
    return b + a*math.log(x)

print(f"{'x empirical:':42}", end=" ")
for i in range(len(x_emp)):
    print(f"{x_emp[i]:5.3}", end=" ")
print("")
print(f"{'y empirical:':42}", end=" ")
for i in range(len(y_emp)):
    print(f"{y_emp[i]:5.3}", end=" ")
print("")

#linear
u = x_emp[:]
g = y_emp[:]

c, d = compute_linear_coeffs(u, g)

y_approx = [linear_fun(c, d, x) for x in x_emp]

residuals_squared_sum = 0
print(f"{'Linear regression':22}: a={c:6.3} b={d:7.3}", end=" ")
for i in range(len(y_approx)):
    print(f"{y_approx[i]:5.3}", end=" ")
    residuals_squared_sum += (y_approx[i] - y_emp[i])**2
print(f"S={residuals_squared_sum:5.3}")

plt.plot(u, y_approx, 'r', label="linear")

#hyperbolic
u = [1/x for x in x_emp]
g = y_emp[:]

c, d = compute_linear_coeffs(u, g)

y_approx = [hyperbolic_fun(c, d, x) for x in x_emp]

residuals_squared_sum = 0
print(f"{'Hyperbolic regression':22}: a={c:6.3} b={d:7.3}", end=" ")
for i in range(len(y_approx)):
    print(f"{y_approx[i]:5.3}", end=" ")
    residuals_squared_sum += (y_approx[i] - y_emp[i])**2
print(f"S={residuals_squared_sum:5.3}")

plt.plot(x_emp, y_approx, 'b', label="hyperbolic")

#power
u = [math.log(x) for x in x_emp]
g = [math.log(y) for y in y_emp]

c, d = compute_linear_coeffs(u, g)
d = math.exp(d)
y_approx = [power_fun(c, d, x) for x in x_emp]

residuals_squared_sum = 0
print(f"{'Power regression':22}: a={c:6.3} b={d:7.3}", end=" ")
for i in range(len(y_approx)):
    print(f"{y_approx[i]:5.3}", end=" ")
    residuals_squared_sum += (y_approx[i] - y_emp[i])**2
print(f"S={residuals_squared_sum:5.3}")

plt.plot(x_emp, y_approx, 'g', label="power")

#exponential
u = x_emp[:]
g = [math.log(y) for y in y_emp]

c, d = compute_linear_coeffs(u, g)
d = math.exp(d)
y_approx = [exponential_fun(c, d, x) for x in x_emp]

residuals_squared_sum = 0
print(f"{'Exponential regression':22}: a={c:6.3} b={d:7.3}", end=" ")
for i in range(len(y_approx)):
    print(f"{y_approx[i]:5.3}", end=" ")
    residuals_squared_sum += (y_approx[i] - y_emp[i])**2
print(f"S={residuals_squared_sum:5.3}")

plt.plot(x_emp, y_approx, 'y', label="exponential")

#logarithmic
u = [math.log(x) for x in x_emp]
g = y_emp[:]

c, d = compute_linear_coeffs(u, g)

y_approx = [logarithmic_fun(c, d, x) for x in x_emp]

residuals_squared_sum = 0
print(f"{'Logarithmic regression':22}: a={c:6.3} b={d:7.3}", end=" ")
for i in range(len(y_approx)):
    print(f"{y_approx[i]:5.3}", end=" ")
    residuals_squared_sum += (y_approx[i] - y_emp[i])**2
print(f"S={residuals_squared_sum:5.3}")

plt.plot(x_emp, y_approx, 'c', label="logarithmic")

plt.xlabel('x')
plt.ylabel('y')
plt.legend();
plt.show()

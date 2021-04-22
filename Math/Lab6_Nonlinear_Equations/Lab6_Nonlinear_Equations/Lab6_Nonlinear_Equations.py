import numpy as np
import specify

coeffs = [2, -3, 0, 7, 0, -3]
pol = np.polynomial.Polynomial(coeffs);
pol_d = pol._get_coefficients(pol.deriv())
a1 = 0.3956
b1 = 1
precision = 0.00001
x1, counter1 = specify.bisection_method(coeffs, a1, b1, precision)
x2, counter2 = specify.chord_method(coeffs, a1, b1, precision)
x3, counter3 = specify.newtons_method(coeffs, a1, b1, precision)

print(f" Results for x in ({a1};{b1}) ε={precision}:")
print(f" Bisection method:\tx = {x1:.5} \t iter = {counter1}")
print(f" Chord method:\t\tx = {x2:.5} \t iter = {counter2}")
print(f" Newton's method:\tx = {x3:.5} \t iter = {counter3}")
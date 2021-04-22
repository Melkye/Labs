import numpy as np

def bisection_method(pol_coeffs, a, b, precision):
    pol = np.polynomial.Polynomial(pol_coeffs)
    iterations = 0
    while abs(b-a) > precision and abs(np.polyval(pol_coeffs, (a+b)/2)) > precision:
        iterations += 1
        c = (a+b)/2
        if np.polyval(pol_coeffs, a)*np.polyval(pol_coeffs, c) < 0:
            b = c
        else:
            a = c
    return (a+b)/2, iterations

def chord_method(pol_coeffs, a, b, precision):
    pol = np.polynomial.Polynomial(pol_coeffs)
    if np.polyval(pol_coeffs, a) > 0:
        x_prev = b
        x = x_prev - np.polyval(pol_coeffs, x_prev) \
            /(np.polyval(pol_coeffs, x_prev)-np.polyval(pol_coeffs, a))*(x_prev-a)
    else:
        x_prev = a
        x = x_prev - np.polyval(pol_coeffs, x_prev) \
            /(np.polyval(pol_coeffs, b)-np.polyval(pol_coeffs, x_prev))*(b- x_prev)
    iterations = 0
    while abs(x - x_prev) > precision and abs(np.polyval(pol_coeffs, x)) > precision:
        iterations += 1
        x_prev = x
        if np.polyval(pol_coeffs, a) > 0:
            x = x_prev - np.polyval(pol_coeffs, x_prev) \
                /(np.polyval(pol_coeffs, x_prev)-np.polyval(pol_coeffs, a))*(x_prev-a)
        else:
            x = x_prev - np.polyval(pol_coeffs, x_prev) \
                /(np.polyval(pol_coeffs, b)-np.polyval(pol_coeffs, x_prev))*(b- x_prev)
    return x, iterations

def newtons_method(pol_coeffs, a, b, precision):
    rev_pol_coeffs = pol_coeffs[:]
    rev_pol_coeffs.reverse()
    pol = np.polynomial.Polynomial(pol_coeffs)
    rev_pol = np.polynomial.Polynomial(rev_pol_coeffs)
    if np.polyval(pol._get_coefficients(rev_pol.deriv()), b) \
        *np.polyval(pol._get_coefficients(rev_pol.deriv(2)), b) < 0:
        x_prev = a
    else:
        x_prev = b
    x = x_prev - np.polyval(pol_coeffs, x_prev) \
        /np.polyval(pol._get_coefficients(rev_pol.deriv()), x_prev)
    iterations = 0
    while abs(x-x_prev) > precision and abs(np.polyval(pol_coeffs, x)) > precision:
        iterations += 1
        x_prev = x
        x = x_prev - np.polyval(pol_coeffs, x_prev) \
            /np.polyval(pol._get_coefficients(rev_pol.deriv()), x_prev)
    return x, iterations

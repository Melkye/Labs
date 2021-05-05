import Integration

a = 1
b = 3
precision = 0.0001

n = 46
tr_result = Integration.trapezoid(a, b, n)

m = 4
g_result = Integration.gaussian(a, b, m)

fun = "cos(x)/(x+1)"
print(f"Integral of {fun} in interval [{a};{b}], ε = {precision}:\n")
print(f"Trapezoid rule: {tr_result:.5} for n = {n}\n")
print(f"Gaussian method: {g_result:.5} for m = {m}")

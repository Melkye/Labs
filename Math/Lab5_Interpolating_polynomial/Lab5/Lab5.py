import polynomial_stuff

x = [-4, -2, 0, 2, 4]
y = polynomial_stuff.get_y_values(x)

coeffs = polynomial_stuff.newtons_polinomial(x, y)
polynomial_stuff.print_polynomial(coeffs, x)

a, b, c, d = polynomial_stuff.cub_spline(x, y, 2)
polynomial_stuff.print_splines(a, b, c, d, x)
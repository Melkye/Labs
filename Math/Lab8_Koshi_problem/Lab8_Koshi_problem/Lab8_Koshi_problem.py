import methods

def func(x, y):
    return 1 + 1.8*y*methods.np.sin(x) - y**2

x0 = 0
y0 = 0
x_end = 6
h = 0.1

x1, y1, e1 = methods.runge_kutta(x0, y0, x_end, func, h) # round x when writing to console
a = 1

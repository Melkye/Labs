import numpy as np
import matplotlib.pyplot as plt

def simple_stochastic_search(fun, args_low, args_high, number_of_points):
   number_of_args = len(args_low)
   min_value = np.inf
   min_args = []
   for k in range(number_of_points):
        args = []
        for i in range(number_of_args):
            args.append(np.random.uniform(args_low[i], args_high[i]))
        new_value = fun(args)
        if new_value < min_value:
            min_value = new_value
            min_args = [args]
        elif np.abs(new_value - min_value) < 10**-6:
            min_args.append([args])
   return min_value, min_args

def simulated_annealing(fun, args_low, args_high, t_max, t_min, t_decrease_rate):
    t = t_max
    min_args = []
    min_args_old = []
    number_of_args = len(args_low)
    for i in range(number_of_args):
         min_args.append(np.random.uniform(args_low[i], args_high[i]))
    min_args = [min_args]
    while (t > t_min):
        args = []
        valid_args = True
        for i in range(number_of_args):
            args.append(min_args[0][i] + np.random.standard_normal()*t)
            if args[-1] < args_low[i] or args[-1] > args_high[i]:
                valid_args = False
        if valid_args:
            delta_e = fun(args) - fun(min_args[0])
            if delta_e < 0:
                if np.abs(delta_e) < 10**-6:
                    min_args.append([args])
                else:
                    min_args = [args]
            elif np.e**(-delta_e/t) > np.random.uniform():
                if np.abs(delta_e) < 10**-6:
                    min_args.append([args])
                else:
                    min_args_old = min_args
                    min_args = [args]
            t = t*t_decrease_rate
    if np.abs(fun(min_args[0]) - fun(min_args_old[0]) < 10**-6):
        min_args.extend(min_args_old)
    return fun(min_args[0]), min_args

def f(args):
    x = args[0]
    y = args[1]
    return (4-2.1*x**2+x**4/3)*x**2 + x*y + 4*(y**2-1)*y**2

true_global_min = -1.03163
true_min_args = [[-0.08984, 0.71266], [0.08984, -0.71266]]
print(f"True global minimum is {true_global_min:.5}")
print("Its arguments are:")
for true_arg_vec in true_min_args:
    print(f"({true_arg_vec[0]:8.5};{true_arg_vec[1]:8.5})")

number_of_points = 10000
min_val, min_args = simple_stochastic_search(f, [-3, -2], [3, 2], number_of_points)
print()
print("Simple stochastic search:")
print(f"Number of points: {number_of_points}")
print(f"Minimum value is {min_val:.5}")
print("Its arguments are:")
for arg_vec in min_args:
    print(f"({arg_vec[0]:8.5};{arg_vec[1]:8.5})")

t_start = 50
t_min = 0.001
t_decrease_rate = 0.99
min_val, min_args = simulated_annealing(f, [-3, -2], [3, 2], t_start, t_min, t_decrease_rate)
print()
print("Simulated annealing:")
print(f"Start T: {t_start}, min T: {t_min}, decrease rate: {t_decrease_rate}")
print(f"Minimum value is {min_val:.5}")
print("Its arguments are:")
for arg_vec in min_args:
    print(f"({arg_vec[0]:8.5};{arg_vec[1]:8.5})")


fig = plt.figure(num='Global extrema v2')
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-3.0, 3.0, 0.05)
X, Y = np.meshgrid(x, y)
zs = np.array([f([x,y]) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z, vmin=-2.0)
ax.set_zlim(-2, 10)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

#Lab8_Koshi_problem.py
import methods
import matplotlib.pyplot as plt

def func(x, y):
    return 1 + 1.8*y*methods.np.sin(x) - y**2

x0 = 0
y0 = 0
x_end = 6
h = 0.1

x1, y1, h = methods.runge_kutta(x0, y0, x_end, func, h, True)
x1_halved, y1_halved = methods.runge_kutta(x0, y0, x_end, func, h/2, False)

x2, y2 = methods.adams(x1[:4], y1[:4], x_end, func, h)
x2_halved, y2_halved = methods.adams(x1_halved[:4], y1_halved[:4], x_end, func, h/2)

e1 = methods.evaluate_error_runge(y1, y1_halved, 4)
e2 = methods.evaluate_error_runge(y2, y2_halved, 4)

print(f"   N x        Runge-Kutta  e1         Adams       e2")
for i in range(len(x1)):
    print(f" {i:>3} {round(x1[i], 5):<6}   {y1[i]:8.6f}    {e1[i]:8.1e}    {y2[i]:8.6f}   {e2[i]:8.1e}")

fig = plt.gcf() # to be able to change window title
fig.canvas.set_window_title("Розв'язок")
plt.plot(x1, y1, 'b', label = "Метод Рунге-Кутта")
plt.plot(x2, y2, 'y', label = "Метод Адамса")
plt.legend(loc="best")
plt.show()

fig = plt.gcf() # to be able to change window title
fig.canvas.set_window_title("Похибка")
plt.plot(x1, e1, 'b', label = "Похибка методу Рунге-Кутта")
plt.plot(x2, e2, 'y', label = "Похибка методу Адамса")
plt.legend(loc="best")
plt.show()
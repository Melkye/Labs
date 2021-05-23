import numpy as np

def runge_kutta(x0, y0, x_end, func, h, eval_theta):
    x = [x0]
    y = [y0]
    n_sections = int((x_end - x[0])/h)  # int to use as index
    for i in range(n_sections):
        K1 = func(x[i], y[i])
        K2 = func(x[i] + h/2, y[i] + h*K1/2)
        K3 = func(x[i] + h/2, y[i] + h*K2/2)
        K4 = func(x[i] + h, y[i] + h*K3)

        delta_y = (h/6)*(K1 + 2*K2 + 2*K3 + K4)
        y.append(y[i] + delta_y)
        x.append(x[i] + h)
        #if eval_theta:
        #    if np.abs((K2-K3)/(K1-K2)) > 0.025:
        #        print(f"splitting h = {h:6}, in half, because theta = {np.abs((K2-K3)/(K1-K2)):.2}")
        #        x, y, h = runge_kutta(x0, y0, x_end, func, h/2, True)
        #        break
    if eval_theta:
        return x, y, h
    else:
        return x, y


def adams(x0, y0, x_end, func, h):
    x = x0[:]                                    
    y = y0[:]
    are_results_different = True
    n_sections = int((x_end - x[0])/h)

    for i in range(3, n_sections, 1):
        x.append(x[i] + h)
        delta_y = (h/24)*(55*func(x[i], y[i]) - 59*func(x[i-1], y[i-1]) \
            + 37*func(x[i-2], y[i-2]) - 9*func(x[i-3], y[i-3]))
        y_ex = y[i] + delta_y

        y.append(y_ex)
        if are_results_different:
            delta_y = (h/24)*(9*func(x[i+1], y_ex) + 19*func(x[i], y[i]) \
            - 5*func(x[i-1], y[i-1]) + func(x[i-2], y[i-2]))
            y_in = y[i] + delta_y
            y.pop()
            y.append(y_in)

        if np.abs(y_ex - y_in) <= 0.0000001:
            are_results_different = False
    return x, y

def evaluate_error_runge(y_h, y_halved_h, error_order):
    e = []
    for i, j in zip(range(len(y_h) + 1), range(0, len(y_halved_h) + 1, 2)):
        error_i = np.abs(y_h[i] - y_halved_h[j])/(2**error_order - 1)
        e.append(error_i)
    return e
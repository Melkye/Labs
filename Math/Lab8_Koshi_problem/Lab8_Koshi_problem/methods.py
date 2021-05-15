import numpy as np

def func(x, y):
    return 1 + 1.8*y*np.sin(x) - y**2

def runge_kutta(x0, y0, x_end, func, h):

    ## for step h
    #x = [x0]
    #y = [y0]
    #n = int((x_end - x0)/h + 1)  # +1 to include x0, int to use as index
    #for i in range(n + 1):  # +1 to include the end
    #    K1 = func(x[i], y[i])
    #    K2 = func(x[i] + h/2, y[i] + h*K1/2)
    #    K3 = func(x[i] + h/2, y[i] + h*K2/2)
    #    K4 = func(x[i] + h, y[i] + h*K3)

    #    #    h /= 2
    #    #    K1 = func(x[i], y[i])
    #    #    K2 = func(x[i] + h/2, y[i] + h*K1/2)
    #    #    K3 = func(x[i] + h/2, y[i] + h*K2/2)
    #    #    K4 = func(x[i] + h, y[i] + h*K3)
    #    delta_y = (h/6)*(K1 + 2*K2 + 2*K3 + K4)
    #    y.append(y[i] + delta_y)
    #    x.append(x[i] + h)
    #    if np.abs((K2-K3)/(K1-K2)) > 0.025:
    #        print("shit")
    #        x = [x0]
    #        y = [y0]
    #        h /= 2
    #        n = int((x_end - x0)/h + 1)
    #        i = 0
    x1, y1, h = runge_kutta_iteration(x0, y0, x_end, func, h, 1)
    # for step h/2 - to evaluate error
    x2 = [x0]
    y2 = [y0]
    n2 = int((x_end - x0)/(h/2)) + 1  # +1 to include x0
    #for i in range(n2 + 1):  # +1 to include the end, int to use as index
    #    K1 = func(x2[i], y2[i])
    #    K2 = func(x2[i] + h/2, y2[i] + h*K1/2)
    #    K3 = func(x2[i] + h/2, y2[i] + h*K2/2)
    #    K4 = func(x2[i] + h, y2[i] + h*K3)
    #    #while np.abs((K2-K3)/(K1-K2)) > 0.025:
    #    #    h /= 2
    #    #    K1 = func(x[i], y[i])
    #    #    K2 = func(x[i] + h/2, y[i] + h*K1/2)
    #    #    K3 = func(x[i] + h/2, y[i] + h*K2/2)
    #    #    K4 = func(x[i] + h, y[i] + h*K3)
    #    delta_y = (h/6)*(K1 + 2*K2 + 2*K3 + K4)
    #    y2.append(y2[i] + delta_y)
    #    x2.append(x2[i] + h)
    x2, y2 = runge_kutta_iteration(x0, y0, x_end, func, h/2, 2)

    #evaluating error
    e = [0]
    for i, j in zip(range(len(x1) + 1), range(0, len(x2) + 1, 2)):
        error_i = np.abs(y1[i] - y2[j])/15
        e.append(error_i)
        print(str(e))
    return x1, y1, e

#def adams(x0, y0, h,)

def runge_kutta_iteration(x0, y0, x_end, func, h, step): # necessary to check for '> 0.025' condition only
        # for step h                                     # on during the iteration with step h
    x = [x0]
    y = [y0]
    n = int((x_end - x0)/h + 1)  # +1 to include x0, int to use as index
    for i in range(n + 1):  # +1 to include the end
        K1 = func(x[i], y[i])
        K2 = func(x[i] + h/2, y[i] + h*K1/2)
        K3 = func(x[i] + h/2, y[i] + h*K2/2)
        K4 = func(x[i] + h, y[i] + h*K3)

        delta_y = (h/6)*(K1 + 2*K2 + 2*K3 + K4)
        y.append(y[i] + delta_y)
        x.append(x[i] + h)
        if step == 1:
            if np.abs((K2-K3)/(K1-K2)) > 0.025:
                print("shit", str(h), str(y[i]), str(np.abs((K2-K3)/(K1-K2))))
                x, y, h = runge_kutta_iteration(x0, y0, x_end, func, h/2, 1)
                break
    if step == 1:
        return x, y, h
    else:
        return x, y
            

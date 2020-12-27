import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x ** 3 - 2 * x + 1


def three_points_interpolation(x1, x2, x3, threshold, f):
    xs = np.inf

    while True:
        A = np.array(([x1 ** 2, x1, 1], [x2 ** 2, x2, 1], [x3 ** 2, x3, 1]))
        A_inv = np.linalg.inv(A)
        b = np.array([f(x1), f(x2), f(x3)])

        x = np.matmul(A_inv, b)  # x = [a; b; c], Coefficients of parabola y=a^2x+bx+c

        xs_new = - x[1] / (2 * x[0])  # x_star = -b/2a
        if abs(xs - xs_new) < threshold:
            return xs_new
        xs = xs_new

        if f(xs) < f(x2):
            if xs < x2:
                x1, x2, x3 = x1, xs, x2
            else:
                x1, x2, x3 = x2, xs, x3
        else:
            if xs < x2:
                x1, x2, x3 = xs, x2, x3
            else:
                x1, x2, x3 = x1, x2, xs


def three_points_interpolation_plot(x1, x2, x3, threshold, f):
    _x = np.arange(x1, x3, 0.01)
    _y = f(_x)
    pause_interval = 0.5
    plt.ion()

    xs = np.inf

    while True:
        plt.clf()
        plt.plot(_x, _y)
        plt.plot(x1, f(x1), "rx")
        plt.plot(x2, f(x2), "rx")
        plt.plot(x3, f(x3), "rx")
        plt.pause(pause_interval)

        A = np.array(([x1 ** 2, x1, 1], [x2 ** 2, x2, 1], [x3 ** 2, x3, 1]))
        A_inv = np.linalg.inv(A)
        b = np.array([f(x1), f(x2), f(x3)])

        x = np.matmul(A_inv, b)  # x = [a; b; c], Coefficients of parabola y=a^2x+bx+c

        xs_new = - x[1] / (2 * x[0])  # x_star = -b/2a

        _py = x[0] * _x ** 2 + x[1] * _x + x[2]
        plt.plot(_x, _py, "r")
        plt.pause(pause_interval)

        plt.plot(xs_new, f(xs_new), "rx")
        plt.axvline(xs_new, color="red")
        plt.pause(pause_interval)

        # stop condition
        if abs(xs - xs_new) < threshold:
            plt.pause(1)
            plt.ioff()
            return xs_new
        xs = xs_new

        if f(xs) < f(x2):
            if xs < x2:
                x1, x2, x3 = x1, xs, x2
            else:
                x1, x2, x3 = x2, xs, x3
        else:
            if xs < x2:
                x1, x2, x3 = xs, x2, x3
            else:
                x1, x2, x3 = x1, x2, xs


if __name__ == '__main__':
    print(three_points_interpolation_plot(0, 1, 3, 0.01, f))

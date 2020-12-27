import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x ** 2 - 6 * x + 2


def extrapolation_interpolation(x, h, f):
    if f(x) < f(x + h) and f(x) < f(x - h):
        return sorted([x - h, x, x + h])
    else:
        h *= -1 if f(x) < f(x + h) else 1
        while f(x) >= f(x + h):
            x = x + h
            h *= 2
        x1 = x - h / 2
        x2 = x
        x3 = x + h
        xs = x + h / 2

        if f(x2) < f(xs):
            x1, x2, x3 = x1, x2, xs
        else:
            x1, x2, x3 = x2, xs, x3
        return sorted([x1, x2, x3])


def extrapolation_interpolation_plot(x, h, f):
    _x = np.arange(0, 6, 0.01)
    _y = f(_x)

    pause_interval = 0.2
    plt.ion()

    plt.plot(_x, _y)
    plt.axvline(x, color="red")
    plt.plot(x, f(x), "rx")
    plt.pause(pause_interval)

    if f(x) < f(x + h) and f(x) < f(x - h):
        plt.axvline(x - h, color="red")
        plt.axvline(x + h, color="red")
        plt.plot(x - h, f(x - h), "rx")
        plt.plot(x + h, f(x + h), "rx")
        plt.pause(1)
        plt.ioff()

        return sorted([x - h, x, x + h])
    else:
        h *= -1 if f(x) < f(x + h) else 1
        while f(x) >= f(x + h):
            plt.axvline(x + h, color="red")
            plt.plot(x + h, f(x + h), "rx")
            plt.pause(pause_interval)
            x = x + h
            h *= 2

        plt.axvline(x + h, color="red")
        plt.plot(x + h, f(x + h), "rx")
        plt.pause(pause_interval)

        x1 = x - h / 2
        x2 = x
        x3 = x + h
        xs = x + h / 2

        plt.clf()
        plt.plot(_x, _y)
        plt.axvline(x1, color="green")
        plt.axvline(x2, color="green")
        plt.axvline(x3, color="green")
        plt.axvline(xs, color="green")
        plt.plot(x1, f(x1), "gx")
        plt.plot(x2, f(x2), "gx")
        plt.plot(x3, f(x3), "gx")
        plt.plot(xs, f(xs), "gx")
        plt.pause(1)

        if f(x2) < f(xs):
            x1, x2, x3 = x1, x2, xs
        else:
            x1, x2, x3 = x2, xs, x3

        plt.clf()
        plt.plot(_x, _y)
        plt.axvline(x1, color="green")
        plt.axvline(x2, color="green")
        plt.axvline(x3, color="green")
        plt.plot(x1, f(x1), "gx")
        plt.plot(x2, f(x2), "gx")
        plt.plot(x3, f(x3), "gx")

        plt.pause(1)
        plt.ioff()

        return sorted([x1, x2, x3])


if __name__ == '__main__':
    print(extrapolation_interpolation_plot(1, 0.1, f))

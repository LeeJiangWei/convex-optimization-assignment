import math
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x ** 2


def golden_section(a, b, threshold, f):
    lam = (math.sqrt(5) - 1) / 2  # 0.618

    x1 = a + (1 - lam) * (b - a)
    x2 = a + lam * (b - a)

    while b - a > threshold:
        if f(x1) > f(x2):
            a = x1
            x1 = x2
            x2 = a + lam * (b - a)
        else:
            b = x2
            x2 = x1
            x1 = a + (1 - lam) * (b - a)
    return [a, b]


def golden_section_plot(a, b, threshold, f):
    lam = (math.sqrt(5) - 1) / 2  # 0.618
    x1 = a + (1 - lam) * (b - a)
    x2 = a + lam * (b - a)

    _x = np.arange(a, b, 0.01)
    _y = f(_x)
    pause_interval = 0.1

    def draw():
        plt.clf()
        plt.plot(_x, _y)
        plt.axvline(a, color="red")
        plt.axvline(b, color="red")
        plt.plot(a, f(a), "rx")
        plt.plot(b, f(b), "rx")
        plt.pause(pause_interval)

    plt.ion()
    draw()

    while b - a > threshold:
        if f(x1) > f(x2):
            a = x1
            x1 = x2
            x2 = a + lam * (b - a)

            draw()
        else:
            b = x2
            x2 = x1
            x1 = a + (1 - lam) * (b - a)

            draw()

    plt.pause(1)
    plt.ioff()

    return [a, b]


if __name__ == '__main__':
    print(golden_section_plot(-5, 5, 1e-2, f))

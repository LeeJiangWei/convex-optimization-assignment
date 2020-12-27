from extrapolation_interpolation import extrapolation_interpolation, extrapolation_interpolation_plot
from golden_section import golden_section, golden_section_plot
from three_points_interpolation import three_points_interpolation, three_points_interpolation_plot

import numpy as np


def f(x):
    return (2 * x - 3) * np.sin(x)


if __name__ == '__main__':
    threshold = 1e-3
    x1, x2, x3 = extrapolation_interpolation_plot(4, 0.2, f)
    print("Founded 3 points: ", x1, x2, x3)
    g = golden_section_plot(x1, x3, threshold, f)
    print("Golden split min interval: ", g)
    t = three_points_interpolation_plot(x1, x2, x3, threshold, f)
    print("Three points interpolation min: ", t)

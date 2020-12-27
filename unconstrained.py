import numpy as np
import time

N = 1000
C = 100
D = 100

H = np.eye(N) * (1 + C + D)
H[0, 0], H[1, 1] = 1, 1 + C
H[-1, -1], H[-2, -2] = D, C + D
H *= 2  # hessian matrix of f
H_INV = np.linalg.inv(H)


def f(x: np.array):  # DQDRTIC function
    res = 0
    for i in range(N - 2):
        res += x[i] ** 2 + C * x[i + 1] ** 2 + D * x[i + 2] ** 2
    return res


def g(x: np.ndarray) -> np.ndarray:  # gradient
    res = (1 + C + D) * x

    res[0], res[1] = x[0], (1 + C) * x[1]
    res[-1], res[-2] = D * x[-1], (C + D) * x[-2]
    res *= 2

    return res.reshape([N, 1])


def bcd(x0, epsilon=1e-2):  # 坐标轮换法
    I = np.eye(N)
    x = x0[:]

    num_iter = 0

    precision = np.inf
    while precision > epsilon:
        x_temp = x
        for n in range(N):
            gx = g(x)
            d = - I[:, [n]]
            λ = - (gx.T @ d) / (d.T @ H @ d)
            x = x + λ * d
        precision = np.linalg.norm(x - x_temp)
        num_iter += 1

    return x, num_iter


def gd(x0, epsilon=1e-1, method=0):
    """
    :param x0:
    :param epsilon:
    :param method: 最速下降法=0, 阻尼牛顿法=1, 拟牛顿法=2
    :return:
    """
    x = x0[:]
    gx = g(x0)
    A = np.eye(N)
    x_temp, gx_temp = None, None

    num_iter = 0

    presicion = np.linalg.norm(gx)
    while presicion > epsilon:
        if method == 0:
            d = -gx
            λ = (gx.T @ gx) / (gx.T @ H @ gx)
        elif method == 1:
            d = -H_INV @ gx
            λ = - (gx.T @ d) / (d.T @ H @ d)
        elif method == 2:
            if x_temp is not None and gx_temp is not None:
                s = x - x_temp
                y = gx - gx_temp
                A += (s @ s.T) / (s.T @ y) - (A @ y @ y.T @ A) / (y.T @ A @ y)
            x_temp, gx_temp = x, gx

            d = - A @ gx
            λ = - (gx.T @ d) / (d.T @ H @ d)

        x = x + λ * d
        gx = g(x)
        presicion = np.linalg.norm(gx)
        num_iter += 1
    return x, num_iter


if __name__ == '__main__':
    x0 = np.full([N, 1], 3)
    ε = 1e-2
    t0 = time.time()
    r, nr = bcd(x0, epsilon=ε)
    t1 = time.time()
    print(nr, t1 - t0, f(r))
    for i in range(3):
        t0 = time.time()
        r, nr = gd(x0, epsilon=ε, method=i)
        t1 = time.time()
        print(nr, t1 - t0, f(r))

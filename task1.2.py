import numpy as np
import matplotlib.pyplot as plt


def test_function(x):
    return np.sin(2 * np.pi * x)


def exact_derivative(x):
    return 2 * np.pi * np.cos(2 * np.pi * x)


def first_order_fd(f, x, h):
    return (f(x + h) - f(x)) / h


def first_order_bd(f, x, h):
    return (f(x) - f(x - h)) / h


def first_order_cd(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def second_order_cd(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)


spacings = [0.1, 0.01, 0.001]
precisions = [np.float32, np.float64]

for spacing in spacings:
    x = np.linspace(0, 1, int(1 / spacing) + 1)
    plt.figure(figsize=(10, 6))
    plt.plot(x, exact_derivative(x), 'k--', label='Exact')

    for precision in precisions:
        derivative_fd = first_order_fd(
            test_function, x, spacing).astype(precision)
        derivative_bd = first_order_bd(
            test_function, x, spacing).astype(precision)
        derivative_cd = first_order_cd(
            test_function, x, spacing).astype(precision)
        derivative_exact = exact_derivative(x).astype(precision)

        error_fd = np.abs(derivative_fd - derivative_exact)
        print(error_fd)

    plt.show()

import matplotlib.pyplot as plt
import numpy as np


def build_plot(x_coefficients: list, degree: int):
    # Create the vectors X and Y
    x = np.array(range(-5, 5))
    plt.axhline(color='b', linestyle='-')
    plt.axvline(color='b', linestyle='-')

    y = 0
    for i in range(degree + 1):
        y += x_coefficients[i] * x ** i
    plt.plot(x, y, color='r')
    plt.show()

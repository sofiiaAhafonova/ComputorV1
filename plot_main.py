import matplotlib.pyplot as plt
import numpy as np
import equation
import sys


def build_plot(x_coefficients: list, degree: int):
    x = np.array(range(-5, 5))
    plt.axhline(color='b', linestyle='-')
    plt.axvline(color='b', linestyle='-')

    y = 0
    try:
        for i in range(degree + 1):
            y += x_coefficients[i] * x ** i
        plt.plot(x, y, color='r')
        plt.show()
    except :
        print("Can't build plot for this equation")


def main():
    args = sys.argv
    ac = len(args)
    if ac == 2:
        eq = equation.Equation(args[1])
        if eq.success:
            build_plot(eq.x, eq.degree)
    elif ac == 1:
        print('Please enter your equation')
    else:
        print('Please enter only one equation')


if __name__ == '__main__':
    main()


import sys
import equation
from plot import build_plot
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

import sys
import equation


def main():
    args = sys.argv
    ac = len(args)
    if ac == 2:
        equation.Equation(args[1])
    elif ac == 1:
        print('Please enter your equation')
    else:
        print('Please enter only one equation')


if __name__ == '__main__':
    main()

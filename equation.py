from math_func import ft_abs, ft_sqrt
import re


class Equation(object):
    allowed_symbols = ['+', '-', '*', '=']
    pattern = r'^X(\^(\d)+)?$'
    max_degree = 10

    def __init__(self, str_equation):
        self.x = [0] * (self.max_degree + 1)
        self.solver = [self._zero_degree, self._linear, self._quadratic]
        self.degree = 0
        self.success = True
        try:
            self._parse(str_equation)
            self._solve()
        except ValueError as v:
            print(f'\033[31m{v}\033[39m')
            self.success = False

    def _parse_degree(self, arg, mult):
        if not mult:
            return self.degree
        num = int(arg)
        self.degree = num if num > self.degree else self.degree
        if self.degree > self.max_degree:
            return -1
        return num

    def _parse(self, str_equation: str):
        for s in self.allowed_symbols:
            str_equation = str_equation.replace(s, f' {s} ')
        str_equation = str_equation.replace('X', ' X')
        if str_equation.count('=') != 1:
            raise ValueError('Should be one = sign in equation')
        equation = str_equation.split()
        mult, sign, right = 1, 1, False
        i, n = 0, len(equation)
        while i < len(equation):
            e = equation[i]
            if e.isdigit() or e.replace('.', '', 1).isdigit():
                mult = float(e) * sign
                if n - i >= 3 and equation[i + 1] == '*' and re.match(self.pattern, equation[i + 2]):
                    i += 2
                elif n - i >= 2 and re.match(self.pattern, equation[i + 1]):
                    i += 1
                elif n - i >= 2 and equation[i + 1] in ['+', '-', '='] or n - i == 1:
                    equation[i] = 'X^0'
                else:
                    raise ValueError('Invalid symbol instead or after coefficient')
                if n - i != 1 and equation[i + 1] not in ['+', '-', '=']:
                    raise ValueError('Invalid symbol instead or after coefficient')
                e = equation[i]
                e = '1' if e == 'X' else e[2:]
                j = self._parse_degree(e, mult)
                if j == -1:
                    break
                self.x[j] += mult
            elif e in ['-', '+', '='] and n - i >= 2 \
                    and (re.match(self.pattern, equation[i + 1])
                         or equation[i + 1].isdigit()
                         or equation[i + 1].replace('.', '', 1).isdigit()):
                if e == '=':
                    right = True
                    sign = -1
                elif e == '-' and not right or e == '+' and right:
                    sign = -1
                else:
                    sign = 1

            elif re.match(self.pattern, e):
                e = '1' if e == 'X' else e[2:]
                j = self._parse_degree(e, 1)
                if j == -1:
                    break
                self.x[j] += 1
            else:
                raise ValueError('Invalid equation')
            i += 1

    def _print_sign(self, x):
        return '-' if x < 0 else '+'

    def _reduce(self):
        res = f'{self.x[0]:g} * X^0'
        for i in range(1, self.degree + 1):
            res += f' {self._print_sign(self.x[i])} {ft_abs(self.x[i]):g} * X^{i}'
        return res + ' = 0'

    def _quadratic(self):
        discriminant = self.x[1] * self.x[1] - 4 * self.x[2] * self.x[0]
        print(f'Discriminant is {discriminant}')

        if discriminant == 0:
            print("Discriminant is 0, the solution is:")
            print(-self.x[1] / (2 * self.x[2]))
        else:
            if discriminant < 0:
                print("Discriminant is strictly negative, the two solutions are:")
                i = ft_sqrt(-discriminant) / (2 * self.x[2])
                x_1 = (-self.x[1] / (2 * self.x[2]), self._print_sign(-i), ft_abs(i))
                x_2 = (-self.x[1] / (2 * self.x[2]), self._print_sign(i), ft_abs(i))
                print("\033[34m(-b - \u221ad) / (2 * a) = \033[32m{:g} {} {:g}i\033[39m"
                      .format(x_1[0], x_1[1], x_1[2]))
                print("\033[34m(-b + \u221ad) / (2 * a) = \033[32m{:g} {} {:g}i\033[39m"
                      .format(x_2[0], x_2[1], x_2[2]))
            else:
                print("Discriminant is strictly positive, the two solutions are:")
                x_1 = (-self.x[1] - ft_sqrt(discriminant)) / (2 * self.x[2])
                x_2 = (-self.x[1] + ft_sqrt(discriminant)) / (2 * self.x[2])
                print("\033[34m(-b - \u221ad) / (2 * a) = \033[32m{:g}\033[39m".format(x_1))
                print("\033[34m(-b + \u221ad) / (2 * a) = \033[32m{:g}\033[39m".format(x_2))

    def _linear(self):
        res = - self.x[0] / self.x[1]
        print('The solution is:')
        print(res)

    def _zero_degree(self):
        if self.x[0] == 0:
            print('All the real numbers are solution')
        else:
            print('There is no solution of equation')

    def _print_degree(self):
        print(f'Polynomial degree: {self.degree}')

    def _print_reduce(self):
        print(f'Reduced form: {self._reduce()}')

    def _solve(self):
        if self.degree > self.max_degree:
            print('\033[34mEquation degree is too high to reduce it\033[39m')
        else:
            self._print_reduce()
        self._print_degree()
        if self.degree > 2:
            print('The polynomial degree is strictly greater than 2, I can\'t solve')
        else:
            self.solver[self.degree]()

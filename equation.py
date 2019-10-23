from math_func import ft_abs, ft_sqrt
import re


class Equation(object):
    allowed_symbols = ['+', '-', '*', '=']
    pattern = r'^X\^\d+$'
    max_degree = 10

    def __init__(self, str_equation):
        self.x = [0] * (self.max_degree + 1)
        self.solver = [self._zero_degree, self._linear, self._quadratic]
        self.degree = 0
        try:
            self._parse(str_equation)
            self._solve()
        except ValueError:
            print('Invalid equation')

    def _parse(self, str_equation: str):
        for s in self.allowed_symbols:
            str_equation = str_equation.replace(s, f' {s} ')
        equation = str_equation.split()
        mult, sign = 1, 1
        i = 0
        while i < len(equation):
            e = equation[i]
            if e.isdigit() or e.replace('.', '', 1).isdigit():
                mult = float(e) * sign
                if equation[i + 1] != '*' or not re.match(self.pattern, equation[i + 2]):
                    raise ValueError()
                e = equation[i + 2][2:]
                if not e.isdigit():
                    raise ValueError()
                j = int(e)
                self.degree = j if j > self.degree and mult else self.degree
                if self.degree > self.max_degree:
                    break
                self.x[j] += mult
                i += 2
            elif e in ['-', '+']:
                sign *= -1 if e == '-' else 1
            elif e == '=':
                sign = -1
            elif re.match(self.pattern, e):
                e = e[2:]
                if not e.isdigit():
                    raise ValueError()
                j = int(e)
                self.degree = j if j > self.degree else self.degree
                if self.degree > self.max_degree:
                    break
                self.x[j] += 1
            else:
                raise ValueError()
            i += 1

    def _print_sign(self, x):
        return '-' if x < 0 else '+'

    def _reduce(self):
        self._count_degree()
        res = f'{self.x[0]:g} * X^0'
        for i in range(1, self.degree + 1):
            res += f' {self._print_sign(self.x[i])} {ft_abs(self.x[i]):g} * X^{i}'
        return res + ' = 0'

    def __str__(self):
        return self._reduce()

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
                print("\033[34m(-b - (d ** 0.5)) / (2 * a) = \033[32m{:g} {} {:g} * i\033[39m"
                      .format(x_1[0], x_1[1], x_1[2]))
                print("\033[34m(-b + (d ** 0.5)) / (2 * a) = \033[32m{:g} {} {:g} * i\033[39m"
                      .format(x_2[0], x_2[1], x_2[2]))
            else:
                print("Discriminant is strictly positive, the two solutions are:")
                x_1 = (-self.x[1] - ft_sqrt(discriminant)) / (2 * self.x[2])
                x_2 = (-self.x[1] + ft_sqrt(discriminant)) / (2 * self.x[2])
                print("\033[34m(-b - (d ** 0.5)) / (2 * a) = \033[32m{:g}\033[39m".format(x_1))
                print("\033[34m(-b + (d ** 0.5)) / (2 * a) = \033[32m{:g}\033[39m".format(x_2))

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

    def _count_degree(self):
        self.degree = len(self.x) - 1
        while not self.x[self.degree]:
            self.degree -= 1

    def _solve(self):
        self._print_reduce()
        self._print_degree()
        if self.degree > 2:
            print('The polynomial degree is strictly greater than 2, I can\'t solve')
        else:
            self.solver[self.degree]()


Equation('5 * X^0 + 4 * X^1 - 9.3 * X^2 + 1 * X^3 =1 * X^0')

print()
Equation("5 * X^0 + 4 * X^1 = 4 * X^0")

print()

Equation('5 * X^0 + 4 * X^1 + X^2 = 0 * X^0')

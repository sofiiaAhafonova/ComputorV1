from math_func import ft_abs


class Equation(object):
    allowed_symbols = ['+', '-', '*', '=']

    def __init__(self, str_equation):
        self.x = [0] * 3
        self._parse(str_equation)

    def _parse(self, str_equation: str):
        equation = str_equation.split()
        mult, sign = 1, 1
        i = 0
        while i < len(equation):
            e = equation[i]
            if e.isdigit() or e.replace('.', '', 1).isdigit():
                mult = float(e) * sign
                if equation[i + 1] != '*' or equation[i + 2] not in ['X^0', 'X^1', 'X^2']:
                    raise ValueError('Invalid input')
                e = equation[i + 2]
                for j in range(3):
                    if e.count(str(j)):
                        self.x[j] += mult
                        break
                i += 2
            elif e in ['-', '+']:
                sign *= -1 if e == '-' else 1
            elif e == '=':
                sign = -1
            else:
                print(e)
                raise ValueError('Invalid input')
            i += 1

    def _reduce(self):
        def sign(x):
            return '-' if x < 0 else '+'

        return f'{self.x[0]} * X^0 {sign(self.x[0])} {ft_abs(self.x[1])} * X^1 ' \
               f'{sign(self.x[2])} {ft_abs(self.x[2])} * X^2 = 0'

    def __str__(self):
        return self._reduce()


eq = Equation('5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0')
print(eq)
print(Equation("5 * X^0 + 4 * X^1 = 4 * X^0"))

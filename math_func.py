import sys

def ft_abs(a):
    return a if a >= 0 else -a


def int_div(dividend, divisor):
    sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
    dividend = ft_abs(dividend)
    divisor = ft_abs(divisor)
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    return sign * quotient


def float_div(dividend, divisor):
    pass


def ft_div(dividend, divisor):
    pass


def ft_mod(dividend, divisor):
    pass


def ft_pow(x, a):
    if a == 0:
        return 1
    res = 1
    for _ in range(a, 0, -1):
        res *= x
    return res if a > 0 else ft_div(x, res)


PRECISION = 10 ** -10


def float_sqrt(n, lo, hi):
    while True:
        mid = (lo + hi) / 2
        mul = mid * mid
        if mul == n or ft_abs(mul - n) < PRECISION:
            return mid
        if mul < n:
            lo = mid
        else:
            hi = mid


def ft_sqrt(n):
    if n < 0:
        raise ValueError('sqrt function works only with non-negative values')
    if n == 0 or n == 1:
        return n
    i = 1
    while True:
        if i * i == n:
            return i
        elif i * i > n:
            return float_sqrt(n, i - 1, i)
        i += 1


def main():
    av = sys.argv
    ac = len(av)
    print(av, ac)
    import math
    print(ft_sqrt(211111111111111.5))
    print(math.sqrt(2111111111111.5))


if __name__ == '__main__':
    main()
bad_pow = "⁰¹²³⁴⁵⁶⁷⁸⁹ⁿ⅟¼½¾⅓⅔⅕⅖⅗⅘⅙⅚⅐⅛⅜⅑⅞⅝⅒"


def str1_in_str2(str1, str2):
    for char in str1:
        if char in str2:
            return True

    return False


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    elif n >= 2 and n % 2 == 0:  # if n is even and positive
        k = n / 2
        fk = fib(k)
        return (2 * fib(k - 1) + fk) * fk

    elif n >= 2:  # if n is odd and positive
        k = (n + 1) / 2
        fk1 = fib(k - 1)
        fk2 = fib(k)
        return fk2 * fk2 + fk1 * fk1

    else:                           # if n is negative
        if abs(n) % 2 == 0:         # if n is even, its fib(n) is the negative value for fib(n) with absolute value of n
            return fib(abs(n)) * -1
        else:                       # if n is odd, its fib(n) is the fib(n) value with absolute n
            return fib(abs(n))

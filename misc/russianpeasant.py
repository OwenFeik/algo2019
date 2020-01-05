
def multiply(a, b):
    return b if a == 1 else multiply(a // 2, b * 2) + (b if (a % 2) == 1 else 0)


def multiply_i(a, b):
    s = 0
    while a > 1:

        if a % 2 == 1:
            s += b

        a = a // 2
        b = b * 2

    s += b

    return s


print(multiply_i(15, 13))

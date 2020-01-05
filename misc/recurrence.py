# # t(n) = t(n - 1) + 1

# def t(n):
#     if n > 0:
#         t(n - 1)
#         print(n)

# t(12)

# # T(n) = T(n - 1) + 1
# #
# #         / 0, n = 0
# # T(n) = {
# #         \ T(n - 1) + 1, n > 0
# #
# # Or, use a call tree.

import math

def func(n):
    steps = 0
    if n > 0:
        i = 1
        while i < n:
            steps += 1
            i *= 2
        steps += func(n - 1)
    return steps

for i in range(1, 100):
    print(f'n^2: {i ** 2}, nlog(n): {round(i * math.log(i), 0)}, f(n): {func(i)}')

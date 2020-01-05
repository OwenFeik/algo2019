from timeit import timeit

setup = 'import coins\nn = 2123\ndenoms = [1, 3, 4, 7, 9, 16]'

print(f'naive: {timeit("coins.get_change_naive(n, denoms)", setup, number = 100)}')
print(f'dynamic: {timeit("coins.get_change(n, denoms)", setup, number = 100)}')
# print(timeit("coins.get_change_coins_naive(n, denoms)", setup, number = 100))
# print(timeit("coins.get_change_coins(n, denoms)", setup, number = 100))

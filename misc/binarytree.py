import sys

#nth Catalan number: (2n)!/(n+1)!n!
#count(n) = sum count(k - 1)*count(n - k)

def build_binary_tree_r(n):
    return 1 if n in [0, 1] else sum([(build_binary_tree_r(k - 1) * build_binary_tree_r(n - k)) for k in range(1, n + 1)])

# def build_binary_tree_d(n, table = {0: 1, 1: 1}):
#     return table[n] if n in table else sum([(build_binary_tree_d(k - 1) * build_binary_tree_d(n - k)) for k in range(1, n + 1)])

build_binary_tree_d = lambda n, table = {0: 1, 1: 1}: table[n] if n in table else sum([(build_binary_tree_d(k - 1) * build_binary_tree_d(n - k)) for k in range(1, n + 1)])


# def build_binary_tree_d(n, table = {0: 1, 1: 1}):
#     if not n in table:
#         total = 0
#         for k in range(1, n + 1):
#             total += build_binary_tree(k - 1) * build_binary_tree(n - k)            
        
#         table[n] = total
#     return table[n]


if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 3

print(build_binary_tree_d(n))

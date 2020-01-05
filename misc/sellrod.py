def rod_price_recursive(length, prices):
    ps = []
    if length <= max(prices):
        ps.append([length])
    for l in range(1, min(length, max(prices))):
        ps.append(rod_price_recursive(length - l, prices) + [l])

    return max(ps, key = lambda k: sum([prices[r] for r in k]))

def rod_price_dynamic(length, prices, table = {}):
    if not length in table:
        ps = []
        if length <= max(prices):
            ps.append([length])
        for l in range(1, min(length, max(prices))):
            ps.append(rod_price_dynamic(length - l, prices) + [l])
        
        table[length] = max(ps, key = lambda k: sum([prices[r] for r in k]))
    return table[length]

import functools
@functools.lru_cache(maxsize = None)
def rod_price_memoized(length):
    return rod_price_recursive(length, prices)


from sys import argv
if len(argv) > 1:
    length = int(argv[1])
else:
    length = 16

prices = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20, 9: 24, 10: 30}
print(rod_price_dynamic(length, prices))

# Give change for amount n using the minimum number coins of
#   denominations 1, d2, d3, d4
# Let F(n) be the minumum number of coins.
# F(0) is therefore equal to 0.
# The amount n can be obtained by adding one coin of 
#   denomination dj to the amount n - dj for j = 1, 2 etc
#   Therfore we can consider all such denominations and select
#   the one minimizing F(n - dj) + 1
# Since 1 is constant, find the smallest F(n - dj) and add 1
#
# F(n) = min({F(n - dj)}) + 1 for n > 0
# F(0) = 0
#

import sys
sys.setrecursionlimit(100000)

from copy import copy

def get_change_naive(n, denoms):
    possibilities = []
    for d in denoms:
        if d == n:
            possibilities.append(1)
        elif d <= n:
            possibilities.append(get_change(n - d, denoms) + 1)
    
    return min(possibilities)

def get_change(n, denoms, table = {0: 0}):
    if n in table:
        return table[n]

    possibilities = []
    for d in denoms:
        if d == n:
            possibilities.append(1)
        elif d <= n:
            possibilities.append(get_change(n - d, denoms) + 1)
    table[n] = min(possibilities)

    return table[n]

def get_change_coins_naive(n, denoms):
    possibilities = []
    for d in denoms:
        if d == n:
            possibilities.append([d])
        elif d <= n:
            p = copy(get_change_coins_naive(n - d, denoms))
            p.append(d)
            possibilities.append(p)
    
    return min(possibilities, key = len)


def get_change_coins(n, denoms, table = {0: []}):
    if n in table:
        return table[n]

    ps = []
    for d in denoms:
        if d == n:
            ps.append([d])
        elif d <= n:
            p = copy(get_change_coins(n - d, denoms))
            p.append(d)
            ps.append(p)
    table[n] = min(ps, key = len)

    return table[n]

# Has overlapping sub problems, exhibits optimal substructure

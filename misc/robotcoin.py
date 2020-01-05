from random import random # Randomly place 0s and 1s on a grid
from copy import copy # Avoid mutating lists
import time # Compare efficiency of approaches

def max_coins(board, y = 0, x = 0): # Naive recursive approach
    if len(board) - 1 == y and len(board[0]) - 1 == x:
        return 0
    
    ps = []

    if not (len(board) - 1 == y):
        if board[y + 1][x] == 1:
            ps.append(max_coins(board, y + 1, x) + 1)
        else:
            ps.append(max_coins(board, y + 1, x))
    
    if not (len(board) - 1 == x):
        if board[y][x + 1] == 1:
            ps.append(max_coins(board, y, x + 1) + 1)
        else:
            ps.append(max_coins(board, y, x + 1))

    return max(ps)

def max_coins_dynamic(board, y = 0, x = 0, table = {}):
    if len(board) - 1 == y and len(board[0]) - 1 == x:
        return 0
    
    if (y, x) in table:
        return table[(y, x)]
    
    ps = []

    if not (len(board) - 1 == y):
        if board[y + 1][x] == 1:
            ps.append(max_coins_dynamic(board, y + 1, x) + 1)
        else:
            ps.append(max_coins_dynamic(board, y + 1, x))
    
    if not (len(board) - 1 == x):
        if board[y][x + 1] == 1:
            ps.append(max_coins_dynamic(board, y, x + 1) + 1)
        else:
            ps.append(max_coins_dynamic(board, y, x + 1))

    table[(y, x)] = max(ps)
    return table[(y, x)]

def start_max_coins_dynamic(board): # Dynamic implementation
    table = {}
    def max_coins_dynamic(board, y = 0, x = 0):
        if len(board) - 1 == y and len(board[0]) - 1 == x:
            return 0
        
        if (y, x) in table:
            return table[(y, x)]
        
        ps = []

        if not (len(board) - 1 == y):
            if board[y + 1][x] == 1:
                ps.append(max_coins_dynamic(board, y + 1, x) + 1)
            else:
                ps.append(max_coins_dynamic(board, y + 1, x))
        
        if not (len(board) - 1 == x):
            if board[y][x + 1] == 1:
                ps.append(max_coins_dynamic(board, y, x + 1) + 1)
            else:
                ps.append(max_coins_dynamic(board, y, x + 1))

        table[(y, x)] = max(ps)
        return table[(y, x)]

    max_coins_dynamic(board)
    return table

def start_max_coins_dynamic_path(board): # Dynamic implementation
    table = {}
    def max_coins_dynamic(board, x = 0, y = 0):
        if len(board) - 1 == y and len(board[0]) - 1 == x:
            return (0, [(x, y)])
        
        if (x, y) in table:
            coins, path = table[(x, y)]
            path = copy(path)
            path.append((x, y))
            return (coins, path)
        
        ps = []

        if not (len(board) - 1 == y): # Down
            coins, path = max_coins_dynamic(board, x, y + 1) 
            if board[y + 1][x] == 1: # If there is a coin down
                coins += 1
            path = copy(path)
            path.append((x, y))
            ps.append((coins, path))
        
        if not (len(board) - 1 == x): # Right
            coins, path = max_coins_dynamic(board, x + 1, y)
            if board[y][x + 1] == 1: # If there is a coin to the right
                coins += 1
            path = copy(path)
            path.append((x, y))
            ps.append((coins, path))

        table[(x, y)] = max(ps, key = lambda k: k[0])
        return table[(x, y)]

    path = max_coins_dynamic(board)[1]
    return table, path

def make_board(size = 10):
    board = [[0 if random() >= 0.1 else 1 for _ in range(size)] for _ in range(size)]
    return board

"""
This problem invites a dynamic approach. Therefore, a recursive stru


Base case: I am in the bottom right corner, the maximum number of coins is 0
otherwise, I want to go to max(max_coins(right), max_coins(down))

"""

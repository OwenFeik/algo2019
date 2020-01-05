from random import shuffle

class Board():
    def __init__(self, board = None, turn = 'X'):
        self.board = board if board is not None else [' '] * 9
        self.turn = turn

        self.victor = self.victory()
        if self.victor:
            self.children = None
        else:
            self.children = []
            for i in range(9):
                if self.board[i] == ' ':
                    child_board = self.board[:]
                    child_board[i] = self.turn
                    self.children.append(Board(child_board, 'X' if self.turn == 'O' else 'O'))
            shuffle(self.children) # make things a bit more interesting

        self.value = self._value()

    def _value(self):
        if self.children:
            if self.turn == 'X':
                return max([c.value for c in self.children])
            elif self.turn == 'O':
                return min([c.value for c in self.children])
        else:
            if self.victor == 'X':
                return 1
            elif self.victor == 'O':
                return -1
            else:
                return 0

    def victory(self):
        lines = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]
        for line in lines: 
            victor = self.check(*line)
            if victor:
                return victor
        
        return None

    def check(self, a, b, c):
        if self.board[a] == self.board[b] == self.board[c] != ' ':
            return self.board[a]
        else:
            return None

    def move(self):
        return max(self.children, key = lambda c: c.value)

def print_board(b):
    print(b[0], b[1], b[2])
    print(b[3], b[4], b[5])
    print(b[6], b[7], b[8])
    # print(b)

cpu = Board()

while True:
    cpu = cpu.move()
    print_board(cpu.board)
    if cpu.victor:
        print(f'{cpu.victor} wins!')
        break
    elif ' ' not in cpu.board:
        print('Draw!')
        break

    move = int(input('> '))
    board = cpu.board[:]
    board[move] = 'O'

    for c in cpu.children:
        if c.board == board:
            cpu = c


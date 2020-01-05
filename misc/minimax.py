from graph import Graph, Node
from display import DisplayGraph

class Board():
    def __init__(self, board, turn):
        self.board = board
        self.turn = turn
        self.winner = None

    def __str__(self):
        return ''.join(self.board)

    def get_moves(self):
        boards = []

        for i in range(9):
            if self.board[i] == '_':
                b = self.board[:]
                b[i] = self.turn

                boards.append(Board(b, 'O' if self.turn == 'X' else 'X'))

        return boards

    def check_victory(self):
        b = self.board
        lines = [
            set([b[0], b[1], b[2]]),
            set([b[3], b[4], b[5]]),
            set([b[6], b[7], b[8]]),
            set([b[0], b[4], b[8]]),
            set([b[2], b[4], b[6]]), 
            set([b[0], b[3], b[6]]), 
            set([b[1], b[4], b[7]]), 
            set([b[2], b[5], b[8]])
        ]

        if set(['X']) in lines:
            self.winner = 'X'
        elif set(['O']) in lines:
            self.winner = 'O'



start_boards = [['_', '_', '_', '_', 'X', '_', '_', '_', '_'], ['_', 'X', '_', '_', '_', '_', '_', '_', '_'], ['X', '_', '_', '_', '_', '_', '_', '_', '_']]
g = Graph(directed = True)

n = Node('_________')
n.explored = True
g.add_node(n)

for board in start_boards:
    b = Board(board, 'O')
    n = Node(str(b))
    n.board = b
    n.explored = False
    g.add_node(n)
    g.add_edge(('         ', str(b)))

depth = 0
while depth < 3:
    for n in [n for n in g.nodes if not n.explored]:
        for b in n.board.get_moves():
            if not g.has_node(str(b)):
                _n = Node(str(b))
                _n.board = b
                _n.board.check_victory()
                if _n.board.winner:
                    _n.explored = True
                    if _n.board.winner == 'X':
                        _n.colour = (0, 255, 0)
                        _n.value = 1
                    elif _n.board.winner == 'O':
                        _n.colour = (255, 0, 0)
                        _n.value = -1
                else:
                    _n.explored = False

                g.add_node(_n)
            if not g.has_edge((n.name, str(b))):
                g.add_edge((n.name, str(b)))

        n.explored = True
    
    depth += 1


for n in g.nodes:
    n.explored = False

s = '_________'

g.get_node(s).explored = True
g.get_neighbours('___')

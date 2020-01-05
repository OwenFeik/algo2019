from graph import Graph
from display import DisplayGraph
from math import inf

class Piece():
    def __init__(self, colour, x, y):
        self.colour = colour # W or B
        self.x = x # Coordinate on the board
        self.y = y

    def get_legal_moves(self, size): # Each move a knight can take
        return [m for m in [
            (self.x - 1, self.y - 2),
            (self.x + 1, self.y - 2),
            (self.x - 2, self.y - 1),
            (self.x + 2, self.y - 1),
            (self.x - 2, self.y + 1),
            (self.x + 2, self.y + 1),
            (self.x - 1, self.y + 2),
            (self.x + 1, self.y + 2)
        ] if 0 <= m[0] < size and 0 <= m[1] < size] # Only moves that are on the board are considered

class Board():
    def __init__(self, size, pieces = None, turn = 'W'):
        self.size = size
        self.pieces = pieces if pieces is not None else [Piece('B', 0, 0), Piece('B', size - 1, 0), Piece('W', 0, size - 1), Piece('W', size - 1, size - 1)] # Four knights
        self.turn = turn
    
    def __str__(self):
        return ''.join([''.join(line) for line in self.grid()]) # String such as "B.B...W.W" that shows the board layout

    def get_legal_steps(self):
        new_boards = []
        for p in [piece for piece in self.pieces if piece.colour == self.turn]: # For each piece of the current turn i.e. white pieces or black pieces
            for move in p.get_legal_moves(self.size): # For each move this piece could take
                if not move in [(p.x, p.y) for p in self.pieces]: # If the tile isn't occupied, create a new board to represent this state
                    new_boards.append(Board(self.size, [Piece(p.colour, move[0], move[1])] + [piece for piece in self.pieces if piece != p], 'B' if self.turn == 'W' else 'W'))
        return new_boards # List of board objects that represent possible next states

    def grid(self): # . or W/B for each tile on the grid
        grid = [['.' for _ in range(self.size)] for _ in range(self.size)]
        for p in self.pieces:
            grid[p.y][p.x] = p.colour
        return grid
    
    def print(self): # Relatively attractive printing of the board
        print('\n'.join([' '.join(line) for line in self.grid()]) + '\n')

starting_board = Board(3) # 3*3 board; 4*4 takes an extremely long time to run.
g = Graph(directed = True) # Directed graph because no states are reversible, because the turns are in a certain order.
g.add_node({'name': str(starting_board), 'board': starting_board, 'visited': False}) # Starting board state

source = 'B.B...W.W'
target = 'W.W...B.B'

unvisited = [g.nodes[source]]
while unvisited: # While there are unprocessed board states.
    for n in unvisited: # For each of these board states
        for b in n.board.get_legal_steps(): # For each possible board state from this state
            name = str(b)
            if not g.has_node(name): # Add it to the graph if it's not there
                g.add_node({'name': name, 'board': b, 'visited': False})
            g.add_edge(((str(n.board)), name)) # Add an edge to the state it was reached from
        n.visited = True # Mark this board state as processed
    unvisited = [n for n in g.nodes if not n.visited] # Find the newly added nodes

# Implementation of dijkstra's algorithm
unvisited = []
for n in g.nodes: 
    n.dist = inf
    n.prev = None
    unvisited.append(n)

g.nodes[source].dist = 0

while unvisited:
    n = min(unvisited, key = lambda k: k.dist)
    unvisited.remove(n)

    for o in g.get_neighbours(n):
        g.get_edge((n, o))
        alt = n.dist + 1 # Cost of edges is 1; i.e. 1 move
        if alt < o.dist:
            o.dist = alt
            o.prev = n

        if o.name == target: # When we find the target node
            path = [] # Re-construct path taken
            node = o
            path.append(o) # Starting from the target node we just found
            while node.prev:
                node.prev.colour = (200, 200, 0) # Mark these nodes yellow
                path.append(node.prev) # Add each to the path
                node = node.prev # Move backward through the chain

            path = reversed(path) # Reverse so we start from the beginning 
            for i, n in enumerate(path): # Print out each board state
                print(f'Move {i}:\n') # With move number
                n.board.print()
            unvisited = [] # Close while loop
            break

g.nodes[source].colour = (255, 0, 0) # Mark source
g.nodes[target].colour = (0, 255, 0) # and target

DisplayGraph(g, colour_theme = 'light', edge_width = 2).run() # Going to be messy, because there are a lot of possible states.

from graph import Graph, Node
from display import DisplayGraph

class Jugs:
    def __init__(self, a, b, c, size):
        self.a = a
        self.b = b
        self.c = c
        self.size = size

    def __str__(self):
        return f'[{self.a}] [{self.b}] [{self.c}]'

    def equals(self, other):
        return True if self.a == other.a and self.b == other.b and self.c == other.c else False

    def get_moves(self):
        opts = []
        if self.a < self.size[0]:
            if self.b > 0:
                change = min(abs(self.a - self.size[0]), self.b) 
                a = self.a + change  
                b = self.b - change
                c = self.c
                opts.append(Jugs(a, b, c, self.size))
            if self.c > 0:
                change = min(abs(self.a - self.size[0]), self.c)
                a = self.a + change 
                b = self.b
                c = self.c - change
                opts.append(Jugs(a, b, c, self.size))
        if self.b < self.size[1]:
            if self.a > 0:
                change = min(abs(self.b - self.size[1]), self.a)
                a = self.a - change
                b = self.b + change
                c = self.c
                opts.append(Jugs(a, b, c, self.size))
            if self.c > 0:
                change = min(abs(self.b - self.size[1]), self.c)
                a = self.a
                b = self.b + change
                c = self.c - change
                opts.append(Jugs(a, b, c, self.size))
        if self.c < self.size[2]:
            if self.a > 0:
                change = min(abs(self.c - self.size[2]), self.a)
                a = self.a - change
                b = self.b
                c = self.c + change
                opts.append(Jugs(a, b, c, self.size))
            if self.b > 0:
                change = min(abs(self.c - self.size[2]), self.b)
                a = self.a
                b = self.b - change
                c = self.c + change
                opts.append(Jugs(a, b, c, self.size))
        
        return opts



size = [8, 5, 3]
g = Graph(directed = True)

start = Jugs(size[0], 0, 0, size)
s = Node(str(start))
s.jugs = start
s.explored = False
s.prev = None
s.colour = (255, 0, 0)
g.add_node(s)

target = Jugs(size[0] / 2, size[0] / 2, 0, size)

found = False
while not found:
    for n in [n for n in g.nodes.nodes if not n.explored]:
        for j in n.jugs.get_moves():
            if not g.has_node(str(j)):
                nn = Node(str(j))
                nn.jugs = j
                nn.explored = False
                nn.prev = n
                g.add_node(nn)
                g.add_edge((n.name, nn.name))

                if j.equals(target):
                    found = True
                    nn.colour = (0, 255, 0)
        n.explored = True

t = [n for n in g.nodes.nodes if n.jugs.equals(target)][0]
prev = t.prev
while prev is not None:
    prev.colour = (200, 200, 0)
    prev = prev.prev

s.colour = (255, 0, 0)

DisplayGraph(g).run()


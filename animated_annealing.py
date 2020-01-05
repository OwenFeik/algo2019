import random
from graph import Graph
from display import DisplayGraph

g = Graph(10, 1)
# for i in range(10):
#     g.add_edge((i, i))
#     g.get_edge((i, i)).cost = 0

def build_path(g):
    start = random.choice(g.nodes)
    prev = start
    path = [start]

    while len(path) < len(g.nodes):
        prev = random.choice([n for n in g.get_neighbours(prev) if not n in path])
        path.append(prev)

    path.append(start)

    return path

def cost(path):
    return sum([g.get_edge((path[i - 1].name, path[i].name)).cost for i in range(1, len(path))])

def get_alternative(path):
    a = random.randint(2, len(path) - 2)
    b = a - 1

    return path[:b] + [path[a]] + [path[b]] + path[a + 1:]

def colour_path(path, g, colour):
    for i in range(1, len(path)):
        g.get_edge((path[i].name, path[i - 1].name)).colour = (0, 255, 0)
    DisplayGraph(g, show_edge_labels = True, edge_labels = 'cost').run()

def clear_colours(g):
    for e in g.edges:
        e.colour = (255, 255, 255)


for e in g.edges:
    e.cost = random.randint(1, 20)

temperature = 1
best_path = build_path(g)
path_cost = cost(best_path)
first_cost = path_cost

d = DisplayGraph(g)
d.show()
d.distribute()
d.scale()

while temperature > 0.1:
    clear_colours(g)

    poss_path = get_alternative(best_path)
    poss_cost = cost(poss_path) 
    
    colour_path(poss_path, g, (255, 255, 0))

    if (poss_cost < path_cost) or (random.random() < 2 ** min(-10, (-1 * (poss_cost - path_cost / temperature)))):
        best_path = poss_path
        path_cost = poss_cost

    colour_path(best_path, g, (0, 255, 0))

    temperature *= 0.99

    d.distribute()
    d.redraw()

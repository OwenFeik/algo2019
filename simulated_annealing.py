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

def show_path(path, g):
    for i in range(1, len(path)):
        g.get_edge((path[i].name, path[i - 1].name)).colour = (0, 255, 0)
    DisplayGraph(g, show_edge_labels = True, edge_labels = 'cost', edge_label_style = 'circle').run()


# improvements = []
# for _ in range(100):
for e in g.edges:
    e.cost = random.randint(1, 20)

temperature = 1
best_path = build_path(g)
path_cost = cost(best_path)
first_cost = path_cost

while temperature > 0.1:
    poss_path = get_alternative(best_path)
    poss_cost = cost(poss_path) 
    
    if (poss_cost < path_cost) or (random.random() < 2 ** min(-10, (-1 * (poss_cost - path_cost / temperature)))):
        best_path = poss_path
        path_cost = poss_cost

    temperature *= 0.99

        # print([str(n) for n in best_path])
        # print(path_cost)
    
show_path(best_path, g)

    # print(f'Improvement: {first_cost - path_cost}')
    # improvements.append(first_cost - path_cost)

# print(f'Avg Improvement: {sum(improvements) / len(improvements)}')

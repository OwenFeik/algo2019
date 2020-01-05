from graph import Graph
from display import DisplayGraph

g = Graph(
    nodes = ['a', 'b', 'c', 'd', 'e', 'f'],
    edges = [
        {'u': 'a', 'v': 'b'},
        {'u': 'a', 'v': 'c'},
        {'u': 'a', 'v': 'e'},
        {'u': 'b', 'v': 'c'},
        {'u': 'b', 'v': 'd'},
        {'u': 'd', 'v': 'c'},
        {'u': 'd', 'v': 'f'},
        {'u': 'c', 'v': 'f'},
        {'u': 'c', 'v': 'e'},
        {'u': 'f', 'v': 'e'}
    ]
)

colours = {'r': (255, 0, 0), 'g': (0, 255, 0), 'b': (0, 0, 255)}
DisplayGraph(g).run()


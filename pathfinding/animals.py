from graph import Graph
from display import DisplayGraph

g = Graph(['C', 'M', 'E', 'G', 'A', 'L', 'H'], [
    {'u': 'C', 'v': 'M'},
    {'u': 'C', 'v': 'E'},
    {'u': 'E', 'v': 'M'},
    {'u': 'E', 'v': 'G'},
    {'u': 'M', 'v': 'E'},
    {'u': 'G', 'v': 'E'},
    {'u': 'G', 'v': 'C'},
    {'u': 'G', 'v': 'A'},
    {'u': 'L', 'v': 'C'},
    {'u': 'L', 'v': 'G'},
    {'u': 'L', 'v': 'A'},  
    {'u': 'L', 'v': 'E'},
    {'u': 'L', 'v': 'M'}  
],
True)

DisplayGraph(g).run()

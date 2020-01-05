import math
from graph import Graph

# The Floyd-Warshall algorithm:
#
#   The Floyd-Warshall algorithm works on the understanding that the shortest
#   path between two vertices v and w that uses only vertices numbered less
#   than k is given by shortest(v,w,k).
#
#   Given this, the shortest path between v and w could be either a path that
#   doesn't pass through k, or a path that passes from v to k and then k to w.
#   
#   Additionally, it is clear that the value of shortest(v,w,0) is simply the
#   cost of the edge vw, as no other nodes are in range. This becomes the 
#   recursive base case.
#
#
# Let G be a weighted graph, without negative cycles.
# Let dist be a square array of size equal to the number of nodes.
# Initialise each value in dist to infinity.
# For each edge in vw in G:
#   Let dist[v][w] be equal to the cost of edge vw
# For each vertex v:
#   Let dist[v][v] be equal to 0
#
# Let n be the number of nodes.
# For k from 1 n:
#   For i from 1 to n:
#       For j from 1 to n:
#           if dist[i][j] > dist[i][k] + dist[k][j]
#               Let dist[i][j] equal dist[i][k] + dist[k][j]

def floyd_warshall(G,directed=False):
    n = len(G.nodes)
    dist = [[math.inf for _ in range(n)] for _ in range(n)] # Create a square array to hold the distance from each node to each other

    for edge in G.edges:
        dist[edge.u][edge.v]=edge.cost # Add the cost of this edge to the array as the base case
        if not directed: # If this isn't a directed graph
            dist[edge.v][edge.u]=edge.cost # We need to add the other direction for each edge
    for node in G.nodes:
        dist[node.ident][node.ident]=0 # Set distance from a node to itself to 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]: # If the current path from i to j is less than the path through k
                    dist[i][j] = dist[i][k] + dist[k][j] # Change the array to reflect this new shortest path

    return dist # Return array of distances


# g = Graph(
#     nodes=[0,1,2,3,4,5,6,7,8,9],
#     edges=[
#         {'u':1,'v':2,'cost':3},
#         {'u':1,'v':3,'cost':4},
#         {'u':1,'v':5,'cost':10},
#         {'u':1,'v':6,'cost':18},
#         {'u':2,'v':3,'cost':1},
#         {'u':2,'v':4,'cost':5},
#         {'u':2,'v':5,'cost':9},
#         {'u':3,'v':4,'cost':4},
#         {'u':4,'v':5,'cost':7},
#         {'u':4,'v':7,'cost':9},
#         {'u':4,'v':8,'cost':9},
#         {'u':5,'v':6,'cost':8},
#         {'u':5,'v':7,'cost':8},
#         {'u':5,'v':9,'cost':9},
#         {'u':6,'v':9,'cost':9},
#         {'u':6,'v':0,'cost':9},
#         {'u':7,'v':8,'cost':2},
#         {'u':7,'v':9,'cost':2},
#         {'u':8,'v':9,'cost':4},
#         {'u':8,'v':0,'cost':6},
#         {'u':9,'v':0,'cost':3}
#     ]
# )

# print(floyd_warshall(g))

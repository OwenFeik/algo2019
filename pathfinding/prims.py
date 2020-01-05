import math
from graph import Graph

# Prim's algorithm (also Jarnik's algorithm):
#
# Prim's algorithm is used to find the minumum spanning tree of a graph.
#   ie. it finds the minimum number total cost of edges to connect all nodes in a graph.
#   It uses a 'greedy' technique; making the locally optimal choice at each stage to
#   find the optimal solution. To do this, it starts with an empty tree, and adds the
#   closest node from the graph until all nodes are part of the tree.
#
# let there be a graph G and a 'forest' F
# For each vertice in G, associate with that vertice the cost of the shortest edge connecting to it (C),
#   initially infinity, and the edge that this cost is obtained through (E), initially null 
# Let Q be the set of nodes not included in F
# Repeat until Q is empty:
#    Find the vertice v with the lowest value C, and remove it from Q
#    Add v to F, if it's E is not null, also add E to F
#    For each neighbour w of this vertice:
#       If cost of edge vw < current C of w:
#          Set C[w] to cost of edge vw
#          Set E[w] to edge vw 
# Return F
#
# F will be a 'Forest'; a graph containing a number of trees equal to the number of disconnected subgraphs in G
#

def prims(G):
    F = Graph() # Forest to build output trees in
    for node in G.nodes: # Initialise C and E for each node
        node.C = math.inf # Cost is initially inf until discovered during search
        node.E = None # No edge is presently associated with this cost

    Q = [n for n in G.nodes] # Set of nodes not in F, initially all nodes
    while Q:
        v = min(Q, key=lambda k:k.C) # Find node with the lowest cost
        Q.remove(v) # Adding this node to F, so remove from Q
        F.add_node(v.ident)
        if v.E: # If an edge was taken to reach this node
            F.add_edge(v.E) # Add it to the tree

        for w in G.neighbours(v.ident): # Visit each neighbour of v
            E = G.get_edge(v.ident,w)
            w = G.nodes[w]

            if w in Q and w.C>E.cost: # If this node is closer to w than previous closest
                w.C = E.cost # Update the minimum cost
                w.E = E # And the edge taken to achieve that cost

    return F # Minimum spanning tree of G


g=Graph(
    nodes=[1,2,3,4,5,6,7,8,9,10],
    edges=[
        {'u':1,'v':2,'cost':3},
        {'u':1,'v':3,'cost':4},
        {'u':1,'v':5,'cost':10},
        {'u':1,'v':6,'cost':18},
        {'u':2,'v':3,'cost':1},
        {'u':2,'v':4,'cost':5},
        {'u':2,'v':5,'cost':9},
        {'u':3,'v':4,'cost':4},
        {'u':4,'v':5,'cost':7},
        {'u':4,'v':7,'cost':9},
        {'u':4,'v':8,'cost':9},
        {'u':5,'v':6,'cost':8},
        {'u':5,'v':7,'cost':8},
        {'u':5,'v':9,'cost':9},
        {'u':6,'v':9,'cost':9},
        {'u':6,'v':10,'cost':9},
        {'u':7,'v':8,'cost':2},
        {'u':7,'v':9,'cost':2},
        {'u':8,'v':9,'cost':4},
        {'u':8,'v':10,'cost':6},
        {'u':9,'v':10,'cost':3},
    ]
)

# mst=prims(g)

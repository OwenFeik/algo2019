import math
from graph import Graph

# The Bellman-Ford Algorithm:
#
#   The Bellman-Ford Algorithm works in a similar fashion to Dijkstra's algorithm,
#   by 'relaxation', where each node is initially marked with an approximation
#   of it's distance, which is improved until the optimal solution is found.
#
#   Where it differs is that, where Dijkstra's algorithm uses a 'greedy' strategy,
#   the Bellman-Ford algorithm performs relaxation on all outgoing edges each
#   iteration.
#
#   The algorithm runs in O(|V|*|E|) time, as for each node it iterates over
#   each edge.
#
# Let G be a graph
# For each node v in G:
#   Set dist[v] to infinity
#   Set prev[v] to null
#
# Set dist[source] to 0
#
# For i from 1 to number of nodes - 1
#   For each edge (u, v) in G:
#       If dist[u] + cost of edge < dist[v]:
#           Let dist[v] equal dist[u] + cost of edge
#           Let prev[v] equal u
#
# For each edge (u, v) in G:
#   If dist[u] + cost of edge < dist[v]:
#       Error: Graph contains a negative cycle
#
# Return G

def bellman_ford(G,S,directed=False):
    for n in G.nodes: # Initialise values for each node
        n.dist = math.inf # Distance from source is initially unknown, so all paths are better
        n.prev = None # No path known, so no previous node

    G.nodes[S].dist = 0 # Distance to source is 0

    for _ in range(len(G.nodes)): # 1 iteration per node
        for edge in G.edges:
            u = G.nodes[edge.u]
            v = G.nodes[edge.v]
            if u.dist + edge.cost < v.dist: # If the path would be shorter through this edge
                v.dist = edge.cost + u.dist # Set the distance to this new shortest distance
                v.prev = u # This path passed through this node

            if not directed: # If the graph is not a digraph, then we need to check both ways
                if v.dist + edge.cost < u.dist:
                    u.dist = edge.cost + v.dist
                    u.prev = v                

    for edge in G.edges: # If there are still better routes, the graph contains a negative cycle
        if G.nodes[edge.u].dist + edge.cost < G.nodes[edge.v].dist:
            raise Exception('Graph contains a negative cycle.')

    return G

from time import sleep
from display import DisplayGraph

def bellman_ford_animated(G,S,directed=False):
    G = DisplayGraph(G, directed = False, show_node_labels = True, show_edge_labels = True, node_labels = 'dist', edge_labels = 'cost')
    G.show()
    G.distribute()
    G.scale()

    for n in G.nodes: # Initialise values for each node
        n.dist = math.inf # Distance from source is initially unknown, so all paths are better
        n.prev = None # No path known, so no previous node
        n.colour = (20, 200, 0)

    G.nodes[S].dist = 0 # Distance to source is 0

    for _ in range(len(G.nodes)): # 1 iteration per node
        for edge in G.edges:
            edge.colour = (0, 150, 0)
            G.redraw()
            sleep(0.05)

            u = G.nodes[edge.u]
            v = G.nodes[edge.v]
            if u.dist + edge.cost < v.dist: # If the path would be shorter through this edge
                v.dist = edge.cost + u.dist # Set the distance to this new shortest distance
                v.prev = u # This path passed through this node

            if not directed: # If the graph is not a digraph, then we need to check both ways
                if v.dist + edge.cost < u.dist:
                    u.dist = edge.cost + v.dist
                    u.prev = v                
            
            edge.colour = (150, 0, 0)
            G.redraw()
            sleep(0.05)

    for edge in G.edges: # If there are still better routes, the graph contains a negative cycle
        if G.nodes[edge.u].dist + edge.cost < G.nodes[edge.v].dist:
            raise Exception('Graph contains a negative cycle.')

    G.run()

from example import g
bellman_ford_animated(g, 0)

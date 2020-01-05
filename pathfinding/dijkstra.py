from math import inf # Set distance of unexplored nodes to infinity

# Dijkstra's algorithm
#
# Given an input graph G:
# Let Q be the set of unvisited nodes of G
# For each of these nodes:
#   Initialise their distance to infinity
#   Set their previous node to null
#
# While there are nodes in Q:
#   let v be the node with the minimum distance
#   remove v from Q
#   for each neighbour w of v:
#       let A equal v's distance + the cost of edge vw
#       if A is less than w's distance:
#           Set the distance of w to A
#           Set the previous node of w to v
#
# Return G 

def dijkstra(graph,source): # Create a graph where nodes have the value 'dist' indicating distance from source and 'prev' indicating path
    unvisited=[]
    for node in graph.nodes: # Place all nodes in the unvisited set
        node.dist=inf # Set their distance to infinity
        node.prev=None
        unvisited.append(node)

    graph.get_node(source).dist=0 # Set the distance of the source node to zero

    while len(unvisited)>0: # While there are unvisited nodes
        nxt=min(unvisited,key=lambda k:k.dist) # Select the nearest as the next
        unvisited.remove(nxt) # Remove it from unvisited
        for edge in graph.get_neighbour_edges(nxt): # For edge connecting to next
            alt=nxt.dist+edge.cost # Distance when routing through next
            other=graph.get_node(edge.other(nxt.ident)) # Other node on the edge
            if alt<other.dist: # If this path is shorter than the nodes current path
                other.dist=alt # Set the distance of this node to this route
                other.prev=nxt # Set the previous node in this nodes path to next
    
    return graph # Return the graph of all nodes, with distance and path for each


def dijkstra_target(graph,source,target,out='path'): # Find shortest path to target from source
    unvisited=[]
    for node in graph.nodes: # Initialise all nodes into the unvisited set
        node.dist=inf
        node.prev=None
        unvisited.append(node)

    graph.get_node(source).dist=0

    while len(unvisited)>0: # Same as regular,
        nxt=min(unvisited,key=lambda k:k.dist) # We are following the shortest path each time,
        unvisited.remove(nxt)
        for edge in graph.get_neighbour_edges(nxt.ident):
            alt=nxt.dist+edge.cost
            other=graph.get_node(edge.other(nxt.ident))
            if alt<other.dist:
                other.dist=alt
                other.prev=nxt
        if nxt.ident==target: # So stop when we first find the target
            node=nxt
            break # Could be above 'for edge...', but keep here so we update next with appropriate data
    
    if out=='string': # Create a string showing the path followed
        path=[]
        while node:
            path.append(f'{node.ident} ({node.dist}) > ')
            node=node.prev
        path.reverse() # The array currently starts from the target node, so we'll reverse it
        string=''.join(path) # Return the path as a string for printing, etc
        return string[0:len(string)-3] # Slice off the ' > ' at the end
    elif out=='dist': # Return the minimum distance to the target
        return node.dist
    else: # Return list of the nodes taken to get to the target
        path=[]
        while node:
            path.append(node)
            node=node.prev
        return path

from time import sleep
from display import DisplayGraph

def dijkstra_animated(g, source):
    g = DisplayGraph(g, show_labels = True, node_labels = 'dist', edge_labels = 'cost')    
    g.show()
    g.distribute(animate = False)
    g.scale()
    g.redraw()

    unvisited = []
    for n in g.nodes:
        n.dist = inf
        n.prev = None
        n.colour = (0, 200, 200)
        unvisited.append(n)

    g.nodes[source].dist = 0
    g.nodes[source].colour = g.default_node_colour

    while len(unvisited) > 0:
        nxt = min(unvisited, key = lambda k: k.dist)
        unvisited.remove(nxt)
        nxt.colour = g.default_node_colour
        g.redraw()
        sleep(0.2)

        for e in g.get_neighbour_edges(nxt):
            e.colour = (200, 0, 0)
            g.redraw()
            sleep(0.2)
            alt = nxt.dist + e.cost
            other = g.nodes[e.other(nxt.name)]
            if alt < other.dist:
                other.dist = alt
                other.prev = nxt
            e.colour = (100, 100, 0)

    g.run()

from example import g
dijkstra_animated(g, 0)

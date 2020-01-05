from math import inf,sqrt # Set node distances to infity, calculate pythag distances

def astar(graph,source,target,heuristic):
    """Where graph is the graph to find a path through, source and target are the start and end node idents respectively and heuristic is a function that returns a numeric value representing an estimate of the distance to a target node from a source node, accepting the graph and idents of target and node to test."""

    closed_nodes=[]
    open_nodes=[]

    for node in graph.nodes:
        node.dist=inf # dist is the distance from the source node to this node
        node.t_dist=inf # t_dist is the distance to the target node through this node
        node.prev=None
    
    open_nodes.append(graph.get_node(source)) # Initially, the only open node is the source
    graph.get_node(source).dist=0 # Distance to the source is 0
    graph.get_node(source).t_dist=heuristic(graph,source,target) # Our distance to the target is given solely by our heuristic

    while open_nodes: # As long as we have nodes to search
        current=min(open_nodes,key=lambda k:k.t_dist) # Grab the node with the lowest distance from the source
        if current.ident==target: # If we found the target
            node=current
            path=[]
            while node: # Create a string showing the path followed
                path.append(f'{node.ident} ({node.dist}) > ')
                node=node.prev
            path.reverse() 
            string=''.join(path)
            return string[0:len(string)-3] # Slice off the ' > ' at the end

        open_nodes.remove(current) # Otherwise, remove this node from the pool of open nodes 
        closed_nodes.append(current) # Add it to the pool of closed nodes

        for edge in graph.neighbours(current.ident): # For each edge touching this node
            other=graph.get_node(edge.other(current.ident)) # Get the other node on the edge
            
            if other in closed_nodes: # If this node has been analysed
                continue # Pass
            alt=current.dist+edge.cost # Otherwise, determine the distance of this node from source
            if other not in open_nodes: # If its not in open nodes 
                open_nodes.append(other) # We found a new node
            elif alt >= other.t_dist: # Otherwise, if this route is longer
                continue # Pass

            other.prev=current # This node is on a path, through current
            other.dist=alt # It is alt far from source
            other.t_dist=current.dist+heuristic(graph,other.ident,target) # Approximate its distance with heuristic
            

def pythag(graph,source,target):
    """Given a graph and 2 node idents from that graph, source and target, with nodes possessing numeric properties x and y, return the pythagorean distance from source target."""
    x1=graph.get_node(source).x
    y1=graph.get_node(source).y
    x2=graph.get_node(target).x
    y2=graph.get_node(target).y
    a=max([x1,x2])-min([x1,x2])
    b=max([y1,y2])-min([y1,y2])
    return sqrt(a**2+b**2)

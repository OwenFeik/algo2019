from graph import Graph,Edge

def bfs(G,A,B):
    unexplored=[A]
    explored=[]
    if not G.has_node(B):
        return False

    found=False
    while not(not unexplored or  found):
        C=unexplored[0]
        if C==B:
            found=True
        else:
            for node in [[node for node in [edge.a,edge.b] if node!=C][0] for edge in G.neighbours(C)]:
                if not node in explored:
                    unexplored.append(node)
        explored.append(unexplored[0])
        del unexplored[0]
    return found

def bfs_map(G,A,B):
    for node in G.nodes:
        node.dist=0
    q=[A]
    for C in q:
        for node in [[node for node in [edge.a,edge.b] if node!=C][0] for edge in G.neighbours(C)]:
            node=G.get_node(node)
            if node.dist==0:
                node.dist=G.get_node(C).dist+1
                q.append(node.ident)
    G.get_node(A).dist=0
    print(f'Distance from {A} to {B}: {G.get_node(B).dist}')
    return G

# G=Graph(['A','B','C','D','E','F','G','H'])
# G.add_edge(Edge('A','B'))
# G.add_edge(Edge('A','E'))
# G.add_edge(Edge('B','F'))
# G.add_edge(Edge('B','C'))
# G.add_edge(Edge('C','G'))
# G.add_edge(Edge('C','D'))
# G.add_edge(Edge('D','H'))
# G.add_edge(Edge('G','H'))
# G.add_edge(Edge('E','F'))

# out=bfs_map(G,'A','H')

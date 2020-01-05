from graph import Graph,Edge
from dijkstra import dijkstra_target

g=Graph([1,2,3,4,5,6,7,8,9,10]) # Create graph with 10 houses
g.add_edge(Edge(1,2,cost=3))
g.add_edge(Edge(2,3,cost=4))
g.add_edge(Edge(3,4,cost=2))
g.add_edge(Edge(4,5,cost=3))
g.add_edge(Edge(5,6,cost=5))
g.add_edge(Edge(6,7,cost=4))
g.add_edge(Edge(7,1,cost=2))
g.add_edge(Edge(1,10,cost=3))
g.add_edge(Edge(10,9,cost=4))
g.add_edge(Edge(9,2,cost=3))
g.add_edge(Edge(9,3,cost=3))
g.add_edge(Edge(5,3,cost=4))
g.add_edge(Edge(9,5,cost=2))
g.add_edge(Edge(8,5,cost=3))
g.add_edge(Edge(8,9,cost=3))
g.add_edge(Edge(8,10,cost=4))
g.add_edge(Edge(10,7,cost=4))
g.add_edge(Edge(8,7,cost=5))
g.add_edge(Edge(10,2,cost=2))
g.add_edge(Edge(6,8,cost=3))


for i in range(1,11):
    pass

# Second idea:
# Algorithm:
# find_minimum_roads(map):
#   for a graph of nodes (houses) joined by edges (roads) with a cost
#   determine the minimum total cost of roads that need be created to join all of the houses
#   and the roads that should be constructed to meet this minimum
#
#   total <- 0
#   finished <- False
#   while:
#       distances <- dict
#       for each node on map:
#           calculate the minimum distance from this node to each other node
#           store these values in distances
#       
#       shortest <- lowest non-zero value in distances
#       if there are no non-zero values:
#           end while       
#
#       for each key in distances:
#           if value of this key = shortest:
#               get the path taken from the first node to the second
#               add the cost of each edge on this path to total
#               set the cost of each edge on this path to zero
#               end for
#
#   return total,roads with cost = 0


total=0
while True:
    distances={}
    for node in g.nodes:
        distances.update({(node.ident,i):dijkstra_target(g,node.ident,i,'dist') for i in range(1,11)})
    
    dists=[value for value in distances.values() if value>0]
    if dists:
        shortest=min(dists)
    else:
        break

    for key in distances:
        if distances[key]==shortest:
            p=dijkstra_target(g,key[0],key[1],'path')
            for node in p:
                if node.prev:
                    total+=g.get_edge(node.ident,node.prev.ident).cost
                    g.get_edge(node.ident,node.prev.ident).cost=0
            break

for edge in g.edges:
    if edge.cost==0:
        print(f'{edge.a}--{edge.b}: Paved')
print(f'Total = {total}')



# # First idea:
# # Algorithm:
# # find_minimum_roads(map):
# #   for a graph of nodes (houses) joined by edges (roads) with a cost
# #   determine the minimum total cost of roads that need be created
# #   and the roads that should be constructed to meet this minimum
# #
# #   let total = 0
# #   let source node = node of the highest degree
# #   for each house:
# #       find the shortest path from source to the house
# #       let p equal a list of edges equal this path
# #       for each edge in p:
# #           add the cost of this edge to total
# #           set the cost of this edge to 0
# #   
# #   return total,roads with cost 0


# print(g)

# total=0
# for i in range(1,11):
#     p=dijkstra_target(g,9,i)
#     for node in p:
#         if node.prev:
#             total+=g.get_edge(node.ident,node.prev.ident).cost
#             g.get_edge(node.ident,node.prev.ident).cost=0

# for edge in g.edges:
#     print(str(edge))
# print(total)
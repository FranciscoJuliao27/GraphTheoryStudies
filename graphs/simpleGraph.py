import networkx as nx

# Creating a null Graph
S = nx.Graph()

# Adding nodes
S.add_nodes_from(['x', 'y', 'z', 'w'])

# Adding Edges
S.add_edges_from([('x','y'),('x','w'),('x','z'),('y','z')])

print(f"Nodes: {S.nodes()}")
print(f"Edges: {S.edges()}")
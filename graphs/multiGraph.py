import networkx as nx

# Instantiating the MultiGraph
S = nx.MultiGraph()

# The nodes are automatically created by adding the edges
S.add_edges_from([('x','y'),('x','y'),('y','x'),('x','w'),('y','w'),('z','w'),('w','z')])

print(f"Nodes: {S.nodes()}")
print(f"Edges: {S.edges()}")

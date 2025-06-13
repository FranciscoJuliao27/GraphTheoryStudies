import networkx as nx

S = nx.MultiGraph()

S.add_edges_from([('x','y'),('x','y'),('x','w'),('y','w'),('z','w'),('w','w')])

print(f"Nodes: {S.nodes()}")
print(f"Edges: {S.edges()}")
import networkx as nx

M = nx.MultiGraph()

M.add_node('a', label ='a', fillcolor = 'grey')
M.add_node('b', label ='b', fillcolor = 'blue')
M.add_node('c', label ='c', fillcolor = 'green')
M.add_node('d', label ='d', fillcolor = 'red')

M.add_edge('a','b',label = 'ab')
M.add_edge('b','c',label = 'bc')
M.add_edge('a','d',label = 'ad')
M.add_edge('b','d',label = 'bd')
M.add_edge('c','d',label = 'cd1')
M.add_edge('c','d',label = 'cd2')

print("Nodes: ")
for n, attr in M.nodes(data=True):
    print(n, attr)
print("Edges: ")
for a, b, i in M.edges:
    print(a, b, i, M.get_edge_data(a, b, i))
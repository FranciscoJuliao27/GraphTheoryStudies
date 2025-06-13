import networkx as nx

S = nx.Graph()

# Adding Nodes with Attributes
S.add_node('a', label ='a', fillcolor = 'grey')
S.add_node('b', label ='b', fillcolor = 'blue')
S.add_node('c', label ='c', fillcolor = 'green')
S.add_node('d', label ='d', fillcolor = 'red')

# Adding Edges with a Attribute
S.add_edge('a','b',label = 'ab')
S.add_edge('b','c',label = 'bc')
S.add_edge('a','d',label = 'ad')
S.add_edge('b','d',label = 'bd')
S.add_edge('c','d',label = 'cd')

print("Nodes: ")
for n, attr in S.nodes(data=True):
    print(n, attr)
print("Edges: ")
for a, b, attr in S.edges(data=True):
    print(a, b, attr)
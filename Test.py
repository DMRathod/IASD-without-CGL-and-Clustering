import networkx as nx

graph = {
    'a': ['c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['a', 'd'],
    'e': ['b', 'c']
}


g =nx.from_dict_of_lists(graph)

h = g.edges()
print(h)

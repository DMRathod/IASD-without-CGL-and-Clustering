from collections import defaultdict

d = lambda _: f'd{_}'
test_cases = [
    # [{'d1'}, {'d2'}, {'d1', 'd2'}],
    # [{d(1)}, {d(2)}],
    # [{d(1)}, {d(2)}, {d(2), d(3)}, {d(2), d(4), d(5)}],
    [{d(2)}, {d(1), d(2)}, {d(2), d(3)}, {d(1)}, {d(1), d(2), d(3)}],
    # [{d(2)}, {d(3), d(4)}]
]

for req in test_cases:
    length_to_node = defaultdict(set)
    length_to_node[0] = {frozenset()}
    nodes_to_children = defaultdict(set)
    nodes_to_children[frozenset()] = set()
    for node in req:
        node_len = len(node)
        length_to_node[node_len].add(frozenset(node))
        connected_to_atleast_one = False
        for i in range(node_len-1, -1, -1):
            old_nodes = length_to_node[i]
            for old_node in old_nodes:
                if old_node.issubset(node):
                    nodes_to_children[frozenset(node)].add(frozenset(old_node))
                    connected_to_atleast_one = True
            if connected_to_atleast_one:
                break
    # print(nodes_to_children)
    for key, val in nodes_to_children.items():
        print(f'{list(key)} :::: {[" ".join(i) for i in val]}')

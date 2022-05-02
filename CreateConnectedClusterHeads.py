from collections import defaultdict

import ClusterHead as CHead

def add_edges_on_node(node_one, node_two, graph):
    graph[node_one].append((node_two, CHead.Euclidean_dist(node_one, node_two)))
    graph[node_two].append((node_one, CHead.Euclidean_dist(node_one, node_two)))

def add_edges(edges, graph):
    for node_one, node_two in edges:
        add_edges_on_node(node_one, node_two, graph)

def Create_graph():
    p1 = CHead.ClusterHead(1, 8)
    p2 = CHead.ClusterHead(7, 9)
    p3 = CHead.ClusterHead(2, 3)
    p4 = CHead.ClusterHead(6, 1)
    p5 = CHead.ClusterHead(10, 4)
    p6 = CHead.ClusterHead(12, 7)
    p7 = CHead.ClusterHead(13, 2)
    p8 = CHead.ClusterHead(5, 15)
    p9 = CHead.ClusterHead(20, 15)
    adjacency_list = defaultdict(list)
    # adjacency_list = {
    #     p1: [(p2, CHead.Euclidean_dist(p1, p2)), (p3, CHead.Euclidean_dist(p1, p3)), (p5, CHead.Euclidean_dist(p1, p5)), (p8, CHead.Euclidean_dist(p1, p8))],
    #     p2: [(p1, CHead.Euclidean_dist(p1, p2)), (p5, CHead.Euclidean_dist(p2, p5)), (p6, CHead.Euclidean_dist(p2, p6)), (p8, CHead.Euclidean_dist(p1, p8))],
    #     p3: [(p1, CHead.Euclidean_dist(p3, p1)), (p5, CHead.Euclidean_dist(p3, p5)), (p4, CHead.Euclidean_dist(p3, p4))],
    #     p4: [(p3, CHead.Euclidean_dist(p4, p3)), (p5, CHead.Euclidean_dist(p4, p5))],
    #     p5: [(p1, CHead.Euclidean_dist(p5, p1)), (p2, CHead.Euclidean_dist(p5, p2)), (p3, CHead.Euclidean_dist(p5, p3)), (p4, CHead.Euclidean_dist(p5, p4))],
    #     p6: [(p5, CHead.Euclidean_dist(p6, p5)), (p2, CHead.Euclidean_dist(p6, p2)), (p7, CHead.Euclidean_dist(p6, p7)), (p9, CHead.Euclidean_dist(p9, p6))],
    #     p7: [(p6, CHead.Euclidean_dist(p7, p6))],
    #     p8: [(p1, CHead.Euclidean_dist(p1, p8)), (p2, CHead.Euclidean_dist(p2, p8))],
    #     p9: [(p6, CHead.Euclidean_dist(p9, p6))]
    # }
    edges = [(p1, p2), (p1, p3), (p1, p5), (p5, p2), (p6, p2), (p3, p5), (p3, p4), (p4, p5), (p5, p6), (p6, p7), (p8, p1), (p2, p8), (p9, p6)]
    add_edges(edges, adjacency_list)
    # print(adjacency_list)
    return adjacency_list


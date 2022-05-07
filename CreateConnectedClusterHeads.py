from collections import defaultdict
import CreateConnectingPoints as CP
import ClusterHead as CHead
import numpy as np


def add_edges_on_node(node_one, node_two, graph):
    graph[node_one].append((node_two, CHead.Euclidean_dist(node_one, node_two)))
    graph[node_two].append((node_one, CHead.Euclidean_dist(node_one, node_two)))


def add_edges(edges, graph):
    for node_one, node_two in edges:
        add_edges_on_node(node_one, node_two, graph)


class Create_clusters:
    BOUND = 32
    adjacency_list = defaultdict(list)
    p1 = CHead.ClusterHead(20, 50, 'C1')
    p2 = CHead.ClusterHead(80, 60, 'C2')
    p3 = CHead.ClusterHead(20, 30, 'C3')
    p4 = CHead.ClusterHead(35, 8, 'C4')
    p5 = CHead.ClusterHead(55, 30, 'C5')
    p6 = CHead.ClusterHead(90, 30, 'C6')
    p7 = CHead.ClusterHead(110, 8, 'C7')
    edges = [(p1, p2), (p1, p3), (p1, p5), (p5, p2), (p6, p2), (p3, p5), (p3, p4), (p4, p5), (p5, p6), (p6, p7)]
    add_edges(edges, adjacency_list)

    def __init__(self):
        self.list_of_clusterheads = []
        self.list_of_clusterheads.extend([self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7])
        # p1 = CHead.ClusterHead(1, 8)
        # p2 = CHead.ClusterHead(7, 9)
        # p3 = CHead.ClusterHead(2, 3)
        # p4 = CHead.ClusterHead(6, 1)
        # p5 = CHead.ClusterHead(10, 4)
        # p6 = CHead.ClusterHead(12, 7)
        # p7 = CHead.ClusterHead(13, 2)
        # p8 = CHead.ClusterHead(5, 15)
        # p9 = CHead.ClusterHead(20, 15)




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
        # edges = [(p1, p2), (p1, p3), (p1, p5), (p5, p2), (p6, p2), (p3, p5), (p3, p4), (p4, p5), (p5, p6), (p6, p7), (p8, p1), (p2, p8), (p9, p6)]
        # print(adjacency_list)

    def assign_connecting_points1(self):
        cp = CP.CreateConnectingPoint()
        points = cp.get_connecting_points()
        cluster_heads = self.list_of_clusterheads
        # # for one,two in zip(cluster_heads,points):
        # #     print(one.name, two.name)
        # # for l in points: print(l.name,end=" ")
        # # # print(points[2].)
        # # cluster_heads[3].list_of_connectingPoints.append(points[2].name)
        # # cluster_heads[3].list_of_connectingPoints.append(points[4].name)
        # # cluster_heads[2].list_of_connectingPoints.append(points[5].name)
        # # cluster_heads[2].list_of_connectingPoints.append(points[9].name)
        # # cluster_heads[5].list_of_connectingPoints.append(points[6].name)
        # # cluster_heads[6].list_of_connectingPoints.append(points[8].name)
        #
        # for each in cluster_heads:
        #     print(each.list_of_connectingPoints)

        bounds = [32, 31, 25, 25, 25, 23, 21, 15]
        for p in points:
            bound_i = 0
            for head in cluster_heads:
                d = np.sqrt((p.x_coordinate - head.x_coordinate) ** 2 + (p.y_coordinate - head.y_coordinate) ** 2)
                # print("from assign points", p.name, head.name, d)
                if d <= bounds[bound_i]:
                    head.list_of_connectingPoints.append(p.name)
                bound_i += 1

                # for j in head.list_of_connectingPoints:print(j)
        # for h in cluster_heads:
        #     print(h.list_of_connectingPoints)
            # #
        for each in cluster_heads:
            print("from connecting point", each.name, each.list_of_connectingPoints)


        return cp.get_connecting_points()

    def get_graph_of_cluster_heads(self):
        return self.adjacency_list

    def get_all_cluster_heads(self):
        return self.list_of_clusterheads


def cluster_head_list():
    cch = Create_clusters()
    return cch.get_graph_of_cluster_heads()

import numpy as np


def Euclidean_dist(p1, p2):
    return np.sqrt((p2.x_coordinate - p1.x_coordinate) ** 2 + (p2.y_coordinate - p1.y_coordinate) ** 2)


def get_list_of_clusters(graph, source, destination):
    s_exist = False
    d_exist = False

    for each in graph.keys():
        if each.x_coordinate == source[0] and each.y_coordinate == source[1]:
            source1 = each
            s_exist = True
        if each.x_coordinate == destination[0] and each.y_coordinate == destination[1]:
            destination1 = each
            d_exist = True

    if s_exist or d_exist:
        print("Source or destination Does not exist")
        return

    limitation_factor = 1.1
    list_of_cluster_heads = []
    # Variation of BFS
    # visited = [False] * (len(graph)+1)
    visited = {}
    for key in graph.keys():
        visited[key] = False
    # print(visited)
    queue = [source1]
    visited[source1] = True
    # j = 0
    # print(graph[source1])
    while queue:
        temp = queue.pop(0)
        # print(temp, i)
        # j += 1
        if Euclidean_dist(temp, destination1) <= limitation_factor * (Euclidean_dist(source1, destination1)):
            list_of_cluster_heads.append(temp)
            # print(graph[temp])
            for i in graph[temp]:
                # print(i[0])
                if not visited[i[0]]:
                    queue.append(i[0])
                    visited[i[0]] = True
    return list_of_cluster_heads


class ClusterHead:

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
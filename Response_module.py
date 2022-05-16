import CreateConnectingPoints as CP
# import CreateConnectedClusterHeads as CG
# import numpy as np

point_graph = CP.CreateConnectingPoint()
connecting_point_graph = point_graph.connecting_point_adjacency_list
#
# Config_of_cluster_heads = CG.Create_clusters()
# cluster_graph = Config_of_cluster_heads.get_graph_of_cluster_heads()
#
#
# def Euclidean_dist(p1, p2):
#     return np.sqrt((p2.x_coordinate - p1.x_coordinate) ** 2 + (p2.y_coordinate - p1.y_coordinate) ** 2)

#
def average_weights(values):
    return sum(values)/len(values)

#
def communicate_with_other_clusters(service_type, source, destination):
    print(service_type)
    # list_of_cluster_heads = get_list_of_clusters(source, destination)
    # for i in list_of_cluster_heads:
    #     print(i.name)

#
# def get_list_of_clusters(source, destination):
#     s_exist = False
#     d_exist = False
#
#     for each in cluster_graph.keys():
#         if each.x_coordinate == source[0] and each.y_coordinate == source[1]:
#             source1 = each
#             s_exist = True
#         if each.x_coordinate == destination[0] and each.y_coordinate == destination[1]:
#             destination1 = each
#             d_exist = True
#
#     if s_exist == False or d_exist == False:
#         print("Source or destination Does not exist")
#         return
#
#     limitation_factor = 1
#     list_of_cluster_heads = []
#     # Variation of BFS
#     # visited = [False] * (len(graph)+1)
#     visited = {}
#     for key in cluster_graph.keys():
#         visited[key] = False
#     # print(visited)
#     queue = [source1]
#     visited[source1] = True
#     # j = 0
#     # print(graph[source1])
#     while queue:
#         temp = queue.pop(0)
#         # print(temp, i)
#         # j += 1
#         if Euclidean_dist(temp, destination1) <= limitation_factor * (Euclidean_dist(source1, destination1)):
#             list_of_cluster_heads.append(temp)
#             # print(graph[temp])
#             for i in cluster_graph[temp]:
#                 # print(i[0])
#                 if not visited[i[0]]:
#                     queue.append(i[0])
#                     visited[i[0]] = True
#     return list_of_cluster_heads
#

def assign_weights_to_edges(weights_of_connecting_point):
    # print("weights of connecting points", weights_of_connecting_point)
    print("weights of connecting points")

    # for k, v in connecting_point_graph.items():
    #     print(k.name, "=>", end='')
    #     for e in v:
    #         print(e[0].name, end='')
    #     print()

    for each in weights_of_connecting_point.keys():
        # print(each.name)
        for p in connecting_point_graph[each]:
            if p[0] in weights_of_connecting_point.keys():
                p[1] = average_weights([weights_of_connecting_point[each], weights_of_connecting_point[p[0]]])
            # print(p[0].name, p[1])

    for k, v in connecting_point_graph.items():
        print(k.name, "=>", end='')
        for e in v:
            print(e[1], end=' ')
        print()
















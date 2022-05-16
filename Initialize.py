import CreateConnectedClusterHeads as CG
import CreateConnectingPoints as CP
import Assignment_of_nodes as An


def Init_structure():
    Config_of_cluster_heads = CG.Create_clusters()
    cluster_graph = Config_of_cluster_heads.get_graph_of_cluster_heads()
    point_graph = CP.CreateConnectingPoint()
    connecting_point_graph = point_graph.connecting_point_adjacency_list

    print("Physical Connecting point")
    for k, v in connecting_point_graph.items():
        print(k.name, "=>", end='')
        for e in v:
            print(e[0].name, end='')
        print()
    result = Config_of_cluster_heads.assign_connecting_points1()
    number_of_nodes = 20
    list_of_all_nodes = An.assign_nodes_to_cluster(number_of_nodes)
    return list_of_all_nodes, cluster_graph, point_graph

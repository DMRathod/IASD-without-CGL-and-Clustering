import Node
import CreateConnectedClusterHeads as CH
import random





def assign_nodes_to_cluster(number_of_nodes):
    list_of_all_nodes = [Node.Node('N'+str(i), ['d1', 'd2']) for i in range(1, number_of_nodes+1)]
    [print(i.name, end=" ") for i in list_of_all_nodes]
    print()

    def dummy_function(cluster_head, index_of_nodes):
        for i in index_of_nodes:
            # assigning node to its parent and cluster to its node
            list_of_all_nodes[i].parent_cluster = cluster_head
            cluster_head.list_of_nodes.append(list_of_all_nodes[i])

    cluster_heads = CH.Create_clusters()
    cluster_heads = cluster_heads.get_all_cluster_heads()
    [print(j.name, end=" ") for j in cluster_heads]
    print()

    # configuration with multiple nodes
    # assign nodes to the clusters
    dummy_function(cluster_heads[0], [0, 3])
    dummy_function(cluster_heads[1], [3, 4])
    dummy_function(cluster_heads[2], [8, 19])
    dummy_function(cluster_heads[3], [8, 9])
    dummy_function(cluster_heads[4], [2, 5])
    dummy_function(cluster_heads[5], [5, 10, 17])
    dummy_function(cluster_heads[6], [12, 15, 16])

    # # configuration with multiple nodes
    # dummy_function(cluster_heads[0], [0, 1, 2, 3])
    # dummy_function(cluster_heads[1], [3, 4, 5, 13])
    # dummy_function(cluster_heads[2], [1, 2, 8, 19])
    # dummy_function(cluster_heads[3], [7, 8, 9, 18])
    # dummy_function(cluster_heads[4], [2, 5, 6, 7, 10])
    # dummy_function(cluster_heads[5], [5, 10, 11, 12, 13, 14, 17])
    # dummy_function(cluster_heads[6], [12, 14, 15, 16])


    # print all the service provider from the cluster
    for cluster in cluster_heads:
        print("Service provider nodes of cluster ", cluster.name, end=' ')
        for node in cluster.list_of_nodes:
            if node.service_flag:
                print(node.name, "context ", node.set_of_dataContexts, end=" ")
        print()
    return list_of_all_nodes

    # # print all the service consumer nodes from the cluster
    # for cluster in cluster_heads:
    #     print("Service consumer nodes of cluster ", cluster.name, end=' ')
    #     for node in cluster.list_of_nodes:
    #         if not node.service_flag:
    #             print(node.name, end=" ")
    #     print()


















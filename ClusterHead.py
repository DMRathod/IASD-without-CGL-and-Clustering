import pickle
from collections import defaultdict

import numpy as np
import createlatticeee as cgl


def Euclidean_dist(p1, p2):
    return np.sqrt((p2.x_coordinate - p1.x_coordinate) ** 2 + (p2.y_coordinate - p1.y_coordinate) ** 2)

#
# def check_in_CGL(datacontext, cluster_head):
#     # CGL_dict = cgl.CGL([set(i) for i in datacontext])
#     for each in datacontext:
#         if each in cluster_head.CGL.keys():
#             return False
#     return True
#
#
# def store_in_file(CGL_dict, name):
#     db = CGL_dict
#     dbfile = open(name, 'wb')
#     pickle.dump(db, dbfile)
#     dbfile.close()
#
#
# def load_from_file(name):
#     dbfile = open(name, 'rb')
#     db = pickle.load(dbfile)
#     for keys in db:
#         print(keys, "=>", db[keys])
#     dbfile.close()
#     return db
#
#
# def init_CGL(db, name):
#     dbfile = open(name, 'wb')
#     pickle.dump(db, dbfile)
#     dbfile.close()
#     return load_from_file(name)
#
#
# def update_CGL(test_cases, name):
#     first = False
#     for req in test_cases:
#         length_to_node = defaultdict(set)
#         length_to_node[0] = {frozenset()}
#         if first:
#             nodes_to_children = defaultdict(set)
#         else:
#             nodes_to_children = load_from_file(name)
#         nodes_to_children[frozenset()] = set()
#         for node in req:
#             node_len = len(node)
#             length_to_node[node_len].add(frozenset(node))
#             connected_to_atleast_one = False
#             for i in range(node_len-1, -1, -1):
#                 old_nodes = length_to_node[i]
#                 for old_node in old_nodes:
#                     if old_node.issubset(node):
#                         nodes_to_children[frozenset(node)].add(frozenset(old_node))
#                         connected_to_atleast_one = True
#                 if connected_to_atleast_one:
#                     break
#         # print(nodes_to_children)
#         for key, val in nodes_to_children.items():
#             print(f'{list(key)} :::: {[" ".join(i) for i in val]}')
#
#     store_in_file(nodes_to_children, name)
#     return load_from_file(name)
#

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

    if s_exist == False or d_exist == False:
        print("Source or destination Does not exist")
        return

    limitation_factor = 1
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

    def __init__(self, x_coordinate, y_coordinate, name):
        self.list_of_nodes = []
        self.list_of_connectingPoints = []
        self.weights_of_connecting_points = []
        self.name = name
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.CGL = self.initiate_CGL()

    # return after checking if any other valid connecting point or not
    # def include_connecting_points(self, points, bound):
    #     # distance_dict = {}
    #     for each in points:
    #         d = np.sqrt((each.x_coordinate - self.x_coordinate) ** 2 + (each.y_coordinate - self.y_coordinate) ** 2)
    #         print("cluster head", each.name, d)
    #         if d <= bound:
    #             self.list_of_connectingPoint.append(each)
    #     return self.list_of_connectingPoint

    # return the existing list of the connecting points
    def print_connecting_points(self):
        return self.list_of_connectingPoint

    def get_list_of_nodes(self):
        return self.list_of_nodes

    def requirement_to_datacontext(self, service_type):
        # we can assign some predefined datacontext to the services so that it can be used for constructing the CGL
        if service_type == 1:
            return [[{'d3'}, {'d2'}]]





    def service_response(self, service_type,  source, destination):
        datacontext = self.requirement_to_datacontext(service_type)
        context_used_before = self.check_in_CGL(datacontext)
        print(datacontext)
        if not context_used_before:
            self.CGL = self.update_CGL(datacontext)
        print("Updated CGL", context_used_before, self.CGL)


    #wait here

    def check_in_CGL(self, datacontext):
        print("data Conetxt new one:", datacontext)
        CGL_keys = self.CGL.keys()
        for each in datacontext[0]:
            if frozenset(each) in CGL_keys:
                datacontext[0].remove(each)
        print("updated datacontext req", datacontext)



        # CGL_dict = cgl.CGL([set(i) for i in datacontext])
        # print("CGL hai yeh", self.CGL.items())
        return False

    def initiate_CGL(self):
        len_to_node = defaultdict(set)
        len_to_node[0] = {frozenset()}
        db = (len_to_node, defaultdict(set))
        dbfile = open(self.name, 'wb')
        pickle.dump(db, dbfile)
        dbfile.close()
        return self.load_from_file()

    def load_from_file(self):
        dbfile = open(self.name, 'rb')
        db = pickle.load(dbfile)
        # for keys in db:
        #     print(keys, "=>", db[keys])
        dbfile.close()
        return db[1]

    def store_in_file(self, len_to_nodes, CGL_dict):
        db = (len_to_nodes, CGL_dict)
        dbfile = open(self.name, 'wb')
        pickle.dump(db, dbfile)
        dbfile.close()

    def update_CGL(self, test_cases, load_old):
        # first = False
        for req in test_cases:
            if not load_old:
                length_to_node = defaultdict(set)
                length_to_node[0] = {frozenset()}
                nodes_to_children = defaultdict(set)
            else:
                length_to_node, nodes_to_children = self.load_from_file()
                # print(length_to_node, nodes_to_children)
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
            # print(length_to_node)
            for key, val in nodes_to_children.items():
                print(f'{list(key)} :::: {[" ".join(i) for i in val]}')
                # print(f'{list(key)} :::: {[print(va) for va in val]}')
        print("len to node", length_to_node)
        self.store_in_file(length_to_node, nodes_to_children)
        db = self.load_from_file()
        return db



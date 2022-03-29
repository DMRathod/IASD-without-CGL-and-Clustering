from itertools import combinations
import Lattice as L
import numpy as np

def intersection(a, b):
    return a & b


def union(a, b):
    return a | b


def create_powerset(s):
    PowerSet = []
    for i in range(0, len(s) + 1):
        for element in combinations(s, i):
            PowerSet.append(set(element))

    return PowerSet

def create_powerset1(s):
    PowerSet1 = []
    for i in range(0, len(s) + 1):
        for element in combinations(s, i):
            PowerSet1.append(set(element))

    return PowerSet1


def CreateLattice(datacontexts, dict1):
    global flag
    flag = 0
    Power_set = create_powerset(datacontexts)
    r = c = len(Power_set)
    lattice1 = L.Lattice(Power_set, union, intersection)
    hasse_graph = lattice1.Hasse(dict1)
    graph = np.zeros(shape=(r, c), dtype=int)
    dummy_dict = {}
    map_dict = {}
    graph_dict = {frozenset(): []}
    graph_visited = {frozenset(): []}
    i = 0
    # request = [{'d1', 'd3'}, {'d2', 'd3'}, {'d1', 'd2'}, {'d3'}, {'d2', 'd3', 'd1'}]
    request = [{'d2'}, {'d1', 'd2'}, {'d1', 'd2', 'd3'}, {'d1'}]
    # for p, va in dict1.items():
    #     request.append(va)
    print('request:', request)
    def selected_combinations(actual_element, length):
        result = []
        combi = combinations(actual_element, length)
        for i in combi:
            pass


    def recursive_comb(each, actual_element, length):
        temp = []
        f = 0
        if length == 0:
            return
        comb = combinations(each, length)
        for element in comb:
            if frozenset(element) in graph_dict.keys():
                print(bool(graph_dict[frozenset(element)]))
                print(graph_dict[frozenset(element)])
                combi = combinations(actual_element, len(element) + 1)
                # combi1 = selected_combinations(actual_element, len(element)+1)
                for m in combi:
                    if set(element).issubset(set(m)):
                        temp.append(set(m))
                for ele in temp:
                    if ele in graph_dict[frozenset(element)]:
                        f = 1
                if(f == 0):
                    graph_dict[frozenset(element)].append(set(actual_element))
                global flag
                flag = 1
            else:
                recursive_comb(element, actual_element, length - 1)


    for each in request:
        recursive_comb(each, each, len(each)-1)
        if flag == 0:
            graph_dict[frozenset()].append(set(each))
        flag = 0
        if frozenset(each) not in graph_dict.keys():
            graph_dict[frozenset(each)] = []
    # print(graph_dict[frozenset('d2')])
    print(graph_dict)








    # def recursive_comb(each, actual_element, length):
    #     if length == 0:
    #         return
    #         # graph[0][map_dict[str(each)]] = graph[map_dict[str(each)]][0] = 1
    #     comb = combinations(each, length)
    #     comb_result = [set(i) for i in comb]
    #     for i in comb_result:
    #         row = graph[map_dict[str(i)]]
    #         if 1 in row:
    #             graph[map_dict[str(actual_element)]][map_dict[str(i)]] = 1
    #             graph[map_dict[str(i)]][map_dict[str(actual_element)]] = 1
    #     if 1 not in graph[map_dict[str(actual_element)]]:
    #         for j in comb_result:
    #             recursive_comb(j, actual_element, length-1)
    #     else:
    #         return
    #
    # for each in Power_set:
    #     map_dict[str(each)] = i
    #     i += 1
    # for key, values in hasse_graph.items():
    #     for v in values:
    #         graph[key][v] = graph[v][key] = 2
    #     dummy_dict[key] = {}
    # for each in request:
    #     if len(each) == 1:
    #         graph[0][map_dict[str(each)]] = graph[map_dict[str(each)]][0] = 1
    #     else:
    #         recursive_comb(each, each, len(each)-1)
    #         if 1 not in graph[map_dict[str(each)]]:
    #             graph[map_dict[str(each)]][0] = graph[0][map_dict[str(each)]] = 1

            # graph[map_dict[str(each)]][0] = graph[0][map_dict[str(each)]] = 1







            # length = len(each) - 1
            # comb = combinations(each, len(each)-1)
            # comb_result = [set(i) for i in comb]
            # for i in comb_result:
            #     row = graph[map_dict[str(i)]]
            #     if 1 in row:
            #         graph[map_dict[str(each)]][map_dict[str(i)]] = 1
            #         graph[map_dict[str(i)]][map_dict[str(each)]] = 1






            # print('result :', comb_result)
            # pass



    # print('dummy :',  dummy_dict)
    # print('map :', map_dict)
    # print('graph :', graph)


    # print("Bottom Element : ", lattice1.BottonElement, "Top Element : ", lattice1.TopElement)


def activate_points(Service_dict):
    # Remove(Service_dict)
    # print(Service_dict)
    dotcode = ''
    # Uelements = L.Lattice.get_uelements()
    # for s, ds in graph.items():
            # for d in ds:
    for s in Service_dict.keys():
        dotcode += "\""+str(set())+"\""
        dotcode += " -> "
        dotcode += "\""+str(Service_dict[s])+"\""
        dotcode += "[arrowhead=none ];\n"
    return dotcode

# def Creation_L(s):




    # pass

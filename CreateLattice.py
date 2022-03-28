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


def CreateLattice(datacontexts, dict1):
    Power_set = create_powerset(datacontexts)
    lattice1 = L.Lattice(Power_set, union, intersection)
    hasse_graph = lattice1.Hasse(dict1)
    r = c = len(Power_set)
    graph = np.zeros(shape=(r, c), dtype=int)
    dummy_dict = {}
    map_dict = {}
    i = 0
    # request = [{'d1', 'd3'}, {'d2', 'd3'}, {'d1', 'd2'}, {'d3'}, {'d2', 'd3', 'd1'}]
    request = [{'d2'}, {'d2', 'd1'}, {'d3', 'd1'}, {'d2', 'd3'}, {'d2', 'd3', 'd1', 'd4'}]
    # for p, va in dict1.items():
    #     request.append(va)
    print('request:', request)

    def recursive_comb(each, actual_element, length):
        if length == 0:
            return
            # graph[0][map_dict[str(each)]] = graph[map_dict[str(each)]][0] = 1
        comb = combinations(each, length)
        comb_result = [set(i) for i in comb]
        for i in comb_result:
            row = graph[map_dict[str(i)]]
            if 1 in row:
                graph[map_dict[str(actual_element)]][map_dict[str(i)]] = 1
                graph[map_dict[str(i)]][map_dict[str(actual_element)]] = 1
        if 1 not in graph[map_dict[str(actual_element)]]:
            for j in comb_result:
                recursive_comb(j, actual_element, length-1)
        else:
            return

    for each in Power_set:
        map_dict[str(each)] = i
        i += 1
    for key, values in hasse_graph.items():
        for v in values:
            graph[key][v] = graph[v][key] = 2
        dummy_dict[key] = {}
    for each in request:
        if len(each) == 1:
            graph[0][map_dict[str(each)]] = graph[map_dict[str(each)]][0] = 1
        else:
            recursive_comb(each, each, len(each)-1)
            if 1 not in graph[map_dict[str(each)]]:
                graph[map_dict[str(each)]][0] = graph[0][map_dict[str(each)]] = 1

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



    print('dummy :',  dummy_dict)
    print('map :', map_dict)
    print('graph :', graph)


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

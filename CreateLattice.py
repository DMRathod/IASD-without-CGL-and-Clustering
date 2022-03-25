from itertools import combinations
import Lattice as L


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
    print(lattice1.Hasse(dict1))
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

# def Remove(Servicedict):
#     service_dict {}
#     for key, value







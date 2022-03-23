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


def CreateLattice(datacontexts):
    Power_set = create_powerset(datacontexts)
    lattice1 = L.Lattice(Power_set, union, intersection)
    print(lattice1.Hasse())
    print("Bottom Element : ", lattice1.BottonElement, "Top Element : ", lattice1.TopElement)









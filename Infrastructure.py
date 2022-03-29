import Node
import Fog
import random


class Infrastructure:
    Edge_nodes = []
    Fog_nodes = []
    Service_set = ['s1', 's2', 's3', 's4', 's5']
    Datacontext_set = ['d1', 'd2', 'd3']
    FID = {'F0', 'F1'}

    def __init__(self, no_of_edge_nodes, no_of_fog_nodes=2):
        for i in range(no_of_edge_nodes):
            self.Edge_nodes.append(Node.Node(f'N{i}', random.sample(self.Service_set, random.randint(1, len(self.Service_set))), random.sample(self.Datacontext_set, random.randint(1, len(self.Datacontext_set))), random.choice(self.FID)))
        for f in range(no_of_fog_nodes):
            self.Fog_nodes.append(Fog.Fog(f'F{f}'))


    def get_clusters(self):
        Fog_dict = {}
        for f in self.FID:
            Fog_dict[f] = []
        for node in self.Edge_nodes:
            if node.FID











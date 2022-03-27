import random


class Node:
    set_of_services = []
    set_of_dataContexts = []

    def __init__(self, ID, S, D):
        self.ID = ID
        self.set_of_services = S
        self.set_of_dataContexts = D
        # self.FID = FID

    def delta(self):
        service_dict = {}
        for s in self.set_of_services:
            print(s, random.sample(self.set_of_dataContexts, random.randint(0, len(self.set_of_dataContexts))))
            service_dict[s] = set(random.sample(self.set_of_dataContexts, random.randint(1, len(self.set_of_dataContexts))))
        return service_dict

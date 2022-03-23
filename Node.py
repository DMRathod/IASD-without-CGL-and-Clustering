import random


class Node:
    set_of_services = []
    set_of_dataContexts = []

    def __init__(self, ID, S, D):
        self.ID = ID
        self.set_of_services = S
        self.set_of_dataContexts = D

    def delta(self):
        for s in self.set_of_services:
            print(s, random.sample(self.set_of_dataContexts, random.randint(0, 3)))




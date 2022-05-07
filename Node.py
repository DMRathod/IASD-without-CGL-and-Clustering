import random
import ClusterHead as CH

class Node:
    set_of_services = []
    set_of_dataContexts = []

    def __init__(self, name, data_context):
        self.name = name
        # if it is False node is service consumer, if it is true node is service provider
        # self.service_flag = random.choice([False, True])
        # assign parent cluster head
        self.parent_cluster = None

        self.service_flag = True
        # self.set_of_services = S
        self.set_of_dataContexts = data_context
        # self.FID = FID

    def delta(self):
        service_dict = {}
        for s in self.set_of_services:
            print(s, random.sample(self.set_of_dataContexts, random.randint(0, len(self.set_of_dataContexts))))
            service_dict[s] = set(random.sample(self.set_of_dataContexts, random.randint(1, len(self.set_of_dataContexts))))
        return service_dict

    def service_request(self, source, destination):
         CH.service_response(self.set_of_dataContexts, self.parent_cluster)
        if not service_served_before:

        CH.get_list_of_clusters()







import random
import cloudservice as Cloudsrvc

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

    # def delta(self):
    #     service_dict = {}
    #     for s in self.set_of_services:
    #         print(s, random.sample(self.set_of_dataContexts, random.randint(0, len(self.set_of_dataContexts))))
    #         service_dict[s] = set(random.sample(self.set_of_dataContexts, random.randint(1, len(self.set_of_dataContexts))))
    #     return service_dict

    def service_request(self, source, destination, intent):
        # print("Self data context", self.set_of_dataContexts)
        service_type = 1
        Cloudsrvc.CloudService.service_response(service_type, source, destination, intent)
        # self.parent_cluster.service_response(service_type, source, destination, intent)
        # CH.get_list_of_clusters()







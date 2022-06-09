import random
from collections import defaultdict
import CreateConnectingPoints as CP
import shortest_path as sp
import sys
import time


class CloudService:
    point_graph = CP.CreateConnectingPoint()
    connecting_point_graph = point_graph.connecting_point_adjacency_list
    list_of_connecting_points = point_graph.get_connecting_points()
    weights_of_connecting_points_dict = defaultdict()

    @staticmethod
    def average_weights(values):
        return sum(values) / len(values)

    @staticmethod
    def validate_service_request(service_type, source, destination):
        source_flag = False
        destination_flag = False
        temp_source = None
        temp_destination = None
        point_source = None
        point_destination = None
        for each in CloudService.list_of_connecting_points:
            if source[0] == each.x_coordinate and source[1] == each.y_coordinate:
                # temp_source = (each.parent_cluster.x_coordinate, each.parent_cluster.y_coordinate)
                point_source = each
                # print("Source Found")
                source_flag = True
            if destination[0] == each.x_coordinate and destination[1] == each.y_coordinate:
                # temp_destination = (each.parent_cluster.x_coordinate, each.parent_cluster.y_coordinate)
                destination_flag = True
                point_destination = each
            # print(each.name, " x: ", each.x_coordinate, " y: ", each.y_coordinate)

        if not source_flag or not destination_flag or service_type != 1:
            sys.exit("Source or Destination point Does not exist or service type does not matched")
        print("Source & Destination Found")
        return point_source, point_destination

    @staticmethod
    def requirement_to_datacontext(service_type):
        # we can assign some predefined datacontext to the services so that it can be used for constructing the CGL that will be accumulated from the individual nodes
        possible_contexts = [[{'d1'}]]
        # possible_contexts = [[{'d1'}], [{'d2'}], [{'d1', 'd2'}], [{'d1', 'd2', 'd3'}], [{'d2'}], [{'d3'}]]
        if service_type == 1:
            d = random.choice(possible_contexts)
            # print("choice is :", d)
            return [d]

    @classmethod
    def compute_connecting_point_weight_from_datacontext(cls, datacontext):
        weights = [2, 3, 4]
        for each in cls.list_of_connecting_points:
            cls.weights_of_connecting_points_dict[each] = random.choice(weights)

    @classmethod
    def assign_weights_to_edges(cls):
        for each in cls.weights_of_connecting_points_dict.keys():
            # print(each.name, end=" ")
            for p in cls.connecting_point_graph[each]:
                if p[0] in cls.weights_of_connecting_points_dict.keys():
                    if p[1] != 0:
                        temp = CloudService.average_weights(
                            [cls.weights_of_connecting_points_dict[each], cls.weights_of_connecting_points_dict[p[0]]])
                        p[1] = CloudService.average_weights([p[1], temp])
                    else:
                        p[1] = CloudService.average_weights(
                            [cls.weights_of_connecting_points_dict[each], cls.weights_of_connecting_points_dict[p[0]]])
        for k, v in cls.connecting_point_graph.items():
            print(k.name, "=>", end='')
            for e in v:
                print(e[1], end=' ')
            print()

    @classmethod
    def service_response(cls, service_type, source, destination, intent):
        timee = [2, 4, 3]
        time.sleep(random.choice(timee))
        p_source, p_destination = CloudService.validate_service_request(service_type, source, destination)
        datacontext = CloudService.requirement_to_datacontext(service_type)
        # We assume that storing each service request datacontext at cloud level is more complex task we will not store anything at cloud level
        CloudService.compute_connecting_point_weight_from_datacontext(datacontext)
        CloudService.assign_weights_to_edges()
        sp.compute_shortest_heuristic_path_with_intent(cls.connecting_point_graph, p_source, p_destination, intent)
        time.sleep(3)

class ConnectingPoint:
    # we may or may not have list of node at connecting point
    list_of_nodes_at_connecting_point = []

    def __init__(self, x_coordinate, y_coordinate, name, intent_id=0):
        self.name = name
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.intent_id = intent_id
        self.parent_cluster = None



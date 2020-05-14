class Flights:
    """ A Value-Object used to hold the different flights a user wants to reserve

    """
    def __init__(self, code, destination, num_clients):  # FIXME: This is supposed to be an aggregation of Flights
        self.code = code
        self.destination = destination
        self.num_clients = num_clients

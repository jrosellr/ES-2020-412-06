class Flight:
    """ A Value-Object to hold flight-related data

    """

    def __init__(self, code: str, destination: str, num_clients: int):
        self.code = code
        self.destination = destination
        self.num_clients = num_clients

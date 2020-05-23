class Flight:
    """ A Value-Object to hold flight-related data
        ----

        Instance variables:
            code: The flight's code

            destination: The flight's destination

            passengers: The flight's number of passengers
    """

    def __init__(self, code: str, destination: str, num_clients: int):
        """ Construct a new Flight object

        :param code: The flight's code
        :param destination: The flight's destination
        :param passengers: The flight's number of passengers
        """
        self.code = code
        self.destination = destination
        self.passengers = num_clients

from src.Flight import Flight


class Flights:
    """ A Value-Object used to hold the different flights a user wants to reserve

    ---

    :var flights: uses a dictionary to enforce the singularity of each flight
    """

    def __init__(self, flights: list):
        """ Creates a dictionary using the flight codes as keys

        :param flights: a list of objects of type Flight
        """
        self.flights = {flight.code: flight for flight in flights}

    def modify_flight(self, code: str, new_destination=None, new_num_clients=None):
        if code in self.flights:
            self.flights[code].destination = new_destination if new_destination else self.flights[code].destination
            self.flights[code].num_clients = new_num_clients if new_num_clients else self.flights[code].num_clients

    def add_flight(self, flight: Flight):
        if flight.code not in self.flights:
            self.flights[flight.code] = flight

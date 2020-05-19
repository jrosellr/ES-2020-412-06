from src.Flight import Flight


class Flights:
    """ A Value-Object that holds the different flights a user wants to reserve

    ----

        Instance variables:
            flights: uses a dictionary to enforce the singularity of each flight
            passengers_per_flight: the number of passengers of each flight
    """

    def __init__(self, flights: list):
        """ Creates a dictionary using the flight codes as keys

        :param flights: a list of objects of type Flight
        """

        if len(flights) != 0:
            self.__flights = {flight.code: flight for flight in flights}
            self.passengers_per_flight: int = flights[0].passengers
        else:
            self.__flights: dict = {}
            self.passengers_per_flight: int = 0

    def __getitem__(self, key: str):
        if key in self.__flights:
            return self.__flights[key]

    def __setitem__(self, key: str, value: Flight):
        if key not in self.__flights:
            self.__flights[key] = value

    def __delitem__(self, key: str):
        if key in self.__flights:
            del self.__flights[key]

    def __len__(self):
        return len(self.__flights)

from src.Flights import Flights
import copy


class Travel:
    """ Class to hold travel information.

        ------

        Public methods:
            get_num_clients(self): accessor

            add_flight(self, new_flight): mutator

            delete_flight(self, code): mutator

        ----

        Instance variables:
            flights: collection of objects of type Flight

            hotels: collection of objects of type Hotel

            cars: collection of objects of type Car
    """

    def __init__(self, flights: Flights, hotels=None, cars=None):
        """ Construct a Travel object

        :param flights: Flights
        :param hotels: Hotels
        :param cars: Cars
        """

        self.flights = copy.deepcopy(flights)
        self.hotels = copy.deepcopy(hotels)
        self.cars = copy.deepcopy(cars)

    def get_num_clients(self) -> int:
        """Return the total number of passengers.

            :return: int
         """

        num_clients = 0
        for code, flight in self.flights.flights.items():
            num_clients += flight.num_clients
        return num_clients

    def add_flight(self, new_flight) -> None:
        """Add a new flight.

            Restrictions:
                The flight should not exist

            :return: None
        """

        self.flights.add_flight(new_flight)

    def delete_flight(self, code) -> None:
        """Delete an existing flight.

            :return: None
        """

        self.flights.delete_flight(code)

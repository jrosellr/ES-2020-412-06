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
            flights

            hotels

            cars
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

    def add_flight(self, new_flight) -> None:
        """Add a new flight.

            Restrictions:
                The flight should not exist

            :return: None
        """

        self.flights[new_flight.code]= new_flight

    def delete_flight(self, code) -> None:
        """Delete an existing flight.

            :return: None
        """

        del self.flights[code]

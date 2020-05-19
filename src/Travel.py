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
            __flights

            __hotels

            __cars
    """

    def __init__(self, flights: Flights):
        """ Construct a Travel object

        :param flights: Flights
        :param hotels: Hotels
        :param cars: Cars
        """

        self._flights = copy.deepcopy(flights)

    def add_flight(self, new_flight) -> None:
        """Add a new flight.

            Restrictions:
                The flight should not exist

            :return: None
        """

        self._flights[new_flight.code] = new_flight

    def delete_flight(self, code) -> None:
        """Delete an existing flight.

            :return: None
        """

        del self._flights[code]

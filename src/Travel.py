from src.Flights import Flights
from src.Hotels import Hotels
from src.Cars import Cars
import copy


class Travel:
    """ Class to hold travel information.

        ------

        Public methods:

            add_flight(self, new_flight): mutator

            delete_flight(self, code): mutator

        Properties:
            cost: the total cost of the Travel

            ticket_price: the price of a single ticket

            room_price: the cost of a single hotel room

            car_price: the cost of a single car

        Property restrictions:
            All properties should be positive float values as they represent prices
    """
    _default_price: float = 0.0

    def __init__(self, num_travelers: int, flights: Flights, hotels: Hotels = None, cars: Cars = None):
        """ Construct a Travel object

        :param num_travelers:
        :param flights: Flights
        :param hotels: Hotels
        :param cars: Cars
        """

        self._flights: Flights = copy.deepcopy(flights)
        self._hotels: Hotels = copy.deepcopy(hotels) if hotels else hotels
        self._cars: Cars = copy.deepcopy(hotels) if cars else cars
        self._num_travelers: int = num_travelers
        self._ticket_price: float = self._default_price
        self._hotel_price: float = self._default_price
        self._car_price: float = self._default_price

    @property
    def has_hotels(self) -> bool:
        return self._hotels is not None

    @property
    def has_cars(self) -> bool:
        return self._cars is not None

    @property
    def ticket_price(self) -> float:
        return self._ticket_price

    @ticket_price.setter
    def ticket_price(self, val):
        if type(val) != float:
            raise TypeError("price should be a float value")

        if val > 0.0:
            self._ticket_price = val
        else:
            raise ValueError("price can't be negative")

    @property
    def hotel_price(self):
        return self._hotel_price

    @hotel_price.setter
    def hotel_price(self, val):
        if type(val) != float:
            raise TypeError("price should be a float value")

        if val > 0.0:
            self._hotel_price = val
        else:
            raise ValueError("price can't be negative")

    @property
    def car_price(self):
        return self._car_price

    @car_price.setter
    def car_price(self, val):
        if type(val) != float:
            raise TypeError("price should be a float value")

        if val > 0.0:
            self._car_price = val
        else:
            raise ValueError("price can't be negative")

    @property
    def cost(self):
        total_ticket_cost = self._calculate_ticket_cost()
        total_hotels_cost = 0.0
        total_cars_cost = 0.0

        if self.has_hotels:
            total_hotels_cost = self._calculate_hotels_cost()
        if self.has_cars:
            total_cars_cost = self._calculate_cars_cost()

        return total_ticket_cost + total_hotels_cost + total_cars_cost

    def _calculate_ticket_cost(self) -> float:
        """ Calculate the total cost of the flights

        :return: total cost of the flights
        """

        return self._ticket_price * self._num_travelers * len(self._flights)

    def _calculate_hotels_cost(self) -> float:
        """ Calculate the total cost of the hotels

        Hotel price is the subtotal price of an Hotel, retrieved directly from Booking.
        This price takes into account the number of days and number of travelers.

        The cost formula for all the Hotels is: hotel price * number of hotels

        :return: total cost of the flights
        """

        return self._hotel_price * len(self._hotels)

    def _calculate_cars_cost(self) -> float:
        """ Calculate the total cost of the cars

        Car price is the subtotal price of a Car, retrieved directly from Rentalcars.
        This price takes into account the number of days and number of travelers.

        The cost formula for all the Cars is: car price * number of cars

        :return: total cost of the flights
        """

        return self._car_price * len(self._cars)

from src.Travel import Travel
from src.Flights import Flights
from src.Hotels import Hotels
from src.Cars import Cars
from .test_constants import *
import pytest

# TODO: improve test documentation


def test_travel_ctor(default_flights: Flights):
    """ Test case for Travel.__init__(**) method with Flights

    RESTRICTION:
        The Flights instance should have elements in.

    TEST CASE:
        Insertion of a Travel object from Flights instance and number of travelers.

    EXPECTED BEHAVIOUR:
        The object is instantiated with the default values of Flights.
    """

    travel = Travel(DEFAULT_NUM_TRAVELERS, default_flights)

    assert isinstance(travel, Travel)

    assert len(travel._flights) != 0
    assert len(travel._flights) == len(default_flights)

    assert travel.ticket_price == travel._default_price
    assert travel.hotel_price == travel._default_price
    assert travel.car_price == travel._default_price
    assert travel.cost == float()


def test_full_travel_ctor(default_flights: Flights, default_hotels: Hotels, default_cars: Cars):
    """ Test case for Travel.__init__(**) method with Flights, Hotels and Cars

    RESTRICTION:
        The Flights, Hotels and Cars instances should have elements in.

    TEST CASE:
        Insertion of a Travel object from Flights, Hotels, Cars instances and number of travelers.

    EXPECTED BEHAVIOUR:
        The object is instantiated with the default values of Flights, Hotels and Cars.
    """

    travel = Travel(DEFAULT_NUM_TRAVELERS, default_flights, default_hotels, default_cars)

    assert isinstance(travel, Travel)

    assert len(travel._flights) != 0
    assert len(travel._hotels) != 0
    assert len(travel._cars) != 0
    assert len(travel._flights) == len(default_flights)
    assert len(travel._hotels) == len(default_hotels)
    assert len(travel._cars) == len(default_cars)

    assert travel.ticket_price == travel._default_price
    assert travel.hotel_price == travel._default_price
    assert travel.car_price == travel._default_price
    assert travel.cost == float()


def test_travel_set_positive_value_to_ticket_property(default_travel: Travel):
    """ Test case for Travel.ticket_price and Travel._ticket_price methods

    TEST CASE:
        Calling ticket_price method to set a flight price and _ticked_price to get that price.

    EXPECTED BEHAVIOUR:
        The methods set and get the prices for a flight correctly.
    """

    default_travel.ticket_price = 5.0

    assert default_travel._ticket_price != 0.0
    assert default_travel._ticket_price == 5.0


def test_travel_set_negative_value_to_ticket_property(default_travel: Travel):
    """ Test case for incorrect Travel.ticket_price method use

    TEST CASE:
        Calling ticket_price method to set a negative flight price.

    EXPECTED BEHAVIOUR:
        The method raise a ValueError exception because the price is negative.
    """

    with pytest.raises(ValueError):
        default_travel.ticket_price = -1.0


def test_travel_set_positive_value_to_room_property(default_travel: Travel):
    """ Test case for Travel.hotel_price and Travel._hotel_price methods

    TEST CASE:
        Calling hotel_price method to set a hotel price and _hotel_price to get that price.

    EXPECTED BEHAVIOUR:
        The methods set and get the prices for a hotel correctly.
    """

    default_travel.hotel_price = 5.0

    assert default_travel._hotel_price != 0.0
    assert default_travel._hotel_price == 5.0


def test_travel_set_negative_value_to_room_property(default_travel: Travel):
    """ Test case for incorrect Travel.hotel_price method use

    TEST CASE:
        Calling hotel_price method to set a negative hotel price.

    EXPECTED BEHAVIOUR:
        The method raise a ValueError exception because the price is negative.
    """

    with pytest.raises(ValueError):
        default_travel.hotel_price = -1.0


def test_travel_set_positive_value_to_car_property(default_travel: Travel):
    """ Test case for Travel.car_price and Travel._car_price methods

    TEST CASE:
        Calling car_price method to set a car price and _car_price to get that price.

    EXPECTED BEHAVIOUR:
        The methods set and get the prices for a car correctly.
    """

    default_travel.car_price = 5.0

    assert default_travel._car_price != 0.0
    assert default_travel._car_price == 5.0


def test_travel_set_negative_value_to_car_property(default_travel: Travel):
    """ Test case for incorrect Travel.car_price method use

    TEST CASE:
        Calling car_price method to set a negative car price.

    EXPECTED BEHAVIOUR:
        The method raise a ValueError exception because the price is negative.
    """

    with pytest.raises(ValueError):
        default_travel.car_price = -1.0


def test_travel_ticket_price_set_wrong_type(default_travel: Travel):
    """ Test case for incorrect Travel.ticket_price method use

    TEST CASE:
        Calling ticked_price method to set non float flight price.

    EXPECTED BEHAVIOUR:
        The method raise a TypeError exception because the price is non float.
    """

    with pytest.raises(TypeError):
        default_travel.ticket_price = 5


def test_travel_room_price_set_wrong_type(default_travel: Travel):
    """ Test case for incorrect Travel.hotel_price method use

    TEST CASE:
        Calling hotel_price method to set non float hotel price.

    EXPECTED BEHAVIOUR:
        The method raise a TypeError exception because the price is non float.
    """

    with pytest.raises(TypeError):
        default_travel.hotel_price = 5


def test_travel_car_price_set_wrong_type(default_travel: Travel):
    """ Test case for incorrect Travel.car_price method use

    TEST CASE:
        Calling car_price method to set non float car price.

    EXPECTED BEHAVIOUR:
        The method raise a TypeError exception because the price is non float.
    """

    with pytest.raises(TypeError):
        default_travel.car_price = 5


def test_travel_cost_only_flights(default_travel: Travel):
    """ Test case for Travel.cost method with Flights

    TEST CASE:
        Calling cost method to check the total cost with only an instance of Flights

    EXPECTED BEHAVIOUR:
        The method returns only the cost of the flights.
        Expected cost = num_flights * passengers_per_flight * ticket_price
    """

    default_travel.ticket_price = MOCKED_TICKET_PRICE

    assert default_travel.cost == DEFAULT_FLIGHT_TOTAL_COST


def test_travel_cost_hotels(default_travel: Travel, default_hotels):
    """ Test cost property

        Tests if the calculated cost is equal to the expected cost
        with well-formed input.

        Expected cost = num_flights * passengers_per_flight * ticket_price

        :return: None
    """

    """ Test case for Travel.cost method with Flights and Hotels

    TEST CASE:
        Calling cost method to check the total cost with only an instances of Flights and Hotels

    EXPECTED BEHAVIOUR:
        The method returns only the sum of flights cost and hotels cost.
    """

    default_travel.ticket_price = MOCKED_TICKET_PRICE
    default_travel.hotel_price = MOCKED_HOTEL_PRICE
    default_travel._hotels = default_hotels

    assert default_travel.cost == DEFAULT_FLIGHT_TOTAL_COST + DEFAULT_HOTEL_TOTAL_COST


def test_travel_cost_cars(default_travel: Travel, default_cars):
    """ Test case for Travel.cost method with Flights and Cars

    TEST CASE:
        Calling cost method to check the total cost with only an instances of Flights and Cars

    EXPECTED BEHAVIOUR:
        The method returns only the sum of flights cost and cars cost.
    """

    default_travel.ticket_price = MOCKED_TICKET_PRICE
    default_travel.car_price = MOCKED_CAR_PRICE
    default_travel._cars = default_cars

    assert default_travel.cost == DEFAULT_FLIGHT_TOTAL_COST + DEFAULT_CAR_TOTAL_COST


def test_full_travel_cost(default_travel: Travel, default_hotels, default_cars):
    """ Test case for Travel.cost method with Flights, Hotels and Cars

    TEST CASE:
        Calling cost method to check the total cost with only an instances of Flights, Hotels and Cars

    EXPECTED BEHAVIOUR:
        The method returns only the sum of flights cost, hotels cost and cars cost.
    """

    default_travel.ticket_price = MOCKED_TICKET_PRICE
    default_travel.hotel_price = MOCKED_HOTEL_PRICE
    default_travel.car_price = MOCKED_CAR_PRICE
    default_travel._hotels = default_hotels
    default_travel._cars = default_cars

    assert default_travel.cost == DEFAULT_FLIGHT_TOTAL_COST + DEFAULT_CAR_TOTAL_COST + DEFAULT_HOTEL_TOTAL_COST


def test_travel_cost_cannot_be_set(default_travel: Travel):
    """ Test case for invalid Travel.cost set

    TEST CASE:
        Set a value to Travel.cost as if it was a variable

    EXPECTED BEHAVIOUR:
        The method raises an AttributeError exception.
    """

    with pytest.raises(AttributeError):
        default_travel.cost = float()

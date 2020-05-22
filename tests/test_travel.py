from src.Travel import Travel
from src.Flights import Flights
from src.Hotels import Hotels
from src.Cars import Cars
from .test_constants import *
import pytest

# TODO: improve test documentation


def test_travel_ctor(default_flights: Flights):
    """ Test Travel constructor

    Tests correct initialization of all Travel properties and Instance Attributes

    :return: None
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
    """ Test Travel constructor

    Tests correct initialization of all Travel properties and Instance Attributes

    :return: None
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
    """ Test ticket property setter

        Tests ticket property setter when using a positive value,
        we expect the property value to be the set value

        :return: None
    """

    default_travel.ticket_price = 5.0

    assert default_travel._ticket_price != 0.0
    assert default_travel._ticket_price == 5.0


def test_travel_set_negative_value_to_ticket_property(default_travel: Travel):
    """ Test ticket property setter

        Tests ticket property setter when using a negative value,
        we expect to raise a ValueError exception

        :return: None
    """

    with pytest.raises(ValueError):
        default_travel.ticket_price = -1.0


def test_travel_set_positive_value_to_room_property(default_travel: Travel):
    """ Test room property setter

        Tests room property setter when using a positive value,
        we expect the property value to be the set value

        :return: None
    """

    default_travel.hotel_price = 5.0

    assert default_travel._hotel_price != 0.0
    assert default_travel._hotel_price == 5.0


def test_travel_set_negative_value_to_room_property(default_travel: Travel):
    """ Test room property setter

        Tests room property setter when using a negative value,
        we expect to raise a ValueError exception

        :return: None
    """

    with pytest.raises(ValueError):
        default_travel.hotel_price = -1.0


def test_travel_set_positive_value_to_car_property(default_travel: Travel):
    """ Test car property setter

        Tests car property setter when using a positive value,
        we expect the property value to be the set value

        :return: None
    """

    default_travel.car_price = 5.0

    assert default_travel._car_price != 0.0
    assert default_travel._car_price == 5.0


def test_travel_set_negative_value_to_car_property(default_travel: Travel):
    """ Test car property setter

        Tests car property setter when using a negative value,
        we expect to raise an ValueError exception

        :return: None
    """

    with pytest.raises(ValueError):
        default_travel.car_price = -1.0


def test_travel_ticket_price_set_wrong_type(default_travel: Travel):
    """ Test ticket property setter

        Tests ticket property setter when using a value which is not of type float,
        we expect to raise an TypeError exception

        :return: None
    """

    with pytest.raises(TypeError):
        default_travel.ticket_price = 5


def test_travel_room_price_set_wrong_type(default_travel: Travel):
    """ Test room property setter

        Tests room property setter when using a value which is not of type float,
        we expect to raise an TypeError exception

        :return: None
    """

    with pytest.raises(TypeError):
        default_travel.hotel_price = 5


def test_travel_car_price_set_wrong_type(default_travel: Travel):
    """ Test car property setter

        Tests car property setter when using a value which is not of type float,
        we expect to raise an TypeError exception

        :return: None
    """

    with pytest.raises(TypeError):
        default_travel.car_price = 5


def test_travel_cost_only_flights(default_travel: Travel):
    """ Test cost property

        Tests if the calculated cost is equal to the expected cost
        with well-formed input.

        Expected cost = num_flights * passengers_per_flight * ticket_price

        :return: None
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

    default_travel.ticket_price = MOCKED_TICKET_PRICE
    default_travel.hotel_price = MOCKED_HOTEL_PRICE
    default_travel._hotels = default_hotels

    assert default_travel.cost == DEFAULT_FLIGHT_TOTAL_COST + DEFAULT_HOTEL_TOTAL_COST


def test_travel_cost_cars(default_travel: Travel, default_cars):
    """ Test cost property

        Tests if the calculated cost is equal to the expected cost
        with well-formed input.

        Expected cost = num_flights * passengers_per_flight * ticket_price

        :return: None
    """

    default_travel.ticket_price = MOCKED_TICKET_PRICE
    default_travel.car_price = MOCKED_CAR_PRICE
    default_travel._cars = default_cars

    assert default_travel.cost == DEFAULT_FLIGHT_TOTAL_COST + DEFAULT_CAR_TOTAL_COST


def test_full_travel_cost(default_travel: Travel, default_hotels, default_cars):
    """ Test cost property

        Tests if the calculated cost is equal to the expected cost
        with well-formed input.

        Expected cost = num_flights * passengers_per_flight * ticket_price

        :return: None
    """

    default_travel.ticket_price = MOCKED_TICKET_PRICE
    default_travel.hotel_price = MOCKED_HOTEL_PRICE
    default_travel.car_price = MOCKED_CAR_PRICE
    default_travel._hotels = default_hotels
    default_travel._cars = default_cars

    assert default_travel.cost == DEFAULT_FLIGHT_TOTAL_COST + DEFAULT_CAR_TOTAL_COST + DEFAULT_HOTEL_TOTAL_COST


def test_travel_cost_cannot_be_set(default_travel: Travel):
    """ Test cost property setter

        Tests cost property setter when setting a value, it should raise
        an AttributeError exception

        :return: None
    """

    with pytest.raises(AttributeError):
        default_travel.cost = float()

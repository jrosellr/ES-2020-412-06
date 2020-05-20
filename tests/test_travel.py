from src.Travel import Travel
from src.Flights import Flights
from src.Flight import Flight
from .test_constants import *
import pytest


def test_travel_ctor(default_flights: Flights):
    """ Test Travel constructor

    Tests correct initialization of all Travel properties and Instance Attributes

    :return: None
    """

    travel = Travel(default_flights)

    assert isinstance(travel, Travel)
    assert len(travel._flights) != 0
    assert travel.ticket_price == travel._default_price
    assert travel.room_price == travel._default_price
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

    default_travel.room_price = 5.0

    assert default_travel._room_price != 0.0
    assert default_travel._room_price == 5.0


def test_travel_set_negative_value_to_room_property(default_travel: Travel):
    """ Test room property setter

        Tests room property setter when using a negative value,
        we expect to raise a ValueError exception

        :return: None
    """

    with pytest.raises(ValueError):
        default_travel.room_price = -1.0


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
        default_travel.room_price = 5


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


def test_travel_cost_cannot_be_set(default_travel: Travel):
    """ Test cost property setter

        Tests cost property setter when setting a value, it should raise
        an AttributeError exception

        :return: None
    """

    with pytest.raises(AttributeError):
        default_travel.cost = float()

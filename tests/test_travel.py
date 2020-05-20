from src.Travel import Travel
from src.Flights import Flights
from src.Flight import Flight
import pytest


def test_travel_ctor():
    """ Test Travel constructor

    Tests correct initialization of all Travel properties and Instance Attributes

    :return: None
    """

    flights = Flights([
        Flight('00', '', 0)
    ])
    travel = Travel(flights)
    assert isinstance(travel, Travel)
    assert len(travel._flights) != 0
    assert travel.ticket_price == float()
    assert travel.room_price == float()
    assert travel.car_price == float()
    assert travel.cost == float()


def test_travel_set_positive_value_to_ticket_property():
    """ Test ticket property setter

        Tests ticket property setter when using a positive value,
        we expect the property value to be the set value

        :return: None
    """

    flights = Flights([
        Flight('00', '', 0)
    ])
    travel = Travel(flights)
    travel.ticket_price = 5.0
    assert travel._ticket_price != 0.0
    assert travel._ticket_price == 5.0


def test_travel_set_negative_value_to_ticket_property():
    """ Test ticket property setter

        Tests ticket property setter when using a negative value,
        we expect to raise a ValueError exception

        :return: None
    """

    flights = Flights([
        Flight('00', '', 0)
    ])
    travel = Travel(flights)

    with pytest.raises(ValueError):
        travel.ticket_price = -1.0


def test_travel_set_positive_value_to_room_property():
    """ Test room property setter

        Tests room property setter when using a positive value,
        we expect the property value to be the set value

        :return: None
    """

    flights = Flights([
        Flight('00', '', 0)
    ])
    travel = Travel(flights)
    travel.room_price = 5.0
    assert travel._room_price != 0.0
    assert travel._room_price == 5.0


def test_travel_set_negative_value_to_room_property():
    """ Test room property setter

        Tests room property setter when using a negative value,
        we expect to raise a ValueError exception

        :return: None
    """

    flights = Flights([
        Flight('00', '', 0)
    ])
    travel = Travel(flights)

    with pytest.raises(ValueError):
        travel.room_price = -1.0


def test_travel_set_positive_value_to_car_property():
    """ Test car property setter

        Tests car property setter when using a positive value,
        we expect the property value to be the set value

        :return: None
    """

    flights = Flights([
        Flight('00', '', 0)
    ])
    travel = Travel(flights)
    travel.car_price = 5.0
    assert travel._car_price != 0.0
    assert travel._car_price == 5.0


def test_travel_set_negative_value_to_car_property():
    """ Test car property setter

        Tests car property setter when using a negative value,
        we expect to raise an ValueError exception

        :return: None
    """

    flights = Flights([
        Flight('00', '', 0)
    ])
    travel = Travel(flights)

    with pytest.raises(ValueError):
        travel.car_price = -1.0


def test_travel_ticket_price_set_wrong_type():
    """ Test ticket property setter

        Tests ticket property setter when using a value which is not of type float,
        we expect to raise an TypeError exception

        :return: None
    """

    flights = Flights([
        Flight('00', '', 0)
    ])
    travel = Travel(flights)
    with pytest.raises(TypeError):
        travel.ticket_price = 5


def test_travel_room_price_set_wrong_type():
    """ Test room property setter

        Tests room property setter when using a value which is not of type float,
        we expect to raise an TypeError exception

        :return: None
    """

    flights = Flights([
        Flight('00', '', 0)
    ])
    travel = Travel(flights)
    with pytest.raises(TypeError):
        travel.room_price = 5


def test_travel_car_price_set_wrong_type():
    """ Test car property setter

        Tests car property setter when using a value which is not of type float,
        we expect to raise an TypeError exception

        :return: None
    """

    flights = Flights([
        Flight('00', '', 0)
    ])
    travel = Travel(flights)
    with pytest.raises(TypeError):
        travel.car_price = 5


def test_travel_cost_only_flights():
    """ Test cost property

        Tests if the calculated cost is equal to the expected cost
        with well-formed input.

        Expected cost = num_flights * passengers_per_flight * ticket_price

        :return: None
    """

    passengers = 5
    num_flights = 2
    ticket_price = 5.0
    expected_cost = passengers * num_flights * ticket_price
    flights = Flights([
        Flight('00', '', passengers),
        Flight('01', '', passengers)
    ])

    travel = Travel(flights)
    travel.ticket_price = ticket_price

    assert travel.cost == expected_cost


def test_travel_cost_cannot_be_set():
    """ Test cost property setter

        Tests cost property setter when setting a value, it should raise
        an AttributeError exception

        :return: None
    """

    passengers = 2
    flights = Flights([
        Flight('00', '', passengers),
        Flight('01', '', passengers)
    ])

    travel = Travel(flights)
    with pytest.raises(AttributeError):
        travel.cost = float()

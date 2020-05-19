from src.Travel import Travel
from src.Flights import Flights
from src.Flight import Flight


def test_travel_ctor():
    """ Test Travel constructor

    :return: None
    """

    flights = Flights([
        Flight('00', '', 0)
    ])
    travel = Travel(flights)
    assert isinstance(travel, Travel)
    assert len(travel._flights) != 0


def test_travel_add_flight_empty_flights():
    """ Test add_flight when there are no flights

    :return: None
    """

    new_flight = Flight('00', '', 0)
    flights = Flights([])
    travel = Travel(flights)
    travel.add_flight(new_flight)
    assert len(travel._flights) != 0
    assert len(travel._flights) == 1


def test_add_flight_same_flight():
    """ Test add_flight when we try to add the same flight two times

    :return: None
    """

    new_flight = Flight('00', '', 0)
    flights = Flights([Flight('00', '', 0)])
    travel = Travel(flights)
    old_len = len(travel._flights)
    travel.add_flight(new_flight)
    assert old_len != 0
    assert len(travel._flights) == old_len


def test_add_flight_new_flight():
    """ Test add_flight when we add a new flight and there are other flights

    :return: None
    """

    new_flight = Flight('01', '', 0)
    flights = Flights([Flight('00', '', 0)])
    travel = Travel(flights)
    old_len = len(travel._flights)
    travel.add_flight(new_flight)
    assert old_len != 0
    assert len(travel._flights) != old_len
    assert len(travel._flights) == old_len + 1


def test_travel_delete_flight_existing_flight():
    """ Test delete_flight on an existing flight

    :return: None
    """

    flights = Flights([
        Flight('00', '', 4),
        Flight('01', '', 4)
    ])
    travel = Travel(flights)
    travel.delete_flight('00')
    assert len(travel._flights) != 2
    assert len(travel._flights) == 1


def test_travel_delete_flight_non_existing_flight():
    """ Test delete_flight on a flight that doesn't exist

        :return: None
    """

    flights = Flights([
        Flight('00', '', 4),
        Flight('01', '', 4)
    ])
    travel = Travel(flights)
    travel.delete_flight('03')
    assert len(travel._flights) == 2
    assert len(travel._flights) != 1

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
    assert len(travel.flights.flights) != 0


def test_travel_add_flight_empty_flights():
    """ Test add_flight when there are no flights

    :return: None
    """

    new_flight = Flight('00', '', 0)
    flights = Flights([])
    travel = Travel(flights)
    travel.add_flight(new_flight)
    assert len(travel.flights.flights) != 0
    assert len(travel.flights.flights) == 1


def test_add_flight_same_flight():
    """ Test add_flight when we try to add the same flight two times

    :return: None
    """

    new_flight = Flight('00', '', 0)
    flights = Flights([Flight('00', '', 0)])
    travel = Travel(flights)
    old_len = len(travel.flights.flights)
    travel.add_flight(new_flight)
    assert old_len != 0
    assert len(travel.flights.flights) == old_len


def test_add_flight_new_flight():
    """ Test add_flight when we add a new flight and there are other flights

    :return: None
    """

    new_flight = Flight('01', '', 0)
    flights = Flights([Flight('00', '', 0)])
    travel = Travel(flights)
    old_len = len(travel.flights.flights)
    travel.add_flight(new_flight)
    assert old_len != 0
    assert len(travel.flights.flights) != old_len
    assert len(travel.flights.flights) == old_len + 1


def test_travel_get_num_clients_no_flights():
    """ Test get_num_clients when we call it on an empty travel

    :return: None
    """

    flights = Flights([])
    travel = Travel(flights)
    assert travel.get_num_clients() == 0


def test_travel_get_num_clients_no_clients():
    """ Test get_num_clients when we call it on travel with flights with no clients

        :return: None
    """

    flights = Flights([
        Flight('00', '', 0),
        Flight('01', '', 0)
    ])
    travel = Travel(flights)
    assert travel.get_num_clients() == 0


def test_travel_get_num_clients():
    """ Test get_num_clients when we call it on travel with flights with clients

        :return: None
    """

    flights = Flights([
        Flight('00', '', 4),
        Flight('01', '', 4)
    ])
    travel = Travel(flights)
    assert travel.get_num_clients() == 8


def test_travel_get_num_clients_add_flight():
    """ Test get_num_clients when we call it on travel after adding a new flight

        :return: None
    """

    flights = Flights([
        Flight('00', '', 4),
        Flight('01', '', 4)
    ])
    travel = Travel(flights)
    travel.add_flight(Flight('02', '', 4))
    assert travel.get_num_clients() == 12


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
    assert len(travel.flights.flights) != 2
    assert len(travel.flights.flights) == 1


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
    assert len(travel.flights.flights) == 2
    assert len(travel.flights.flights) != 1

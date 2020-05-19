from src.Flight import Flight
from src.Flights import Flights


def test_flights_ctor():
    """ Test case for flights.__init__(**) method

        ---

        :return: None
    """

    f1 = Flight('00', 'Berlin', 4)
    f2 = Flight('01', 'Berlin', 4)
    f3 = Flight('03', 'Berlin', 4)
    flights = Flights([f1, f2, f3])
    assert len(flights) != 0
    assert len(flights) == 3
    assert flights.passengers_per_flight == 4

    f1 = Flight('00', 'Berlin', 4)
    f2 = Flight('00', 'Berlin', 4)
    f3 = Flight('00', 'Berlin', 4)
    flights = Flights([f1, f2, f3])
    assert len(flights) != 0
    assert len(flights) != 3
    assert len(flights) == 1
    assert flights.passengers_per_flight == 4


def test_setitem_same_flight():
    new_flight = Flight('00', '', 0)
    flights = Flights([Flight('00', '', 0)])
    old_len = len(flights)
    flights[new_flight.code] = new_flight
    assert old_len != 0
    assert len(flights) == old_len


def test_setitem_new_flight():
    new_flight = Flight('01', '', 0)
    flights = Flights([Flight('00', '', 0)])
    old_len = len(flights)
    flights[new_flight.code] = new_flight
    assert old_len != 0
    assert len(flights) != old_len
    assert len(flights) == old_len + 1


def test_delitem_existing_flight():
    flights = Flights([Flight('00', '', 0)])
    del flights['00']
    assert len(flights) == 0


def test_delitem_non_existing_flight():
    flights = Flights([Flight('00', '', 0)])
    del flights['01']
    assert len(flights) != 0
    assert len(flights) == 1

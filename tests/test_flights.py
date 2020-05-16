from src.Flight import Flight
from src.Flights import Flights


def test_flights_ctor():
    """ Test case for flight.__init__(**) method

        ---

        :return: None
    """
    f1 = Flight('00', 'Berlin', 4)
    f2 = Flight('01', 'Berlin', 4)
    f3 = Flight('03', 'Berlin', 4)
    flights = Flights([f1, f2, f3])
    assert len(flights.flights) != 0
    assert len(flights.flights) == 3

    f1 = Flight('00', 'Berlin', 4)
    f2 = Flight('00', 'Berlin', 4)
    f3 = Flight('00', 'Berlin', 4)
    flights = Flights([f1, f2, f3])
    assert len(flights.flights) != 0
    assert len(flights.flights) != 3
    assert len(flights.flights) == 1


def test_modify_flight_destination():
    """ Test case for modify_flight(**) method

        ---

        :return: None
    """

    f1 = Flight('00', 'Berlin', 4)
    f2 = Flight('01', 'Berlin', 4)
    f3 = Flight('03', 'Berlin', 4)
    flights = Flights([f1, f2, f3])
    flights.modify_flight('00', new_destination='Roma')
    assert flights.flights['00'].destination != 'Berlin'
    assert flights.flights['00'].destination == 'Roma'
    assert flights.flights['00'].num_clients == 4


def test_modify_flight_num_clients():
    """ Test case for modify_flight(**) method

        ---

        :return: None
    """

    f1 = Flight('00', 'Berlin', 4)
    f2 = Flight('01', 'Berlin', 4)
    f3 = Flight('03', 'Berlin', 4)
    flights = Flights([f1, f2, f3])

    flights.modify_flight('00', new_num_clients=2)
    assert flights.flights['00'].num_clients != 4
    assert flights.flights['00'].num_clients == 2
    assert flights.flights['00'].destination == 'Berlin'


def test_modify_flight_all_params():
    """ Test case for modify_flight(**) method

        ---

        :return: None
    """

    f1 = Flight('00', 'Berlin', 4)
    f2 = Flight('01', 'Berlin', 4)
    f3 = Flight('03', 'Berlin', 4)
    flights = Flights([f1, f2, f3])

    flights.modify_flight('00', new_destination='Stockholm', new_num_clients=5)
    assert flights.flights['00'].destination != 'Berlin'
    assert flights.flights['00'].destination == 'Stockholm'
    assert flights.flights['00'].num_clients != 4
    assert flights.flights['00'].num_clients == 5


def test_modify_flight_invalid_code():
    """ Test case for modify_flight(**) method

        ---

        :return: None
    """
    f1 = Flight('00', 'Berlin', 4)
    f2 = Flight('01', 'Berlin', 4)
    f3 = Flight('03', 'Berlin', 4)
    flights = Flights([f1, f2, f3])

    flights.modify_flight('04', new_destination='Stockholm', new_num_clients=5)
    assert '05' not in flights.flights

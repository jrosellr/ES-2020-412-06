from src.Flight import Flight
from src.Flights import Flights


def test_init():
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


def test_modify_flight():
    """ Test suite for modify_flight(**) method

    ---
    Tests three main usage cases:
    *   We want to modify one attribute only
    *   We want to modify many attributes at the same time
    *   We want to modify a non-existing flight

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

    flights.modify_flight('00', new_num_clients=2)
    assert flights.flights['00'].num_clients != 4
    assert flights.flights['00'].num_clients == 2
    assert flights.flights['00'].destination == 'Roma'

    flights.modify_flight('00', new_destination='Stockholm', new_num_clients=5)
    assert flights.flights['00'].destination != 'Roma'
    assert flights.flights['00'].destination == 'Stockholm'
    assert flights.flights['00'].num_clients != 2
    assert flights.flights['00'].num_clients == 5

    flights.modify_flight('05', new_destination='Stockholm', new_num_clients=5)
    assert '05' not in flights.flights

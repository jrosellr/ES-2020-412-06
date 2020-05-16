from src.Travel import Travel
from src.Flights import Flights
from src.Flight import Flight


def test_travel_ctor():
    flights = Flights([
        Flight('00', '', 0)
    ])
    travel = Travel(flights)
    assert isinstance(travel, Travel)
    assert len(travel.flights.flights) != 0


def test_travel_get_num_clients_no_flights():
    flights = Flights([])
    travel = Travel(flights)
    assert travel.get_num_clients() == 0


def test_travel_get_num_clients_no_clients():
    flights = Flights([
        Flight('00', '', 0),
        Flight('01', '', 0)
    ])
    travel = Travel(flights)
    assert travel.get_num_clients() == 0


def test_travel_get_num_clients():
    flights = Flights([
        Flight('00', '', 4),
        Flight('01', '', 4)
    ])
    travel = Travel(flights)
    assert travel.get_num_clients() == 8

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


def test_travel_add_flight_empty_flights():
    new_flight = Flight('00', '', 0)
    flights = Flights([])
    travel = Travel(flights)
    travel.add_flight(new_flight)
    assert len(travel.flights.flights) != 0
    assert len(travel.flights.flights) == 1


def test_add_flight_same_flight():
    new_flight = Flight('00', '', 0)
    flights = Flights([Flight('00', '', 0)])
    travel = Travel(flights)
    old_len = len(travel.flights.flights)
    travel.add_flight(new_flight)
    assert old_len != 0
    assert len(travel.flights.flights) == old_len


def test_add_flight_new_flight():
    new_flight = Flight('01', '', 0)
    flights = Flights([Flight('00', '', 0)])
    travel = Travel(flights)
    old_len = len(travel.flights.flights)
    travel.add_flight(new_flight)
    assert old_len != 0
    assert len(travel.flights.flights) != old_len
    assert len(travel.flights.flights) == old_len + 1


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


def test_travel_get_num_clients_add_flight():
    flights = Flights([
        Flight('00', '', 4),
        Flight('01', '', 4)
    ])
    travel = Travel(flights)
    travel.add_flight(Flight('02', '', 4))
    assert travel.get_num_clients() == 12


def test_travel_delete_flight_existing_flight():
    flights = Flights([
        Flight('00', '', 4),
        Flight('01', '', 4)
    ])
    travel = Travel(flights)
    travel.delete_flight('00')
    assert len(travel.flights.flights) != 2
    assert len(travel.flights.flights) == 1


def test_travel_delete_flight_non_existing_flight():
    flights = Flights([
        Flight('00', '', 4),
        Flight('01', '', 4)
    ])
    travel = Travel(flights)
    travel.delete_flight('03')
    assert len(travel.flights.flights) == 2
    assert len(travel.flights.flights) != 1


def test_travel_initialization_non_existing_flights():
    travel = Travel(Flights(list()))
    assert isinstance(travel.flights, Flights)
    assert travel.flights.flights == dict()

from src.Reservation import Reservation
from src.Travel import Travel
from src.User import User
from src.Flights import Flights
from src.Flight import Flight
from src.PaymentData import PaymentData


def test_reservation_ctor():
    """ Unit test for Reservation.__init__(**)

    :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'test', 0)
    ]))
    reservation = Reservation(travel, usr)
    assert isinstance(reservation, Reservation)

    travel.flights.modify_flight('00', new_destination='Berlin')
    assert reservation.travel.flights.flights['00'] != travel.flights.flights['00']


def test_reservation_calculate_flights_price_no_flights():
    """ Unit test for Reservation.calculate_flights_price(**)

        Calculated price should be zero when there are no destinations
        :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([]))
    reservation = Reservation(travel, usr)
    assert reservation.calculate_flights_price(5) == 0


def test_reservation_calculate_flights_price_no_clients():
    """ Unit test for Reservation.calculate_flights_price(**)

        Calculated price should be zero when there are no destinations
        :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([Flight('00', 'Berlin', 0)]))
    reservation = Reservation(travel, usr)
    assert reservation.calculate_flights_price(5) == 0

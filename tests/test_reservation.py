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
    payment = PaymentData('Test', '000000', '000', 5)
    reservation = Reservation(travel, usr, payment)
    assert isinstance(reservation, Reservation)

    travel.flights.modify_flight('00', new_destination='Berlin')
    assert reservation.travel.flights.flights['00'] != travel.flights.flights['00']

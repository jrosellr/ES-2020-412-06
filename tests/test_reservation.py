from src.Reservation import Reservation
from src.Travel import Travel
from src.User import User
from src.Flights import Flights
from src.Flight import Flight
from src.PaymentData import PaymentData
from .test_constants import *
import pytest

# TODO: add documentation about fixture usage


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

    travel._flights['00'].destination = 'Berlin'
    assert reservation._travel._flights['00'] != travel._flights['00']


def test_reservation_process_payment_data(mock_fetch_prices):
    """ Unit test for Reservation._process_payment_data()

        Amount in payment_data should be != 0 and == number of flights * flight price
        :return: None
    """

    num_travelers = 2
    num_flights = 2
    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'Berlin', num_travelers),
        Flight('01', 'Roma', num_travelers)
    ]))

    reservation = Reservation(travel, usr)

    # 2. Process the payment data:
    payment_data = reservation._process_payment_data('Test', '000000', '000', 'VISA')

    assert isinstance(payment_data, PaymentData)
    assert payment_data.amount != 0.0
    assert payment_data.amount == MOCKED_TICKET_PRICE * num_travelers * num_flights


def test_confirm_payment_error(mock_fetch_prices, mock_bank_error):
    """ Unit test for Reservation.confirm() when Bank.do_payment returns False

        reservation.confirm() should be False
        :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'Berlin', 2),
        Flight('01', 'Roma', 2)
    ]))
    reservation = Reservation(travel, usr)
    assert reservation.confirm('Test_card', '', '123', 'VISA') is not None
    assert reservation.confirm('Test_card', '', '123', 'VISA') is not True
    assert reservation.confirm('Test_card', '', '123', 'VISA') is False


def test_confirm_payment_done(mock_fetch_prices, mock_bank_success):
    """ Mock test for Reservation.confirm() when Bank.do_payment returns True

        reservation.confirm() should be True
        :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'Berlin', 2),
        Flight('01', 'Roma', 2)
    ]))
    reservation = Reservation(travel, usr)
    assert reservation.confirm('Test_card', '', '123', 'VISA') is not None
    assert reservation.confirm('Test_card', '', '123', 'VISA') is not False
    assert reservation.confirm('Test_card', '', '123', 'VISA') is True


def test_retries_confirm_flights(mock_confirm_reserve_return_retries, mock_fetch_prices, mock_skyscanner_error):
    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'Berlin', 2),
        Flight('01', 'Roma', 2)
    ]))
    reservation = Reservation(travel, usr)
    assert reservation._confirm_flights() == 3


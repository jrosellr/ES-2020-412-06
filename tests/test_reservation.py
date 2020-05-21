from src.Reservation import Reservation
from src.Travel import Travel
from src.User import User
from src.Flights import Flights
from src.Flight import Flight
from src.PaymentData import PaymentData
from .test_constants import *
import pytest

# TODO: add documentation about fixture usage


def test_reservation_ctor(default_user, default_travel):
    """ Unit test for Reservation.__init__(**)

    :return: None
    """

    reservation = Reservation(default_travel, default_user)

    assert isinstance(reservation, Reservation)


def test_reservation_process_payment_data(mock_fetch_prices, default_reservation):
    """ Unit test for Reservation._process_payment_data()

        Amount in payment_data should be != 0 and == number of flights * flight price
        :return: None
    """

    # 2. Process the payment data:
    default_payment_data = default_reservation._process_payment_data(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER, DEFAULT_CARD_CVV, DEFAULT_CARD_TYPE)

    assert isinstance(default_payment_data, PaymentData)
    assert default_payment_data.amount != 0.0
    assert default_payment_data.amount == MOCKED_TICKET_PRICE * DEFAULT_FLIGHT_PASSENGERS * DEFAULT_FLIGHTS_LEN


def test_confirm_payment_error(mock_fetch_prices, mock_bank_error, default_reservation):
    """ Unit test for Reservation.confirm() when Bank.do_payment returns False

        reservation.confirm() should be False
        :return: None
    """
    reservation_confirmed = default_reservation.confirm(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER, DEFAULT_CARD_CVV, DEFAULT_CARD_TYPE)

    assert reservation_confirmed is not None
    assert reservation_confirmed is not True
    assert reservation_confirmed is False


def test_confirm_payment_done(mock_fetch_prices, mock_bank_success, default_reservation):
    """ Mock test for Reservation.confirm() when Bank.do_payment returns True

        reservation.confirm() should be True
        :return: None
    """

    reservation_confirmed = default_reservation.confirm(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER, DEFAULT_CARD_CVV,  DEFAULT_CARD_TYPE)

    assert reservation_confirmed is not None
    assert reservation_confirmed is not False
    assert reservation_confirmed is True


def test_retries_confirm_flights(mock_confirm_reserve_return_retries, mock_fetch_prices, mock_skyscanner_error, default_reservation):

    assert default_reservation._confirm_flights() == 3

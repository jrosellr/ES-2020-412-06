from src.Reservation import Reservation
from src.PaymentData import PaymentData
from .test_constants import *
from src.Response import Response

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
    assert default_payment_data.amount == MOCKED_TICKET_PRICE * DEFAULT_NUM_TRAVELERS * DEFAULT_FLIGHTS_LEN


def test_retries_confirm_flights(mock_confirm_reserve_return_retries, mock_fetch_prices, mock_skyscanner_error, default_reservation):

    assert default_reservation._confirm_flights() == 3


def test_retries_confirm_hotels(mock_booking_retries, mock_fetch_prices, mock_booking_error, default_reservation):

    assert default_reservation._confirm_hotels() == 3


def test_retries_confirm_cars(mock_rentalcars_retries, mock_fetch_prices, mock_rentalcars_error, default_reservation):

    assert default_reservation._confirm_cars() == 3


def test_confirm_payment_error(mock_fetch_prices, mock_bank_error, default_reservation):
    """ Unit test for Reservation.confirm() when Bank.do_payment returns False

        reservation.confirm() should be False
        :return: None
    """
    reservation_response = default_reservation.confirm(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER, DEFAULT_CARD_CVV, DEFAULT_CARD_TYPE)

    assert reservation_response is not ''
    assert reservation_response is Response.BANK_ERROR

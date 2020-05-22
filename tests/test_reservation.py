from src.Reservation import Reservation
from src.PaymentData import PaymentData
from src.Booking import Booking
from .test_constants import *
from src.Response import Response


# TODO: add documentation about fixture usage


def test_reservation_ctor(default_user, default_travel):
    """ Unit test for Reservation.__init__(**)

    :return: None
    """

    reservation = Reservation(default_travel, default_user)

    assert isinstance(reservation, Reservation)


def test_reservation_process_payment_data(default_reservation):
    """ Unit test for Reservation._process_payment_data()

        Amount in payment_data should be != 0 and == number of flights * flight price
        :return: None
    """

    # 2. Process the payment data:
    default_payment_data = default_reservation._process_payment_data(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER,
                                                                     DEFAULT_CARD_CVV, DEFAULT_CARD_TYPE)

    assert isinstance(default_payment_data, PaymentData)
    assert default_payment_data.amount != 0.0
    assert default_payment_data.amount == MOCKED_TICKET_PRICE * DEFAULT_NUM_TRAVELERS * DEFAULT_FLIGHTS_LEN


def test_retries_confirm_flights_error(mock_confirm_reserve_return_retries, default_reservation):
    assert default_reservation._confirm_flights() == 3


def test_confirm_flights(default_reservation):
    assert default_reservation._confirm_flights() is True


def test_retries_confirm_hotels(mock_booking_retries, default_reservation):
    assert default_reservation._confirm_hotels() == 3


def test_confirm_hotels(default_reservation, default_hotels):
    default_reservation._travel._hotels = default_hotels

    assert default_reservation._travel.has_hotels is True
    assert default_reservation._confirm_hotels() is True


def test_confirm_hotels_no_hotels(default_reservation):
    assert default_reservation._travel.has_hotels is False
    assert default_reservation._confirm_hotels() is True


def test_retries_confirm_cars(mock_rentalcars_retries, default_reservation):
    assert default_reservation._confirm_cars() == 3


def test_confirm_cars(default_reservation, default_cars):
    default_reservation._travel._cars = default_cars

    assert default_reservation._travel.has_cars is True
    assert default_reservation._confirm_cars() is True


def test_confirm_cars_no_cars(default_reservation):
    assert default_reservation._travel.has_cars is False
    assert default_reservation._confirm_cars() is True


def test_confirm_payment_error(mock_bank_error, default_reservation):
    """ Unit test for Reservation.confirm() when Bank.do_payment returns False

        reservation.confirm() should be False
        :return: None
    """
    reservation_response = default_reservation.confirm(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER, DEFAULT_CARD_CVV,
                                                       DEFAULT_CARD_TYPE)

    assert reservation_response is not ''
    assert reservation_response is Response.BANK_ERROR


def test_confirm_skyscanner_error(default_reservation, mock_skyscanner_error):
    """ Unit test for Reservation.confirm() when Bank.do_payment returns False

        reservation.confirm() should be False
        :return: None
    """
    reservation_response = default_reservation.confirm(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER, DEFAULT_CARD_CVV,
                                                       DEFAULT_CARD_TYPE)

    assert reservation_response is not ''
    assert reservation_response is Response.SKYSCANNER_ERROR


def test_confirm_booking_error(mock_booking_error, default_reservation, default_hotels):
    default_reservation._travel._hotels = default_hotels

    reservation_response = default_reservation.confirm(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER, DEFAULT_CARD_CVV,
                                                       DEFAULT_CARD_TYPE)

    assert reservation_response is not ''
    assert reservation_response is Response.BOOKING_ERROR


def test_confirm_rentalcars_error(mock_rentalcars_error, default_reservation, default_cars):
    default_reservation._travel._cars = default_cars

    reservation_response = default_reservation.confirm(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER, DEFAULT_CARD_CVV,
                                                       DEFAULT_CARD_TYPE)

    assert reservation_response is not ''
    assert reservation_response is Response.RENTALCARS_ERROR


def test_full_confirm_booking_error(full_reservation, mock_booking_error):
    reservation_response = full_reservation.confirm(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER, DEFAULT_CARD_CVV,
                                                    DEFAULT_CARD_TYPE)

    assert reservation_response is not ''
    assert reservation_response is Response.BOOKING_ERROR


def test_full_confirm_rentalcars_error(full_reservation, mock_rentalcars_error):
    reservation_response = full_reservation.confirm(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER, DEFAULT_CARD_CVV,
                                                    DEFAULT_CARD_TYPE)

    assert reservation_response is not ''
    assert reservation_response is Response.RENTALCARS_ERROR


def test_configure_travel(full_reservation):
    full_reservation._configure_travel()

    assert full_reservation._travel.ticket_price == MOCKED_TICKET_PRICE
    assert full_reservation._travel.hotel_price == MOCKED_HOTEL_PRICE
    assert full_reservation._travel.car_price == MOCKED_CAR_PRICE


def test_full_process_payment_data(full_reservation):
    """ Unit test for Reservation._process_payment_data()

        Amount in payment_data should be != 0 and == number of flights * flight price
        :return: None
    """
    default_payment_data = full_reservation._process_payment_data(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER,
                                                                  DEFAULT_CARD_CVV, DEFAULT_CARD_TYPE)

    assert isinstance(default_payment_data, PaymentData)
    assert default_payment_data.amount != 0.0
    assert full_reservation._travel.cost == DEFAULT_FLIGHT_TOTAL_COST + DEFAULT_HOTEL_TOTAL_COST + DEFAULT_CAR_TOTAL_COST

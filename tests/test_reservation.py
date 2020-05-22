from src.Reservation import Reservation
from src.PaymentData import PaymentData
from src.Booking import Booking
from .test_constants import *
from src.Response import Response


# TODO: add documentation about fixture usage


def test_reservation_ctor(default_travel):
    """ Unit test for Reservation.__init__(**)

    :return: None
    """

    reservation = Reservation(default_travel)

    assert isinstance(reservation, Reservation)
    assert reservation._user is None
    assert reservation._payment_method is None
    assert reservation._payment_data is None


def test_save_billing_data(default_travel):
    reservation = Reservation(default_travel)
    assert reservation.save_billing_data(DEFAULT_USER_NAME,
                                         DEFAULT_DNI,
                                         DEFAULT_ADDRESS,
                                         DEFAULT_MOBILE_NUMBER, DEFAULT_USER_EMAIL) == Response.RESERVATION_DATA_UPDATED


def test_invalid_billing_data(default_travel):
    reservation = Reservation(default_travel)
    assert reservation.save_billing_data(DEFAULT_USER_NAME,
                                         '0009CA',
                                         DEFAULT_ADDRESS,
                                         DEFAULT_MOBILE_NUMBER, DEFAULT_USER_EMAIL) is Response.INVALID_BILLING_DATA


def test_save_payment_method(default_travel):
    reservation = Reservation(default_travel)
    assert reservation.save_payment_method(DEFAULT_CARD_TYPE) is Response.RESERVATION_DATA_UPDATED


def test_invalid_payment_method(default_travel):
    reservation = Reservation(default_travel)
    assert reservation.save_payment_method('EXPRESS') is Response.INVALID_PAYMENT_METHOD


def test_save_payment_data(default_travel, mock_fetch_prices):
    reservation = Reservation(default_travel)
    assert reservation.save_payment_data(DEFAULT_CARD_HOLDER_NAME,
                                         DEFAULT_CARD_NUMBER, DEFAULT_CARD_CVV) is Response.RESERVATION_DATA_UPDATED


def test_invalid_payment_data(default_reservation):
    assert default_reservation.save_payment_data(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER,
                                       '1234') is Response.INVALID_PAYMENT_DATA


def test_retries_confirm_flights_error(mock_confirm_reserve_return_retries, default_reservation):
    assert default_reservation._confirm_flights() == DEFAULT_MAX_RETRIES


def test_confirm_flights(default_reservation):
    assert default_reservation._confirm_flights() is True


def test_retries_confirm_hotels(mock_booking_retries, default_reservation):
    assert default_reservation._confirm_hotels() == DEFAULT_MAX_RETRIES


def test_confirm_hotels(default_reservation, default_hotels):
    default_reservation._travel._hotels = default_hotels

    assert default_reservation._travel.has_hotels is True
    assert default_reservation._confirm_hotels() is True


def test_confirm_hotels_no_hotels(default_reservation):
    assert default_reservation._travel.has_hotels is False
    assert default_reservation._confirm_hotels() is True


def test_retries_confirm_cars(mock_rentalcars_retries, default_reservation):
    assert default_reservation._confirm_cars() == DEFAULT_MAX_RETRIES


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
    reservation_response = default_reservation.confirm()

    assert reservation_response is not ''
    assert reservation_response is Response.BANK_ERROR


def test_confirm_skyscanner_error(default_reservation, mock_skyscanner_error):
    """ Unit test for Reservation.confirm() when Bank.do_payment returns False

        reservation.confirm() should be False
        :return: None
    """
    reservation_response = default_reservation.confirm()

    assert reservation_response is not ''
    assert reservation_response is Response.SKYSCANNER_ERROR


def test_confirm_booking_error(mock_booking_error, default_reservation, default_hotels):
    default_reservation._travel._hotels = default_hotels

    reservation_response = default_reservation.confirm()

    assert reservation_response is not ''
    assert reservation_response is Response.BOOKING_ERROR


def test_confirm_rentalcars_error(mock_rentalcars_error, default_reservation, default_cars):
    default_reservation._travel._cars = default_cars

    reservation_response = default_reservation.confirm()

    assert reservation_response is not ''
    assert reservation_response is Response.RENTALCARS_ERROR


def test_full_confirm_booking_error(full_reservation, mock_booking_error):
    reservation_response = full_reservation.confirm()

    assert reservation_response is not ''
    assert reservation_response is Response.BOOKING_ERROR


def test_full_confirm_rentalcars_error(full_reservation, mock_rentalcars_error):
    reservation_response = full_reservation.confirm()

    assert reservation_response is not ''
    assert reservation_response is Response.RENTALCARS_ERROR


def test_configure_travel(full_reservation):
    full_reservation._configure_travel()

    assert full_reservation._travel.ticket_price == MOCKED_TICKET_PRICE
    assert full_reservation._travel.hotel_price == MOCKED_HOTEL_PRICE
    assert full_reservation._travel.car_price == MOCKED_CAR_PRICE

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
    assert default_payment_data.amount == DEFAULT_FLIGHT_TOTAL_COST


def test_reservation_process_payment_data_hotels(default_reservation, default_hotels):
    """ Unit test for Reservation._process_payment_data()

        Amount in payment_data should be != 0 and == number of flights * flight price
        :return: None
    """

    # 2. Process the payment data:
    default_reservation._travel._hotels = default_hotels
    default_payment_data = default_reservation._process_payment_data(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER,
                                                                     DEFAULT_CARD_CVV, DEFAULT_CARD_TYPE)

    assert isinstance(default_payment_data, PaymentData)
    assert default_payment_data.amount != 0.0
    assert default_payment_data.amount == DEFAULT_FLIGHT_TOTAL_COST + DEFAULT_HOTEL_TOTAL_COST


def test_reservation_process_payment_data_cars(default_reservation, default_cars):
    """ Unit test for Reservation._process_payment_data()

        Amount in payment_data should be != 0 and == number of flights * flight price
        :return: None
    """

    # 2. Process the payment data:
    default_reservation._travel._cars = default_cars
    default_payment_data = default_reservation._process_payment_data(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER,
                                                                     DEFAULT_CARD_CVV, DEFAULT_CARD_TYPE)

    assert isinstance(default_payment_data, PaymentData)
    assert default_payment_data.amount != 0.0
    assert default_payment_data.amount == DEFAULT_FLIGHT_TOTAL_COST + DEFAULT_CAR_TOTAL_COST


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


def test_payment_retries(mock_bank_retries, default_reservation: Reservation, default_payment_data):
    assert default_reservation._confirm_payment(default_payment_data) == DEFAULT_MAX_RETRIES

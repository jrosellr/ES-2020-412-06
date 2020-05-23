from src.Reservation import Reservation
from src.PaymentData import PaymentData
from src.Travel import Travel
from .test_constants import *
from src.Response import Response


def test_reservation_ctor(default_travel):
    """ Test case for Reservation.__init__(**) method

    RESTRICTION:
        The Reservation object should be initialized with its default values and the travel object used as parameter

    TEST CASE:
        Check that all the instance attributes are None except for _travel

    EXPECTED BEHAVIOUR:
        _travel is initialized and all the other instance attributes are None
    """

    reservation = Reservation(default_travel)

    assert isinstance(reservation, Reservation)
    assert reservation._travel is not None
    assert isinstance(reservation._travel, Travel)
    assert reservation._user is None
    assert reservation._payment_method is None
    assert reservation._payment_data is None


def test_save_billing_data(default_travel):
    """ Test case for Reservation.save_billing_data(**) method

    RESTRICTION:
        The call should return Response.RESERVATION_DATA_UPDATED if the data is valid
        and Response.INVALID_BILLING_DATA if it isn't

    TEST CASE:
        The given data is all valid

    EXPECTED BEHAVIOUR:
        The call returns Response.RESERVATION_DATA_UPDATED and the _user instance attribute is not None
    """

    reservation = Reservation(default_travel)
    assert reservation.save_billing_data(DEFAULT_USER_NAME,
                                         DEFAULT_DNI,
                                         DEFAULT_ADDRESS,
                                         DEFAULT_MOBILE_NUMBER, DEFAULT_USER_EMAIL) == Response.RESERVATION_DATA_UPDATED

    assert reservation._user is not None


def test_invalid_billing_data(default_travel):
    """ Test case for Reservation.save_billing_data(**) method

    RESTRICTION:
        The call should return Response.RESERVATION_DATA_UPDATED if the data is valid
        and Response.INVALID_BILLING_DATA if it isn't

    TEST CASE:
        The given data is not valid

    EXPECTED BEHAVIOUR:
        The call returns Response.INVALID_BILLING_DATA and the _user instance attribute is None
    """

    reservation = Reservation(default_travel)
    assert reservation.save_billing_data(DEFAULT_USER_NAME,
                                         '0009CA',
                                         DEFAULT_ADDRESS,
                                         DEFAULT_MOBILE_NUMBER, DEFAULT_USER_EMAIL) is Response.INVALID_BILLING_DATA

    assert reservation._user is None


def test_save_payment_method(default_travel):
    """ Test case for Reservation.save_payment_method(**) method

    RESTRICTION:
        The call should return Response.RESERVATION_DATA_UPDATED if the data is valid
        and Response.INVALID_PAYMENT_METHOD if it isn't

    TEST CASE:
        The given data is valid

    EXPECTED BEHAVIOUR:
        The call returns Response.RESERVATION_DATA_UPDATED and _payment_method instance attribute is not None
    """

    reservation = Reservation(default_travel)
    assert reservation.save_payment_method(DEFAULT_CARD_TYPE) is Response.RESERVATION_DATA_UPDATED
    assert reservation._payment_method is not None


def test_invalid_payment_method(default_travel):
    """ Test case for Reservation.save_payment_method(**) method

    RESTRICTION:
        The call should return Response.RESERVATION_DATA_UPDATED if the data is valid
        and Response.INVALID_PAYMENT_METHOD if it isn't

    TEST CASE:
        The given data is not valid

    EXPECTED BEHAVIOUR:
        The call returns Response.INVALID_PAYMENT_METHOD  and _payment_method instance attribute is None
    """

    reservation = Reservation(default_travel)
    assert reservation.save_payment_method('EXPRESS') is Response.INVALID_PAYMENT_METHOD
    assert reservation._payment_method is None


def test_save_payment_data(default_travel, mock_fetch_prices):
    """ Test case for Reservation.save_payment_data(**) method

    RESTRICTION:
        The call should return Response.RESERVATION_DATA_UPDATED if the data is valid
        and Response.INVALID_PAYMENT_DATA if it isn't

    TEST CASE:
        The given data is valid

    EXPECTED BEHAVIOUR:
        The call returns Response.RESERVATION_DATA_UPDATED and the _payment_data instance attribute is not None
    """

    reservation = Reservation(default_travel)
    assert reservation.save_payment_data(DEFAULT_CARD_HOLDER_NAME,
                                         DEFAULT_CARD_NUMBER, DEFAULT_CARD_CVV) is Response.RESERVATION_DATA_UPDATED

    assert reservation._payment_data is not None


def test_invalid_payment_data(default_travel):
    """ Test case for Reservation.save_payment_data(**) method

    RESTRICTION:
        The call should return Response.RESERVATION_DATA_UPDATED if the data is valid
        and Response.INVALID_PAYMENT_DATA if it isn't

    TEST CASE:
        The given data is not valid

    EXPECTED BEHAVIOUR:
        The call returns Response.RESERVATION_DATA_UPDATED and the _payment_data instance attribute is None
    """

    reservation = Reservation(default_travel)
    assert reservation.save_payment_data(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER,
                                       '1234') is Response.INVALID_PAYMENT_DATA
    assert reservation._payment_method is None


def test_max_retries_confirm_payment(mock_max_bank_retries, default_reservation: Reservation, default_payment_data):
    """ Test case for Reservation._confirm_payment(**) method

    RESTRICTION:
        The connection to the Bank API should be attempted
        a total of 4 times, 1 first connection and 3 retries

    TEST CASE:
        The connection fails every time, exhausting the retry limit

    EXPECTED BEHAVIOUR:
        The connection fails and raises a ConnectionRefusedError, however we patch out
        that functionality, returning the number of retries, which should be equal to DEFAULT_MAX_RETRIES
    """

    assert default_reservation._confirm_payment(default_payment_data) == DEFAULT_MAX_RETRIES


def test_retries_confirm_payment(mock_bank_retries, default_reservation):
    """ Test case for Reservation._confirm_payment(**) method

    RESTRICTION:
        The connection to the Bank API should be attempted
        a total of 4 times, 1 first connection and 3 retries

    TEST CASE:
        The connection fails DEFAULT_RETRIES times, works in the next attempt and performs the payment

    EXPECTED BEHAVIOUR:
        The connection fails DEFAULT_RETRIES times and returns the expected boolean value
    """

    retries, bank_response = default_reservation._confirm_payment()

    assert retries == DEFAULT_RETRIES
    assert bank_response is True


def test_max_retries_confirm_flights(mock_max_skyscanner_retries, default_reservation):
    """ Test case for Reservation._confirm_flights(**) method

    RESTRICTION:
        The connection to the Skyscanner API should be attempted
        a total of 4 times, 1 first connection and 3 retries

    TEST CASE:
        The connection fails every time, exhausting the retry limit

    EXPECTED BEHAVIOUR:
        The connection fails and raises a ConnectionRefusedError, however we patch out
        that functionality, returning the number of retries, which should be equal to DEFAULT_MAX_RETRIES
    """

    assert default_reservation._confirm_flights() == DEFAULT_MAX_RETRIES


def test_retries_confirm_flights(mock_skyscanner_retries, default_reservation):
    """ Test case for Reservation._confirm_flights(**) method

    RESTRICTION:
        The connection to the Skyscanner API should be attempted
        a total of 4 times, 1 first connection and 3 retries

    TEST CASE:
        The connection fails DEFAULT_RETRIES times, works in the next attempt and performs the payment

    EXPECTED BEHAVIOUR:
        The connection fails DEFAULT_RETRIES times and returns the expected boolean value
    """

    retries, skyscanner_response = default_reservation._confirm_flights()

    assert retries == DEFAULT_RETRIES
    assert skyscanner_response is True


def test_confirm_flights(default_reservation):
    """ Test case for Reservation._confirm_flights(**) method

    RESTRICTION:
        The connection to the Skyscanner API should be attempted
        a total of 4 times, 1 first connection and 3 retries

    TEST CASE:
        The connection works the first time

    EXPECTED BEHAVIOUR:
        The connection works and returns the expected boolean value
    """

    assert default_reservation._confirm_flights() is True


def test_max_retries_confirm_hotels(mock_max_booking_retries, default_reservation):
    """ Test case for Reservation._confirm_hotels(**) method

    RESTRICTION:
        The connection to the Booking API should be attempted
        a total of 4 times, 1 first connection and 3 retries

    TEST CASE:
        The connection fails every time, exhausting the retry limit

    EXPECTED BEHAVIOUR:
        The connection fails and raises a ConnectionRefusedError, however we patch out
        that functionality, returning the number of retries, which should be equal to DEFAULT_MAX_RETRIES
    """

    assert default_reservation._confirm_hotels() == DEFAULT_MAX_RETRIES


def test_retries_confirm_hotels(mock_booking_retries, default_reservation):
    """ Test case for Reservation._confirm_hotels(**) method

    RESTRICTION:
        The connection to the Booking API should be attempted
        a total of 4 times, 1 first connection and 3 retries

    TEST CASE:
        The connection fails DEFAULT_RETRIES times, works in the next attempt and performs the payment

    EXPECTED BEHAVIOUR:
        The connection fails DEFAULT_RETRIES times and returns the expected boolean value
    """

    retries, hotels_ret = default_reservation._confirm_hotels()

    assert retries == DEFAULT_RETRIES
    assert hotels_ret is True


def test_confirm_hotels(default_reservation, default_hotels):
    """ Test case for Reservation._confirm_hotels(**) method

    RESTRICTION:
        _confirm_hotels should return the expected boolean value when there are Hotels in the Travel
        and return always True when there are no Hotels.

    TEST CASE:
        There are Hotels in the Travel object

    EXPECTED BEHAVIOUR:
        The returned value should be the same as the one returned by the API
    """

    default_reservation._travel._hotels = default_hotels

    assert default_reservation._travel.has_hotels is True
    assert default_reservation._confirm_hotels() is True


def test_confirm_hotels_no_hotels(default_reservation):
    """ Test case for Reservation._confirm_hotels(**) method

    RESTRICTION:
        _confirm_hotels should return the expected boolean value when there are Hotels in the Travel
        and return always True when there are no Hotels.

    TEST CASE:
        There are no Hotels in the Travel object

    EXPECTED BEHAVIOUR:
        The returned value should always be True
    """

    assert default_reservation._travel.has_hotels is False
    assert default_reservation._confirm_hotels() is True


def test_max_retries_confirm_cars(mock_max_rentalcars_retries, default_reservation):
    """ Test case for Reservation._confirm_cars(**) method

    RESTRICTION:
        The connection to the Rentalcars API should be attempted
        a total of 4 times, 1 first connection and 3 retries

    TEST CASE:
        The connection fails every time, exhausting the retry limit

    EXPECTED BEHAVIOUR:
        The connection fails and raises a ConnectionRefusedError, however we patch out
        that functionality, returning the number of retries, which should be equal to DEFAULT_MAX_RETRIES
    """

    assert default_reservation._confirm_cars() == DEFAULT_MAX_RETRIES


def test_retries_confirm_cars(mock_rentalcars_retries, default_reservation):
    """ Test case for Reservation._confirm_cars(**) method

    RESTRICTION:
        The connection to the Rentalcars API should be attempted
        a total of 4 times, 1 first connection and 3 retries

    TEST CASE:
        The connection fails DEFAULT_RETRIES times, works in the next attempt and performs the payment

    EXPECTED BEHAVIOUR:
        The connection fails DEFAULT_RETRIES times and returns the expected boolean value
    """
    retries, cars_ret = default_reservation._confirm_cars()

    assert retries == DEFAULT_RETRIES
    assert cars_ret is True


def test_confirm_cars(default_reservation, default_cars):
    """ Test case for Reservation._confirm_cars(**) method

    RESTRICTION:
        _confirm_cars should return the expected boolean value when there are Cars in the Travel
        and return always True when there are no Cars.

    TEST CASE:
        There are Cars in the Travel object

    EXPECTED BEHAVIOUR:
        The returned value should be the same as the one returned by the API
    """

    default_reservation._travel._cars = default_cars

    assert default_reservation._travel.has_cars is True
    assert default_reservation._confirm_cars() is True


def test_confirm_cars_no_cars(default_reservation):
    """ Test case for Reservation._confirm_cars(**) method

    RESTRICTION:
        _confirm_hotels should return the expected boolean value when there are Cars in the Travel
        and return always True when there are no Cars.

    TEST CASE:
        There are no Cars in the Travel object

    EXPECTED BEHAVIOUR:
        The returned value should always be True
    """

    assert default_reservation._travel.has_cars is False
    assert default_reservation._confirm_cars() is True


def test_confirm_payment_error(mock_bank_error, default_reservation):
    """ Test case for Reservation.confirm()

    RESTRICTION:
        This method should return the correct Response code depending on
        the outcome of the different transactions that it performs

    TEST CASE:
        The Bank API call fails and aborts the confirmation process

    EXPECTED BEHAVIOUR:
        The method returns Response.BANK_ERROR
    """

    reservation_response = default_reservation.confirm()

    assert reservation_response is not ''
    assert reservation_response is Response.BANK_ERROR


def test_confirm_skyscanner_error(default_reservation, mock_skyscanner_error):
    """ Test case for Reservation.confirm()

    RESTRICTION:
        This method should return the correct Response code depending on
        the outcome of the different transactions that it performs

    TEST CASE:
        The Skyscanner API call fails and aborts the confirmation process

    EXPECTED BEHAVIOUR:
        The method returns Response.SKYSCANNER_ERROR
    """

    reservation_response = default_reservation.confirm()

    assert reservation_response is not ''
    assert reservation_response is Response.SKYSCANNER_ERROR


def test_confirm_booking_error(mock_booking_error, default_reservation, default_hotels):
    """ Test case for Reservation.confirm()

    RESTRICTION:
        This method should return the correct Response code depending on
        the outcome of the different transactions that it performs

    TEST CASE:
        The Booking API call fails and aborts the confirmation process

    EXPECTED BEHAVIOUR:
        The method returns Response.BOOKING_ERROR
    """

    default_reservation._travel._hotels = default_hotels

    reservation_response = default_reservation.confirm()

    assert reservation_response is not ''
    assert reservation_response is Response.BOOKING_ERROR


def test_confirm_rentalcars_error(mock_rentalcars_error, default_reservation, default_cars):
    """ Test case for Reservation.confirm()

    RESTRICTION:
        This method should return the correct Response code depending on
        the outcome of the different transactions that it performs

    TEST CASE:
        The Rentalcars API call fails and aborts the confirmation process

    EXPECTED BEHAVIOUR:
        The method returns Response.RENTALCARS_ERROR
    """

    default_reservation._travel._cars = default_cars

    reservation_response = default_reservation.confirm()

    assert reservation_response is not ''
    assert reservation_response is Response.RENTALCARS_ERROR


def test_full_confirm_booking_error(full_reservation, mock_booking_error):
    """ Test case for Reservation.confirm()

    RESTRICTION:
        This method should return the correct Response code depending on
        the outcome of the different transactions that it performs

    TEST CASE:
        The Booking API call fails and aborts the confirmation process
        when the Reservation's Travel has all it's options initialized

    EXPECTED BEHAVIOUR:
        The method returns Response.BOOKING_ERROR
    """

    reservation_response = full_reservation.confirm()

    assert reservation_response is not ''
    assert reservation_response is Response.BOOKING_ERROR


def test_full_confirm_rentalcars_error(full_reservation, mock_rentalcars_error):
    """ Test case for Reservation.confirm()

    RESTRICTION:
        This method should return the correct Response code depending on
        the outcome of the different transactions that it performs

    TEST CASE:
        The Rentalcars API call fails and aborts the confirmation process
        when the Reservation's Travel has all it's options initialized

    EXPECTED BEHAVIOUR:
        The method returns Response.RENTALCARS_ERROR
    """

    reservation_response = full_reservation.confirm()

    assert reservation_response is not ''
    assert reservation_response is Response.RENTALCARS_ERROR


def test_configure_travel(full_reservation):
    """ Test for Reservation._configure_travel(**)

    RESTRICTION:
        The prices of each Travel product should be initialized with the prices retrieved from the different APIs

    TEST CASE:
        All Travel prices are initialized

    EXPECTED BEHAVIOUR:
        The Travel prices should be the same as the mocked prices
    """

    full_reservation._configure_travel()

    assert full_reservation._travel.ticket_price == MOCKED_TICKET_PRICE
    assert full_reservation._travel.hotel_price == MOCKED_HOTEL_PRICE
    assert full_reservation._travel.car_price == MOCKED_CAR_PRICE


def test_reservation_process_payment_data(default_reservation):
    """ Test for Reservation._process_payment_data(**)

    RESTRICTION:
        The PaymentData object created by this method should be initialized with the specified
        parameters and the amount should be equal to the cost of the current Travel stored in Reservation

    TEST CASE:
        Reservation's Travel has only flights

    EXPECTED BEHAVIOUR:
        The PaymentData's amount should be the same as the Travel's cost:
        (DEFAULT_FLIGHT_TOTAL_COST)
    """

    default_payment_data = default_reservation._process_payment_data(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER,
                                                                     DEFAULT_CARD_CVV, DEFAULT_CARD_TYPE)

    assert isinstance(default_payment_data, PaymentData)
    assert default_payment_data.amount != 0.0
    assert default_payment_data.amount == DEFAULT_FLIGHT_TOTAL_COST


def test_reservation_process_payment_data_hotels(default_reservation, default_hotels):
    """ Test for Reservation._process_payment_data(**)

    RESTRICTION:
        The PaymentData object created by this method should be initialized with the specified
        parameters and the amount should be equal to the cost of the current Travel stored in Reservation

    TEST CASE:
        Reservation's Travel has flights and hotels

    EXPECTED BEHAVIOUR:
        The PaymentData's amount should be the same as the Travel's cost:
        (DEFAULT_FLIGHT_TOTAL_COST + DEFAULT_HOTEL_TOTAL_COST)
    """

    default_reservation._travel._hotels = default_hotels
    default_payment_data = default_reservation._process_payment_data(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER,
                                                                     DEFAULT_CARD_CVV, DEFAULT_CARD_TYPE)

    assert isinstance(default_payment_data, PaymentData)
    assert default_payment_data.amount != 0.0
    assert default_payment_data.amount == DEFAULT_FLIGHT_TOTAL_COST + DEFAULT_HOTEL_TOTAL_COST


def test_reservation_process_payment_data_cars(default_reservation, default_cars):
    """ Test for Reservation._process_payment_data(**)

    RESTRICTION:
        The PaymentData object created by this method should be initialized with the specified
        parameters and the amount should be equal to the cost of the current Travel stored in Reservation

    TEST CASE:
        Reservation's Travel has flights and cars

    EXPECTED BEHAVIOUR:
        The PaymentData's amount should be the same as the Travel's cost:
        (DEFAULT_FLIGHT_TOTAL_COST + DEFAULT_CAR_TOTAL_COST)
    """

    default_reservation._travel._cars = default_cars
    default_payment_data = default_reservation._process_payment_data(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER,
                                                                     DEFAULT_CARD_CVV, DEFAULT_CARD_TYPE)

    assert isinstance(default_payment_data, PaymentData)
    assert default_payment_data.amount != 0.0
    assert default_payment_data.amount == DEFAULT_FLIGHT_TOTAL_COST + DEFAULT_CAR_TOTAL_COST


def test_full_process_payment_data(full_reservation):
    """ Test for Reservation._process_payment_data(**)

    RESTRICTION:
        The PaymentData object created by this method should be initialized with the specified
        parameters and the amount should be equal to the cost of the current Travel stored in Reservation

    TEST CASE:
        Reservation's Travel has flights, hotels and cars

    EXPECTED BEHAVIOUR:
        The PaymentData's amount should be the same as the Travel's cost:
        (DEFAULT_FLIGHT_TOTAL_COST + DEFAULT_HOTEL_TOTAL_COST + DEFAULT_CAR_TOTAL_COST)
    """

    default_payment_data = full_reservation._process_payment_data(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER,
                                                                  DEFAULT_CARD_CVV, DEFAULT_CARD_TYPE)

    assert isinstance(default_payment_data, PaymentData)
    assert default_payment_data.amount != 0.0
    assert full_reservation._travel.cost == DEFAULT_FLIGHT_TOTAL_COST + DEFAULT_HOTEL_TOTAL_COST + DEFAULT_CAR_TOTAL_COST

""" pytest configuration file

    File used by pytest to set up the testing environment.
    In this file are declared multiple test fixtures to make them available to all unit tests.
"""

import pytest
from src.Skyscanner import Skyscanner
from src.Booking import Booking
from src.Rentalcars import Rentalcars
from src.Reservation import Reservation
from src.PaymentData import PaymentData
from src.Bank import Bank
from src.Travel import Travel
from src.Flight import Flight
from src.Flights import Flights
from src.Car import Car
from src.Cars import Cars
from src.User import User
from src.Response import Response
from src.Hotel import Hotel
from src.Hotels import Hotels

from .test_constants import *


@pytest.fixture
def mock_fetch_prices(monkeypatch):
    """ Fixture to simulate the price returned by each API

    PATCHED FUNCTIONALITY:
        Replaces the fetch functions of each API by mocks and returns the default prices.
    """

    def mock_fetch_ticket_price(*args):
        return MOCKED_TICKET_PRICE

    def mock_fetch_hotel_price(*args):
        return MOCKED_HOTEL_PRICE

    def mock_fetch_car_price(*args):
        return MOCKED_CAR_PRICE

    monkeypatch.setattr(Skyscanner, "fetch_ticket_price", mock_fetch_ticket_price)
    monkeypatch.setattr(Booking, "fetch_hotel_price", mock_fetch_hotel_price)
    monkeypatch.setattr(Rentalcars, "fetch_car_price", mock_fetch_car_price)


@pytest.fixture
def mock_bank_error(monkeypatch):
    """ Fixture to simulate an error with the bank.

    PATCHED FUNCTIONALITY:
        Replaces the do_payment function in Bank by a mock that raises an error exception.
    """

    def mock_do_payment_error(*args):
        raise ConnectionRefusedError(Response.BANK_ERROR)

    monkeypatch.setattr(Bank, "do_payment", mock_do_payment_error)


@pytest.fixture
def mock_skyscanner_error(monkeypatch):
    """ Fixture to simulate an error with the Skyscanner API.

    PATCHED FUNCTIONALITY:
        Replaces the confirm_reserve function in Skyscanner by a mock that raises an error exception.
    """

    def mock_confirm_reserve_error(*args):
        raise ConnectionRefusedError(Response.SKYSCANNER_ERROR)

    monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_confirm_reserve_error)


@pytest.fixture
def mock_booking_error(monkeypatch):
    """ Fixture to simulate an error with the Booking API.

    PATCHED FUNCTIONALITY:
        Replaces the confirm_reserve function in Booking by a mock that raises an error exception.
    """

    def mock_confirm_booking_error(*args):
        raise ConnectionRefusedError(Response.BOOKING_ERROR)

    monkeypatch.setattr(Booking, "confirm_reserve", mock_confirm_booking_error)


@pytest.fixture
def mock_rentalcars_error(monkeypatch):
    """ Fixture to simulate an error with the Rentalcars API.

    PATCHED FUNCTIONALITY:
        Replaces the confirm_reserve method in Rentalcars
        by a mock that raises an error exception.
    """

    def mock_confirm_rentalcars_error(*args):
        raise ConnectionRefusedError(Response.RENTALCARS_ERROR)

    monkeypatch.setattr(Rentalcars, "confirm_reserve", mock_confirm_rentalcars_error)


@pytest.fixture
def mock_max_bank_retries(monkeypatch, mock_bank_error):
    """ Fixture to simulate the maximum number of retries for the Bank API.

    PATCHED FUNCTIONALITY:
        Replaces the _confirm_payment method in Reservation by a mock
        that returns the maximum number of retries.
    """

    def mock_confirm_payment(*args):
        retries = 0
        while retries < DEFAULT_MAX_RETRIES:
            try:
                return Bank.do_payment(*args)
            except ConnectionRefusedError:
                retries += 1
        return retries

    monkeypatch.setattr(Reservation, "_confirm_payment", mock_confirm_payment)


@pytest.fixture
def mock_bank_retries(monkeypatch, mock_bank_error):
    """ Fixture to simulate the maximum number of retries for the Bank API.

    PATCHED FUNCTIONALITY:
        Replaces the _confirm_payment method in Reservation by a mock
        that returns the attempted retries and the correct Bank response
    """

    def mock_bank_success(*args):
        return True

    def mock_confirm_payment(*args):
        retries = 0
        while retries < DEFAULT_MAX_RETRIES:
            try:
                return retries, Bank.do_payment(*args)
            except ConnectionRefusedError:
                retries += 1
                if retries == DEFAULT_RETRIES:
                    monkeypatch.setattr(Bank, "do_payment", mock_bank_success)

    monkeypatch.setattr(Reservation, "_confirm_payment", mock_confirm_payment)


@pytest.fixture
def mock_max_skyscanner_retries(monkeypatch, mock_skyscanner_error):
    """ Fixture to simulate the maximum number of retries for the Skyscanner API.

    PATCHED FUNCTIONALITY:
        Replaces the _confirm_flights method in Reservation by a mock
        that returns the attempted retries
    """

    def mock_confirm_flights(*args):
        retries = 0
        while retries < DEFAULT_MAX_RETRIES:
            try:
                if Skyscanner.confirm_reserve(*args):
                    pass
            except ConnectionRefusedError:
                retries += 1

        return retries

    monkeypatch.setattr(Reservation, "_confirm_flights", mock_confirm_flights)


@pytest.fixture
def mock_skyscanner_retries(monkeypatch, mock_skyscanner_error):
    """ Fixture to simulate the maximum number of retries for the Bank API.

    PATCHED FUNCTIONALITY:
        Replaces the _confirm_flights method in Reservation by a mock
        that returns the attempted retries and the correct Skyscanner response
    """

    def mock_skyscanner_success(*args):
        return True

    def mock_confirm_payment(*args):
        retries = 0
        while retries < DEFAULT_MAX_RETRIES:
            try:
                return retries, Skyscanner.confirm_reserve(*args)
            except ConnectionRefusedError:
                retries += 1
                if retries == DEFAULT_RETRIES:
                    monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_skyscanner_success)

    monkeypatch.setattr(Reservation, "_confirm_flights", mock_confirm_payment)


@pytest.fixture
def mock_max_booking_retries(monkeypatch, mock_booking_error):
    """ Fixture to simulate the maximum number of retries for the Booking API.

    PATCHED FUNCTIONALITY:
        Replaces the _confirm_hotels method in Reservation by a mock
        that returns the maximum number of retries.
    """

    def mock_confirm_hotels(*args):
        retries = 0
        while retries < DEFAULT_MAX_RETRIES:
            try:
                if Booking.confirm_reserve(*args):
                    pass
            except ConnectionRefusedError:
                retries += 1
        return retries

    monkeypatch.setattr(Reservation, "_confirm_hotels", mock_confirm_hotels)


@pytest.fixture
def mock_booking_retries(monkeypatch, mock_booking_error):
    """ Fixture to simulate the maximum number of retries for the Booking API.

    PATCHED FUNCTIONALITY:
        Replaces the _confirm_hotels method in Reservation by a mock
        that returns the attempted number of retries and the correct Booking response
    """

    def mock_booking_success(*args):
        return True

    def mock_confirm_hotels(*args):
        retries = 0
        while retries < DEFAULT_MAX_RETRIES:
            try:
                return retries, Booking.confirm_reserve(*args)
            except ConnectionRefusedError:
                retries += 1
                if retries == DEFAULT_RETRIES:
                    monkeypatch.setattr(Booking, "confirm_reserve", mock_booking_success)

    monkeypatch.setattr(Reservation, "_confirm_hotels", mock_confirm_hotels)


@pytest.fixture
def mock_max_rentalcars_retries(monkeypatch, mock_rentalcars_error):
    """ Fixture to simulate the maximum number of retries for the Rentalcars API.

    PATCHED FUNCTIONALITY:
        Replaces the _confirm_cars method in Reservation by a mock
        that returns the maximum number of retries.
    """

    def mock_confirm_cars(*args):
        retries = 0
        while retries < DEFAULT_MAX_RETRIES:
            try:
                if Rentalcars.confirm_reserve(*args):
                    pass
            except ConnectionRefusedError:
                retries += 1
        return retries

    monkeypatch.setattr(Reservation, "_confirm_cars", mock_confirm_cars)


@pytest.fixture
def mock_rentalcars_retries(monkeypatch, mock_rentalcars_error):
    """ Fixture to simulate the maximum number of retries for the Rentalcars API.

    PATCHED FUNCTIONALITY:
        Replaces the _confirm_cars method in Reservation by a mock
        that returns the attempted number of retries and the correct Rentalcars error.
    """

    def mock_rentalcars_success(*args):
        return True

    def mock_confirm_cars(*args):
        retries = 0
        while retries < DEFAULT_MAX_RETRIES:
            try:
                return retries, Rentalcars.confirm_reserve(*args)
            except ConnectionRefusedError:
                retries += 1
                if retries == DEFAULT_RETRIES:
                    monkeypatch.setattr(Rentalcars, "confirm_reserve", mock_rentalcars_success)

    monkeypatch.setattr(Reservation, "_confirm_cars", mock_confirm_cars)


@pytest.fixture
def default_flight_list():
    """ Fixture to create a list of Flight objects from default values.

    """

    f0 = Flight(DEFAULT_FLIGHT_CODE_0, DEFAULT_FLIGHT_DESTINATION, DEFAULT_NUM_TRAVELERS)
    f1 = Flight(DEFAULT_FLIGHT_CODE_1, DEFAULT_FLIGHT_DESTINATION, DEFAULT_NUM_TRAVELERS)
    f2 = Flight(DEFAULT_FLIGHT_CODE_2, DEFAULT_FLIGHT_DESTINATION, DEFAULT_NUM_TRAVELERS)
    return [f0, f1, f2]


@pytest.fixture
def default_flights(default_flight_list):
    """ Fixture to create a Flights object from a default flight list.

    """

    return Flights(default_flight_list)


@pytest.fixture
def default_new_flight():
    """ Fixture to create a Flight object from a default values.

    """

    return Flight(DEFAULT_NEW_FLIGHT_CODE, DEFAULT_FLIGHT_DESTINATION, DEFAULT_NUM_TRAVELERS)


@pytest.fixture
def default_hotel_list():
    """ Fixture to create a list of Hotel objects from default values.

    """

    h0 = Hotel(DEFAULT_HOTEL_CODE_0, DEFAULT_HOTEL_NAME_0, DEFAULT_HOTEL_DAYS_RESERVED)
    h1 = Hotel(DEFAULT_HOTEL_CODE_1, DEFAULT_HOTEL_NAME_1, DEFAULT_HOTEL_DAYS_RESERVED)
    h2 = Hotel(DEFAULT_HOTEL_CODE_2, DEFAULT_HOTEL_NAME_2, DEFAULT_HOTEL_DAYS_RESERVED)
    return [h0, h1, h2]

  
@pytest.fixture
def default_car_list():
    """ Fixture to create a list of Car objects from default values.

    """

    c0 = Car(DEFAULT_CAR_CODE_0, DEFAULT_CAR_BRAND, DEFAULT_CAR_PICK_UP_PLACE, DEFAULT_CAR_DAYS_RESERVED)
    c1 = Car(DEFAULT_CAR_CODE_1, DEFAULT_CAR_BRAND, DEFAULT_CAR_PICK_UP_PLACE, DEFAULT_CAR_DAYS_RESERVED)
    return [c0, c1]


@pytest.fixture
def default_payment_data():
    """ Fixture to create a PaymentData object from a default values.

    """

    return PaymentData(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER, DEFAULT_CARD_CVV, DEFAULT_PAYMENT_AMOUNT, DEFAULT_CARD_TYPE)


@pytest.fixture
def default_cars(default_car_list):
    """ Fixture to create a Cars object from a default car list.

    """

    return Cars(default_car_list)


@pytest.fixture
def default_hotels(default_hotel_list):
    """ Fixture to create a Hotels object from a default hotel list.

    """

    return Hotels(default_hotel_list)


@pytest.fixture
def default_new_car():
    """ Fixture to create a Car object from a default values.

    """

    return Car(DEFAULT_NEW_CAR_CODE, DEFAULT_CAR_BRAND, DEFAULT_CAR_PICK_UP_PLACE, DEFAULT_CAR_DAYS_RESERVED)


@pytest.fixture
def default_travel(default_flights):
    """ Fixture to create a Travel object from a default values and flights.

    """

    return Travel(DEFAULT_NUM_TRAVELERS, default_flights)


@pytest.fixture
def default_user():
    """ Fixture to create a User object from a default values.

    """

    return User(DEFAULT_USER_NAME, DEFAULT_DNI, DEFAULT_ADDRESS, DEFAULT_MOBILE_NUMBER, DEFAULT_USER_EMAIL)


@pytest.fixture
def default_reservation(default_travel, default_user, default_payment_data, mock_fetch_prices):
    """ Fixture to create a Reservation object from a default values of User and Travel with Fligths.

    """

    res = Reservation(default_travel)
    res._user = default_user
    res._payment_method = DEFAULT_CARD_TYPE
    res._payment_data = default_payment_data
    return res


@pytest.fixture
def full_reservation(default_flights, default_user, default_hotels, default_cars, mock_fetch_prices):
    """ Fixture to create a Reservation object from a default values of User, Travel with Flights, Cars and Hotels.

    """

    res = Reservation(Travel(DEFAULT_NUM_TRAVELERS, default_flights, default_hotels, default_cars))
    res._user = default_user
    res._payment_method = DEFAULT_CARD_TYPE
    res._payment_data = default_payment_data
    return res

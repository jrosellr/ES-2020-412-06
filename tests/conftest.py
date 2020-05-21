import pytest
from src.Skyscanner import Skyscanner
from src.Booking import Booking
from src.Rentalcars import Rentalcars
from src.Reservation import Reservation
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

# TODO: add documentation to fixtures


@pytest.fixture
def mock_fetch_prices(monkeypatch):
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
    def mock_do_payment_error(*args):
        raise ConnectionRefusedError(Response.BANK_ERROR)

    monkeypatch.setattr(Bank, "do_payment", mock_do_payment_error)


@pytest.fixture
def mock_bank_success(monkeypatch):
    def mock_do_payment_successful(*args):
        return MOCKED_BANK_SUCCESS_RET

    monkeypatch.setattr(Bank, "do_payment", mock_do_payment_successful)


@pytest.fixture
def mock_skyscanner_error(monkeypatch):
    def mock_confirm_reserve_error(*args):
        raise ConnectionRefusedError(Response.SKYSCANNER_ERROR)

    monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_confirm_reserve_error)


@pytest.fixture
def mock_confirm_reserve_return_retries(monkeypatch, mock_skyscanner_error):
    def mock_confirm_reserve(*args):
        retries = 0
        while retries < 3:
            try:
                return Skyscanner.confirm_reserve(*args)
            except ConnectionRefusedError:
                retries += 1
        return retries

    monkeypatch.setattr(Reservation, "_confirm_flights", mock_confirm_reserve)


@pytest.fixture
def mock_booking_retries(monkeypatch, mock_booking_error):
    def mock_confirm_reserve(*args):
        retries = 0
        while retries < 3:
            try:
                return Booking.confirm_reserve(*args)
            except ConnectionRefusedError:
                retries += 1
        return retries

    monkeypatch.setattr(Reservation, "_confirm_hotels", mock_confirm_reserve)


@pytest.fixture
def mock_rentalcars_retries(monkeypatch, mock_rentalcars_error):
    def mock_confirm_reserve(*args):
        retries = 0
        while retries < 3:
            try:
                return Rentalcars.confirm_reserve(*args)
            except ConnectionRefusedError:
                retries += 1
        return retries

    monkeypatch.setattr(Reservation, "_confirm_cars", mock_confirm_reserve)


@pytest.fixture
def mock_skyscanner_error(monkeypatch):
    def mock_confirm_reserve_error(*args):
        raise ConnectionRefusedError(Response.SKYSCANNER_ERROR)

    monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_confirm_reserve_error)


@pytest.fixture
def mock_booking_error(monkeypatch):
    def mock_confirm_reserve_error(*args):
        raise ConnectionRefusedError(Response.BOOKING_ERROR)

    monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_confirm_reserve_error)


@pytest.fixture
def mock_rentalcars_error(monkeypatch):
    def mock_confirm_reserve_error(*args):
        raise ConnectionRefusedError(Response.RENTALCARS_ERROR)

    monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_confirm_reserve_error)


@pytest.fixture
def default_flight_list():
    f0 = Flight(DEFAULT_FLIGHT_CODE_0, DEFAULT_FLIGHT_DESTINATION, DEFAULT_NUM_TRAVELERS)
    f1 = Flight(DEFAULT_FLIGHT_CODE_1, DEFAULT_FLIGHT_DESTINATION, DEFAULT_NUM_TRAVELERS)
    f2 = Flight(DEFAULT_FLIGHT_CODE_2, DEFAULT_FLIGHT_DESTINATION, DEFAULT_NUM_TRAVELERS)
    return [f0, f1, f2]


@pytest.fixture
def default_flights(default_flight_list):
    return Flights(default_flight_list)


@pytest.fixture
def default_new_flight():
    return Flight(DEFAULT_NEW_FLIGHT_CODE, DEFAULT_FLIGHT_DESTINATION, DEFAULT_NUM_TRAVELERS)


@pytest.fixture
def default_hotel_list():
    h0 = Hotel(DEFAULT_HOTEL_CODE_0, DEFAULT_HOTEL_NAME_0, DEFAULT_HOTEL_DAYS_RESERVED_0)
    h1 = Hotel(DEFAULT_HOTEL_CODE_1, DEFAULT_HOTEL_NAME_1, DEFAULT_HOTEL_DAYS_RESERVED_0)
    h2 = Hotel(DEFAULT_HOTEL_CODE_2, DEFAULT_HOTEL_NAME_2, DEFAULT_HOTEL_DAYS_RESERVED_0)
    return [h0, h1, h2]

  
@pytest.fixture
def default_car_list():
    c0 = Car(DEFAULT_CAR_CODE_0, DEFAULT_CAR_BRAND, DEFAULT_CAR_PICK_UP_PLACE, DEFAULT_CAR_DAYS_RESERVED)
    c1 = Car(DEFAULT_CAR_CODE_1, DEFAULT_CAR_BRAND, DEFAULT_CAR_PICK_UP_PLACE, DEFAULT_CAR_DAYS_RESERVED)
    return [c0, c1]
  

@pytest.fixture
def default_cars(default_car_list):
    return Cars(default_car_list)


@pytest.fixture
def default_new_car():
    return Car(DEFAULT_NEW_CAR_CODE, DEFAULT_CAR_BRAND, DEFAULT_CAR_PICK_UP_PLACE, DEFAULT_CAR_DAYS_RESERVED)
  

@pytest.fixture
def default_travel(default_flights):
    return Travel(DEFAULT_NUM_TRAVELERS, default_flights)


@pytest.fixture
def default_user():
    return User(DEFAULT_USER_NAME, DEFAULT_DNI, DEFAULT_ADDRESS, DEFAULT_MOBILE_NUMBER, DEFAULT_USER_EMAIL)


@pytest.fixture
def default_reservation(default_travel, default_user):
    return Reservation(default_travel, default_user)

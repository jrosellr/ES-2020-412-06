import pytest
from src.Skyscanner import Skyscanner
from src.Reservation import Reservation
from src.Bank import Bank
from src.Travel import Travel
from src.Flight import Flight
from src.Flights import Flights
from src.User import User
from .test_constants import *

# TODO: add documentation to fixtures


@pytest.fixture
def mock_fetch_prices(monkeypatch):
    def mock_fetch_ticket_price(*args):
        return MOCKED_TICKET_PRICE

    monkeypatch.setattr(Skyscanner, "fetch_ticket_price", mock_fetch_ticket_price)


@pytest.fixture
def mock_bank_error(monkeypatch):
    def mock_do_payment_error(*args):
        raise ConnectionRefusedError("Connection with bank failed.")

    monkeypatch.setattr(Bank, "do_payment", mock_do_payment_error)


@pytest.fixture
def mock_bank_success(monkeypatch):
    def mock_do_payment_successful(*args):
        return MOCKED_BANK_SUCCESS_RET

    monkeypatch.setattr(Bank, "do_payment", mock_do_payment_successful)


@pytest.fixture
def mock_skyscanner_error(monkeypatch):
    def mock_confirm_reserve_error(*args):
        raise ConnectionRefusedError("Connection with SkyScanner failed.")

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
def default_travel(default_flights):
    return Travel(DEFAULT_NUM_TRAVELERS, default_flights)


@pytest.fixture
def default_user():
    return User(DEFAULT_USER_NAME, DEFAULT_DNI, DEFAULT_ADDRESS, DEFAULT_MOBILE_NUMBER, DEFAULT_USER_EMAIL)


@pytest.fixture
def default_reservation(default_travel, default_user):
    return Reservation(default_travel, default_user)

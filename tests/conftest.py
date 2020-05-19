import pytest
from src.Skyscanner import Skyscanner
from src.Bank import Bank
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
        return MOCKED_BANK_ERROR_RET

    monkeypatch.setattr(Bank, "do_payment", mock_do_payment_error)


@pytest.fixture
def mock_bank_success(monkeypatch):
    def mock_do_payment_successful(*args):
        return MOCKED_BANK_SUCCESS_RET

    monkeypatch.setattr(Bank, "do_payment", mock_do_payment_successful)

from src.PaymentData import PaymentData
from .test_constants import *


# TODO: add fixtures for PaymentData unit tests
def test_payment_data_ctor():
    """ Test case for payment_data.__init__(**) method

        ---
    EXPECTED BEHAVIOUR:
        The object is instantiated with the default values

    """

    p = PaymentData(DEFAULT_CARD_HOLDER_NAME, DEFAULT_CARD_NUMBER, DEFAULT_CARD_CVV, DEFAULT_PAYMENT_AMOUNT, DEFAULT_CARD_TYPE)
    assert p.user_name == DEFAULT_CARD_HOLDER_NAME
    assert p.card_number == DEFAULT_CARD_NUMBER
    assert p.security_code == DEFAULT_CARD_CVV
    assert p.amount != 0
    assert p.amount == DEFAULT_PAYMENT_AMOUNT
    assert p.credit_card_type == DEFAULT_CARD_TYPE

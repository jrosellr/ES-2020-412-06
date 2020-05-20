from src.PaymentData import PaymentData


def test_payment_data_ctor():
    """ Test case for payment_data.__init__(**) method

        ---

        :return: None
    """

    p = PaymentData('Sample Text', '0000000', '000', 2.0, 'VISA')
    assert p.user_name == 'Sample Text'
    assert p.card_number == '0000000'
    assert p.security_code == '000'
    assert p.amount != 0
    assert p.amount == 2.0
    assert p.credit_card_type == 'VISA'

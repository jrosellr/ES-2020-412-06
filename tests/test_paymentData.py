from src.PaymentData import PaymentData


def test_init():
    p = PaymentData('Sample Text', '0000000', '000', 2.0)
    assert p.user_name == 'Sample Text'
    assert p.card_number == '0000000'
    assert p.security_code == '000'
    assert p.amount != 0
    assert p.amount == 2.0

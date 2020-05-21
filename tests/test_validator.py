from src.Validator import Validator

def test_validate_payment_info():
    """ Test check payment info

    Tests if the payment information, containing a name, dni, email,
    card_number and security_code, is validated with the corresponding
    regular expression.

    :return: None
    """
    name = 'This Is a Good Test'
    dni = '12345678A'
    email = 'good_email@test.uab'
    mobile_number = '123456789'
    card_number = '1234 3456 5678 7890'
    security_code = '123'
    credit_card_type = ['VISA', 'MASTERCARD']

    assert Validator.validate_full_name(name) is not None
    assert Validator.validate_full_name(name) is True
    assert Validator.validate_dni(dni) is not None
    assert Validator.validate_dni(dni) is True
    assert Validator.validate_email(email) is not None
    assert Validator.validate_email(email) is True
    assert Validator.validate_mobile_number(mobile_number) is not None
    assert Validator.validate_mobile_number(mobile_number) is True
    assert Validator.validate_credit_card_number(card_number) is not None
    assert Validator.validate_credit_card_number(card_number) is True
    assert Validator.validate_credit_security_code(security_code) is not None
    assert Validator.validate_credit_security_code(security_code) is True
    assert Validator.validate_credit_card_type(credit_card_type[0]) is True
    assert Validator.validate_credit_card_type(credit_card_type[1]) is True


def test_validate_payment_info_error():
    """ Test check invalid payment info

    Tests if the payment information, containing a name, dni, email,
    card_number and security_code, is invalid because doesn't match
    with the corresponding regular expression.

    :return: None
    """

    name = "7his_1s-a Bad 7est"
    dni = '2EFC678A9'
    email = 'bad@e/mail@test uab'
    mobile_number = '123a56aa'
    card_number = '4568 98761 234 5698'
    security_code = 'a56'
    credit_card_type = 'EXPRESS'

    assert Validator.validate_full_name(name) is not None
    assert Validator.validate_full_name(name) is False
    assert Validator.validate_dni(dni) is not None
    assert Validator.validate_dni(dni) is False
    assert Validator.validate_email(email) is not None
    assert Validator.validate_email(email) is False
    assert Validator.validate_mobile_number(mobile_number) is not None
    assert Validator.validate_mobile_number(mobile_number) is False
    assert Validator.validate_credit_card_number(card_number) is not None
    assert Validator.validate_credit_card_number(card_number) is False
    assert Validator.validate_credit_security_code(security_code) is not None
    assert Validator.validate_credit_security_code(security_code) is False
    assert Validator.validate_credit_card_type(credit_card_type[0]) is False

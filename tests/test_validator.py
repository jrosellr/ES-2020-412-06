from src.Validator import Validator
from src.Reservation import Reservation

def test_validate_payment_info():
    name = 'This Is a Good Test'
    dni = '12345678A'
    email = 'good_email@test.uab'
    card_number = '1234 3456 5678 7890'
    security_code = '123'

    assert Validator._validate_full_name(name) == True
    assert Validator._validate_full_name(name) != False
    assert Validator._validate_dni(dni) == True
    assert Validator._validate_dni(dni) != False
    assert Validator._validate_email(email) == True
    assert Validator._validate_email(email) != False
    assert Validator._validate_credit_card_number(card_number) == True
    assert Validator._validate_credit_card_number(card_number) != False
    assert Validator._validate_credit_security_code(security_code) == True
    assert Validator._validate_credit_security_code(security_code) != False

def test_validate_payment_info_error():
    name = "7his_1s-a Bad 7est"
    dni = '2EFC678A9'
    email = 'bad@e/mail@test uab'
    card_number = '4568 98761 234 5698'
    security_code = 'a56'

    assert Validator._validate_full_name(name) != True
    assert Validator._validate_full_name(name) == False
    assert Validator._validate_dni(dni) != True
    assert Validator._validate_dni(dni) == False
    assert Validator._validate_email(email) != True
    assert Validator._validate_email(email) == False
    assert Validator._validate_credit_card_number(card_number) != True
    assert Validator._validate_credit_card_number(card_number) == False
    assert Validator._validate_credit_security_code(security_code) != True
    assert Validator._validate_credit_security_code(security_code) == False
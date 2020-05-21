from src.Reservation import Reservation
from src.User import User
from src.PaymentData import PaymentData
import re

class Validator:
    """ Handles the validation of regular expressions of paymentData

    """
    _name_regexp = r'[A-Za-z ]{1,30}'
    _dni_regexp = r'\d{8}[A-Z]'
    _email_regexp = r'\w{1,30}@\w{2,20}\.\w{2,5}'
    _mobile_number_regexp = r'\d\d\d\d\d\d\d\d\d'
    _credit_card_number_regexp = r'\d{4} \d{4} \d{4} \d{4}'
    _credit_card_cvv_regexp = r'\d\d\d'


    @staticmethod
    def validate_billing_data(user: User):
        try:    # FIXME: Put exceptions when method does not work
            Validator._validate_full_name(user.full_name)
            Validator._validate_dni(user.dni)
            Validator._validate_email(user.email)
            Validator._validate_mobile_number(user.mobile_number)
        except ValueError:
            return False
        return True

    @staticmethod
    def validate_credit_card_type(credit_card_type: str):
        if credit_card_type is 'VISA' or credit_card_type is 'MASTERCARD':
            return True
        else:
            return False

    @staticmethod
    def validate_payment_data(paymentData: PaymentData):
        try:
            Validator._validate_full_name(paymentData.user_name)
            Validator._validate_credit_card_number(paymentData.card_number)
            Validator._validate_credit_security_code(paymentData.security_code)
        except AssertionError:
            raise AssertionError('Error: Input payment data again.')


    @staticmethod
    def _validate_full_name(name: str):
        if re.fullmatch(Validator._name_regexp, name) is not None:
            return True
        else:
            return False

    @staticmethod
    def _validate_dni(dni: str):
        if re.fullmatch(Validator._dni_regexp, dni) is not None:
            return True
        else:
            return False

    @staticmethod
    def _validate_email(email: str):
        if re.fullmatch(Validator._email_regexp, email) is not None:
            return True
        else:
            return False

    @staticmethod
    def _validate_mobile_number(mobile_number: str):
        if re.fullmatch(Validator._mobile_number_regexp, mobile_number) is not None:
            return True
        else:
            return False

    @staticmethod
    def _validate_credit_card_number(card_number: str):
        if re.fullmatch(Validator._credit_card_number_regexp, card_number) is not None:
            return True
        else:
            return False

    @staticmethod
    def _validate_credit_security_code(security_code: str):
        if re.fullmatch(Validator._credit_card_cvv_regexp, security_code) is not None:
            return True
        else:
            return False



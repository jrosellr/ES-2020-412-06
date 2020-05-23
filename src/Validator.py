from src.User import User
from src.PaymentData import PaymentData
import re

class Validator:
    """ Handles the validation of regular expressions of User and paymentData
    ----

    Public methods:
        validate_billing_data(user)
        validate_credit_card_type(credit_card_type)
        validate_payment_data(user_name, card_number, security_code)

    ----

    Instance variables:
        _name_regexp: regular expression for names

        _dni_regexp: regular expression for dni

        _email_regexp: regular expression for emails

        _mobile_number_regexp: regular expression for mobile numbers

        _credit_card_number_regexp: regular expression for credit card numbers

        _credit_card_cvv_regexp: regular expression for credit card security code
    """

    _name_regexp = r'[A-Za-z ]{1,30}'
    _dni_regexp = r'\d{8}[A-Z]'
    _email_regexp = r'\w{1,30}@\w{2,20}\.\w{2,5}'
    _mobile_number_regexp = r'\d\d\d\d\d\d\d\d\d'
    _credit_card_number_regexp = r'\d{4} \d{4} \d{4} \d{4}'
    _credit_card_cvv_regexp = r'\d\d\d'


    @staticmethod
    def validate_billing_data(user: User):
        """ Validate the User data
        ----

        Called methods:
            _validate_full_name(name)
            _validate_dni(dni)
            _validate_email(email)
            _validate_mobile_number(mobile_number)
        ----

        :return: bool representing the validation of the billing data
        """

        return Validator._validate_full_name(user.full_name) and \
               Validator._validate_dni(user.dni) and \
               Validator._validate_email(user.email) and \
               Validator._validate_mobile_number(user.mobile_number)

    @staticmethod
    def validate_credit_card_type(credit_card_type: str):
        """ Validate the credit card type

        :return: bool representing if the credit_card_type is 'VISA' or 'MASTERCARD'
        """

        return credit_card_type is 'VISA' or credit_card_type is 'MASTERCARD'

    @staticmethod
    def validate_payment_data(user_name, card_number, security_code):
        """ Validate the payment data
        ----

        Called methods:
            _validate_full_name(name)
            _validate_credit_card_number(card_number)
            _validate_credit_security_code(security_code)
        ----

        :return: bool representing the validation of the payment data
        """

        return Validator._validate_full_name(user_name) and \
               Validator._validate_credit_card_number(card_number) and \
               Validator._validate_credit_security_code(security_code)

    @staticmethod
    def _validate_full_name(name: str):
        """ Validate the given name

        :return: bool representing the validation of the name
        """

        return re.fullmatch(Validator._name_regexp, name) is not None

    @staticmethod
    def _validate_dni(dni: str):
        """ Validate the given dni

        :return: bool representing the validation of the dni
        """

        return re.fullmatch(Validator._dni_regexp, dni) is not None

    @staticmethod
    def _validate_email(email: str):
        """ Validate the given email

        :return: bool representing the validation of the email
        """

        return re.fullmatch(Validator._email_regexp, email) is not None

    @staticmethod
    def _validate_mobile_number(mobile_number: str):
        """ Validate the given mobile number

        :return: bool representing the validation of the mobile number
        """

        return re.fullmatch(Validator._mobile_number_regexp, mobile_number) is not None

    @staticmethod
    def _validate_credit_card_number(card_number: str):
        """ Validate the given credit card number

        :return: bool representing the validation of the credit card number
        """

        return re.fullmatch(Validator._credit_card_number_regexp, card_number) is not None

    @staticmethod
    def _validate_credit_security_code(security_code: str):
        """ Validate the given credit card security code

        :return: bool representing the validation of the credit card security code
        """

        return re.fullmatch(Validator._credit_card_cvv_regexp, security_code) is not None

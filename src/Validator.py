from src.Reservation import Reservation
import re

class Validator:
    def __init__(self, _email_regexp: str, _credit_card_number_regexp: str, _credit_card_sec_code_regexp: str):
        self._email_regexp = None
        self._credit_card_number_regexp = None
        self._credit_card_sec_code_regexp = None

    def validate_full_name(self, name: str):
        result = re.fullmatch('[A-Za-z ]{1,30}', name)

    def validate_dni(self, dni: str):
        result = re.fullmatch('\d{8}[A-Z]', dni)

    def validate_email(email: str):
        result = re.fullmatch('\w{1,30}@\w{2,20}\.\w{2,5}', email)

    def validate_credit_card_number(self, card_number: str):
        result = re.fullmatch('\d{4} \d{4} \d{4} \d{4}', card_number)

    def validate_credit_security_code(self, security_code: str):
        result = re.fullmatch('\d\d\d', security_code)

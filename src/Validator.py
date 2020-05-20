from src.Reservation import Reservation
import re

class Validator:
    def __init__(self, _email_regexp: str, _credit_card_number_regexp: str, _credit_card_sec_code_regexp: str):
        self._email_regexp = None
        self._credit_card_number_regexp = None
        self._credit_card_sec_code_regexp = None

    def _validate_full_name(name: str):
        if re.fullmatch('[A-Za-z ]{1,30}', name) is not None:
            return True
        else:
            return False

    def _validate_dni(dni: str):
        if re.fullmatch('\d{8}[A-Z]', dni) is not None:
            return True
        else:
            return False

    def _validate_email(email: str):
        if re.fullmatch('\w{1,30}@\w{2,20}\.\w{2,5}', email) is not None:
            return True
        else:
            return False

    def _validate_credit_card_number(card_number: str):
        if re.fullmatch('\d{4} \d{4} \d{4} \d{4}', card_number) is not None:
            return True
        else:
            return False

    def _validate_credit_security_code(security_code: str):
        if re.fullmatch('\d\d\d', security_code) is not None:
            return True
        else:
            return False

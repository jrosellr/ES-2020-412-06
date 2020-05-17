from src.User import User
from src.PaymentData import PaymentData


class Bank:
    """ Wrapper for VISA and MASTERCARD APIs

    """

    def __init__(self):
        pass

    @staticmethod
    def do_payment(user: User, payment_data: PaymentData):
        return True

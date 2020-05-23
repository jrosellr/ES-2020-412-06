from enum import Enum, unique, auto


@unique
class Response(Enum):
    """ Class dedicated to check if the interactions between the web and the user have been successful

    """
    CONFIRMATION_SUCCESSFUL = auto()
    RESERVATION_DATA_UPDATED = auto()
    INVALID_BILLING_DATA = auto()
    INVALID_PAYMENT_METHOD = auto()
    INVALID_PAYMENT_DATA = auto()
    BANK_ERROR = auto()
    SKYSCANNER_ERROR = auto()
    BOOKING_ERROR = auto()
    RENTALCARS_ERROR = auto()

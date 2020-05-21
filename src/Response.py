from enum import Enum, unique, auto


@unique
class Response(Enum):
    CONFIRMATION_SUCCESSFUL = auto()
    INVALID_BILLING_INFO = auto()
    INVALID_CARD_TYPE = auto()
    INVALID_PAYMENT_INFO = auto()
    BANK_ERROR = auto()
    SKYSCANNER_ERROR = auto()
    BOOKING_ERROR = auto()
    RENTALCARS_ERROR = auto()

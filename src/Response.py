from enum import Enum, unique, auto


@unique
class Response(Enum):
    """ Enum that encodes the different response codes this module sends back to the interface

    CODES:
        CONFIRMATION_SUCCESSFUL: code sent when the reserve confirmation
        has been carried out successfully

        RESERVATION_DATA_UPDATED: code sent when the user's data has been processed and stored correctly

        INVALID_BILLING_DATA: error code sent when the user's billing
        data is invalid, restarting the operation

        INVALID_PAYMENT_METHOD: error code sent when the user's payment method
        is invalid, restarting the operation

        INVALID_PAYMENT_DATA: error code sent when the user's payment data
        is invalid, restarting the operation

        BANK_ERROR: error code sent when the module has exhausted the connection
        attempts with the Bank API, aborting the confirmation process

        SKYSCANNER_ERROR: error code sent when the module has exhausted the connection
        attempts with the Skyscanner API, aborting the confirmation process

        BOOKING_ERROR: error code sent when the module has exhausted the connection
        attempts with the Booking API, aborting the confirmation process

        RENTALCARS_ERROR: error code sent when the module has exhausted the connection
        attempts with the Rentalcars API, aborting the confirmation process
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

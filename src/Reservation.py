from src.Travel import Travel
from src.User import User
from src.PaymentData import PaymentData
from src.Skyscanner import Skyscanner
from src.Booking import Booking
from src.Rentalcars import Rentalcars
from src.Bank import Bank
from src.Response import Response
from src.Validator import Validator
import copy


class Reservation:
    """ Handles reservation data and reservation confirmation

    ----

    Public methods:
        confirm(self, name, card_number, security_code)

    ----

    Instance variables:
        travel: The User's Travel

        user: The User object who makes the reservation
    """

    MAX_RETRIES = 4

    def __init__(self, travel: Travel):
        """ Copies a travel and user instance and initializes the total_price at 0

        :param travel: copy of Travel instance
        :param user: copy of User instance
        """

        self._travel = copy.deepcopy(travel)
        self._user = None
        self._payment_method = None
        self._payment_data = None

    def save_billing_data(self, full_name: str, dni: str, address: str, mobile_number: str, email: str) -> Response:
        response = Response.INVALID_BILLING_DATA
        usr = User(full_name, dni, address, mobile_number, email)
        if Validator.validate_billing_data(usr):
            self._user = copy.deepcopy(usr)
            response = Response.RESERVATION_DATA_UPDATED

        return response

    def save_payment_method(self, payment_method: str) -> Response:
        response = Response.INVALID_PAYMENT_METHOD
        if Validator.validate_credit_card_type(payment_method):
            self._payment_method = payment_method
            response = Response.RESERVATION_DATA_UPDATED

        return response

    def save_payment_data(self, name: str, card_number: str, security_code: str) -> Response:
        response = Response.INVALID_PAYMENT_DATA
        if Validator.validate_payment_data(name, card_number, security_code):
            self._payment_data = self._process_payment_data(user_name=name,
                                                            card_number=card_number,
                                                            security_code=security_code,
                                                            credit_card_type=self._payment_method)

            response = Response.RESERVATION_DATA_UPDATED

        return response

    def confirm(self) -> Response:
        """ Confirm the reservation

        """

        try:
            if self._confirm_payment(self._payment_data) and self._confirm_flights() and self._confirm_hotels() and self._confirm_cars():
                return Response.CONFIRMATION_SUCCESSFUL
        except ConnectionRefusedError as e:
            return e.args[0]

    def _process_payment_data(self, user_name: str, card_number: str, security_code: str, credit_card_type: str) -> PaymentData:  # FIXME: update documentation
        """ Call _configure_travel and create an instance of PaymentData with the amount calculated.

        :param user_name: string with the name of the card holder
        :param card_number: string containing the card number
        :param security_code: integer with the security code of the card
        :return: instance of PaymentData with the total amount of money to pay and client information
        """

        self._configure_travel()
        return PaymentData(user_name, card_number, security_code, self._travel.cost, credit_card_type)

    def _configure_travel(self):
        self._travel.ticket_price = self._fetch_ticket_price()
        self._travel.hotel_price = self._fetch_hotel_price()
        self._travel.car_price = self._fetch_car_price()

    @staticmethod
    def _fetch_ticket_price() -> float:
        return Skyscanner.fetch_ticket_price()

    @staticmethod
    def _fetch_hotel_price() -> float:
        return Booking.fetch_hotel_price()

    @staticmethod
    def _fetch_car_price() -> float:
        return Rentalcars.fetch_car_price()

    def _confirm_payment(self, payment_data: PaymentData) -> bool:
        retries = 0
        while retries < self.MAX_RETRIES:
            try:
                return Bank.do_payment(self._user, payment_data)
            except ConnectionRefusedError:
                retries += 1

        raise ConnectionRefusedError(Response.BANK_ERROR)

    def _confirm_flights(self) -> bool:
        retries = 0
        while retries < self.MAX_RETRIES:
            try:
                return Skyscanner.confirm_reserve(self._user, self._travel._flights)
            except ConnectionRefusedError:
                retries += 1

        raise ConnectionRefusedError(Response.SKYSCANNER_ERROR)

    def _confirm_hotels(self) -> bool:
        if self._travel.has_hotels:
            retries = 0
            while retries < self.MAX_RETRIES:
                try:
                    return Booking.confirm_reserve(self._user, self._travel._hotels)
                except ConnectionRefusedError:
                    retries += 1
            raise ConnectionRefusedError(Response.BOOKING_ERROR)
        else:
            return True

    def _confirm_cars(self) -> bool:
        if self._travel.has_cars:
            retries = 0
            while retries < self.MAX_RETRIES:
                try:
                    return  Rentalcars.confirm_reserve(self._user, self._travel._cars)
                except ConnectionRefusedError:
                    retries += 1
            raise ConnectionRefusedError(Response.RENTALCARS_ERROR)
        else:
            return True





from src.Travel import Travel
from src.User import User
from src.PaymentData import PaymentData
from src.Skyscanner import Skyscanner
from src.Booking import Booking
from src.Rentalcars import Rentalcars
from src.Bank import Bank
from src.Response import Response
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

    def __init__(self, travel: Travel, user: User):
        """ Copies a travel and user instance and initializes the total_price at 0

        :param travel: copy of Travel instance
        :param user: copy of User instance
        """

        self._travel = copy.deepcopy(travel)
        self._user = copy.deepcopy(user)

    def confirm(self, name: str, card_number: str, security_code: str, credit_card_type: str) -> Response:
        """ Takes the payment data with the total price and proceeds to do the payment and flights confirmation

        :param credit_card_type: card type can be VISA or MASTERCARD, we need to construct a CardType object
        :param name: string with the name of the card holder
        :param card_number: string containing the card number
        :param security_code: integer with the security code of the card
        :return: bool that confirms the payment and flights reservation
        """

        payment_data = self._process_payment_data(name, card_number, security_code, credit_card_type)

        return self._confirm_reservation(payment_data)

    def _process_payment_data(self, name: str, card_number: str, security_code: str, credit_card_type: str) -> PaymentData:  # FIXME: update documentation
        """ Call calculate_flights_price and create an instance of PaymentData with the amount calculated.

        :param name: string with the name of the card holder
        :param card_number: string containing the card number
        :param security_code: integer with the security code of the card
        :return: instance of PaymentData with the total amount of money to pay and client information
        """

        self._configure_travel()
        return PaymentData(name, card_number, security_code, self._travel.cost, credit_card_type)

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

    def _confirm_reservation(self, payment_data: PaymentData) -> Response:
        try:
            if self._confirm_payment(payment_data) and self._confirm_flights() and self._confirm_hotels() and self._confirm_cars():
                return Response.CONFIRMATION_SUCCESSFUL
        except ConnectionRefusedError as e:
            return e.args[0]

    def _confirm_payment(self, payment_data: PaymentData) -> bool:
        return Bank.do_payment(self._user, payment_data)

    def _confirm_flights(self) -> bool:
        retries = 0
        while retries < 3:
            try:
                return Skyscanner.confirm_reserve(self._user, self._travel._flights)
            except ConnectionRefusedError:
                retries += 1

        raise ConnectionRefusedError(Response.SKYSCANNER_ERROR)

    def _confirm_hotels(self) -> bool:
        if self._travel.has_hotels:
            retries = 0
            while retries < 3:
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
            while retries < 3:
                try:
                    return  Rentalcars.confirm_reserve(self._user, self._travel._cars)
                except ConnectionRefusedError:
                    retries += 1
            raise ConnectionRefusedError(Response.RENTALCARS_ERROR)
        else:
            return True





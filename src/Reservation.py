from src.Travel import Travel
from src.User import User
from src.PaymentData import PaymentData
from src.Skyscanner import Skyscanner
from src.Booking import Booking
from src.Rentalcars import Rentalcars
from src.Bank import Bank
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

    def confirm(self, name: str, card_number: str, security_code: str) -> bool:
        """ Takes the payment data with the total price and proceeds to do the payment and flights confirmation

        :param name: string with the name of the card holder
        :param card_number: string containing the card number
        :param security_code: integer with the security code of the card
        :return: bool that confirms the payment and flights reservation
        """

        payment_data = self._process_payment_data(name, card_number, security_code)
        confirm_flights = False

        if Bank.do_payment(self._user, payment_data):
            confirm_flights = Skyscanner.confirm_reserve(self._user, self._travel._flights)
        return confirm_flights

    def _process_payment_data(self, name: str, card_number: str, security_code: str) -> PaymentData:
        """ Call calculate_flights_price and create an instance of PaymentData with the amount calculated.

        :param name: string with the name of the card holder
        :param card_number: string containing the card number
        :param security_code: integer with the security code of the card
        :return: instance of PaymentData with the total amount of money to pay and client information
        """

        self._configure_travel()
        # TODO: add user input validation before returning the PaymentData instance
        return PaymentData(name, card_number, security_code, self._travel.cost)

    def _configure_travel(self):
        self._travel.ticket_price = self._fetch_ticket_price()

    @staticmethod
    def _fetch_ticket_price() -> float:
        return Skyscanner.fetch_ticket_price()

    @staticmethod
    def _fetch_room_price() -> float:
        return Booking.fetch_room_price()

    @staticmethod
    def _fetch_car_price() -> float:
        return Rentalcars.fetch_car_price()

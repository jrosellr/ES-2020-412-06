from src.Travel import Travel
from src.User import User
from src.PaymentData import PaymentData
from src.Skyscanner import Skyscanner
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

    def calculate_total_price(self, flights_price, hotels_price, cars_price):
        """ Calculates the total price of the reservation from the price of the flights, hotels and cars

        :param flights_price: price of the flights
        :param hotels_price: price of the hotels
        :param cars_price: price of the cars
        """

        self.total_price = self.calculate_flights_price(flights_price) + self.calculate_hotels_price(hotels_price) + self.calculate_cars_price(cars_price)

    def add_flight(self, new_flight):
        """ Call the method add_flight from Travel class

        :param new_flight: instance of Flight to be added
        """

        self._travel.add_flight(new_flight)

    def delete_flight(self, code):
        """ Call the method delete_flight from Travel class

        :param code: code of an instance of Flight to be deleted
        """

        self._travel.delete_flight(code)

    def _process_payment_data(self, name: str, card_number: str, security_code: str) -> PaymentData:
        """ Call calculate_flights_price and create an instance of PaymentData with the amount calculated.

        :param name: string with the name of the card holder
        :param card_number: string containing the card number
        :param security_code: integer with the security code of the card
        :return: instance of PaymentData with the total amount of money to pay and client information
        """

        amount = 0
        return PaymentData(name, card_number, security_code, amount)

    def _fetch_ticket_price(self) -> float:
        pass

    def _fetch_room_price(self) -> float:
        pass

    def _fetch_car_price(self) -> float:
        pass

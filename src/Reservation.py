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

    _flight_price = 5.0

    def __init__(self, travel: Travel, user: User):
        """ Copies a travel and user instance and initializes the total_price at 0

        :param travel: copy of Travel instance
        :param user: copy of User instance
        """

        self.travel = copy.deepcopy(travel)
        self.user = copy.deepcopy(user)
        self.total_price = 0.0  # Just in case, if the module fails the price should be at least 0

    def confirm(self, name: str, card_number: str, security_code: str) -> bool:
        """ Takes the payment data with the total price and proceeds to do the payment and flights confirmation

        :param name: string with the name of the card holder
        :param card_number: string containing the card number
        :param security_code: integer with the security code of the card
        :return: bool that confirms the payment and flights reservation
        """

        payment_data = self._process_payment_data(name, card_number, security_code)
        confirm_flights = False

        if Bank.do_payment(self.user, payment_data):
            confirm_flights = Skyscanner.confirm_reserve(self.user, self.travel.flights)
        return confirm_flights

    def calculate_flights_price(self, price: float) -> float:
        """ Calculate the total price from given price by flight and the number of clients

        :param price: price per client, equal for all flights
        :return: float
        """

        total_price = 0
        if len(self.travel.flights.flights) != 0:
            num_clients = self.travel.get_num_clients()
            total_price = price * num_clients
        return total_price

    def calculate_hotels_price(self, price):
        return 0

    def calculate_cars_price(self, price):
        return 0

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

        self.travel.add_flight(new_flight)

    def delete_flight(self, code):
        """ Call the method delete_flight from Travel class

        :param code: code of an instance of Flight to be deleted
        """

        self.travel.delete_flight(code)

    def _process_payment_data(self, name: str, card_number: str, security_code: str):
        """ Call calculate_flights_price and create an instance of PaymentData with the amount calculated.

        :param name: string with the name of the card holder
        :param card_number: string containing the card number
        :param security_code: integer with the security code of the card
        :return: instance of PaymentData with the total amount of money to pay and client information
        """

        amount = self.calculate_flights_price(self._flight_price)
        return PaymentData(name, card_number, security_code, amount)

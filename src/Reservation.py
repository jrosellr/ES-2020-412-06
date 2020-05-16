from src.Travel import Travel
from src.User import User
from src.PaymentData import PaymentData
import copy


class Reservation:

    def __init__(self, travel: Travel, user: User, payment_data: PaymentData):
        self.travel = copy.deepcopy(travel)
        self.user = copy.deepcopy(user)
        self.payment_data = copy.deepcopy(payment_data)
        self.total_price = 0.0  # Just in case, if the module fails the price should be at least 0

    def calculate_flights_price(self, price):
        return price * len(self.travel.flights.flights) * self.travel.flights.flights[0].num_clients

    def calculate_hotels_price(self, price):
        return 0

    def calculate_cars_price(self, price):
        return 0

    def calculate_total_price(self, flights_price, hotels_price, cars_price):
        self.total_price = self.calculate_flights_price(flights_price) + self.calculate_hotels_price(hotels_price) + self.calculate_cars_price(cars_price)

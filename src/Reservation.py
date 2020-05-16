from src.Travel import Travel
from src.User import User
from src.PaymentData import PaymentData
import copy


class Reservation:
    """ Handles reservation data and reservation confirmation

    """
    def __init__(self, travel: Travel, user: User):
        self.travel = copy.deepcopy(travel)
        self.user = copy.deepcopy(user)
        self.total_price = 0.0  # Just in case, if the module fails the price should be at least 0

    def confirm(self):
        pass

    def calculate_flights_price(self, price) -> float:
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
        self.total_price = self.calculate_flights_price(flights_price) + self.calculate_hotels_price(hotels_price) + self.calculate_cars_price(cars_price)

    def add_flight(self, new_flight):
        self.travel.add_flight(new_flight)

    def delete_flight(self, code):
        self.travel.delete_flight(code)

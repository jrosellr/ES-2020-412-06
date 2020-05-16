from src.Flights import Flights
import copy

class Travel:

    def __init__(self, flights: Flights, hotels=None, cars=None):
        self.flights = copy.deepcopy(flights)
        self.hotels = copy.deepcopy(hotels)
        self.cars = copy.deepcopy(cars)

    def get_num_clients(self):
        num_clients = 0
        for code, flight in self.flights.flights.items():
            num_clients += flight.num_clients
        return num_clients

    def add_flight(self, new_flight):
        self.flights.add_flight(new_flight)

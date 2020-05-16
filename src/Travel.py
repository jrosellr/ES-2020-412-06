from src.Flights import Flights


class Travel:

    def __init__(self, flights: Flights, hotels=None, cars=None):
        self.flights = flights
        self.hotels = hotels
        self.cars = cars

    def get_num_clients(self):
        num_clients = 0
        for code, flight in self.flights.flights.items():
            num_clients += flight.num_clients
        return num_clients

from src.Flights import Flights


class Travel:

    def __init__(self, flights: Flights, hotels=None, cars=None):
        self.flights = flights
        self.hotels = hotels
        self.cars = cars

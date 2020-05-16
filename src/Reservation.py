class Reservation:

    def __init__(self, travel: Travel, user: User, payment_data: PaymentData):
        self.travel = travel
        self.user = user
        self.payment_data = payment_data

    def calculate_flights_price(self, price):
        return (price * len(travel.flights.flights) * travel.flights.flights[0].num_clients)

    def calculate_hotels_price(self, price):
        pass

    def calculate_cars_price(self, price):
        pass

    def calculate_total_price(self, flights_price, hotels_price, cars_price):
        self.total_price = self.calculate_fligts_price(flights_price) + self.calculate_hotels_price(hotels_price) + self.calculate_cars_price(cars_price)

from src.User import User
from src.Cars import Cars


class Rentalcars:
    """ Class that wraps the RentalCars API

    """
    def __init__(self):
        pass

    @staticmethod
    def confirm_reserve(user: User, cars: Cars) -> bool:
        return True

    @staticmethod
    def fetch_car_price() -> float:
        pass

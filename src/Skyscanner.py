from src.User import User
from src.Flights import Flights


class Skyscanner:
    """ Class that wraps the SkyScanner API

    """
    def __init__(self):
        pass

    @staticmethod
    def confirm_reserve(user: User, flights: Flights) -> bool:
        return True

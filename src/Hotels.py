from src.Hotel import Hotel


class Hotels:
    """ A Value-Object that holds the different Hotels a user wants to reserve

        ----

            Instance variables:
                Hotels: uses a dictionary to enforce the singularity of each hotel
    """

    def __init__(self, hotels: list):
        """ Creates a dictionary using the hotel codes as keys

        :param hotels: a list of objects of type Hotel
        """
        if len(hotels) != 0:
            self._hotels = {hotel.code: hotel for hotel in hotels}
        else:
            self._hotels: dict = {}

    def __getitem__(self, key: str):
        if key in self._hotels:
            return self._hotels[key]

    def __setitem__(self, key: str, value: Hotel):
        if key not in self._hotels:
            self._hotels[key] = value

    def __delitem__(self, key: str):
        if key in self._hotels:
            del self._hotels[key]

    def __len__(self):
        return len(self._hotels)


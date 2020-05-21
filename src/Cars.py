from src.Flight import Flight


class Cars:
    """ A Value-Object used to hold the car data

    """
    def __init__(self, cars: list):

        if len(cars) != 0:
            self._cars = {car.code: car for car in cars}
        else:
            self._cars: dict = {}

    def __getitem__(self, key: str):
        if key in self._cars:
            return self._cars[key]

    def __len__(self):
        return len(self._cars)

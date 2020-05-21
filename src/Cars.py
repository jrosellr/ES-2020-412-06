from src.Flight import Flight


class Cars:
    """ A Value-Object that holds the different cars a user wants to reserve

    ----

        Instance variables:
            cars: uses a dictionary to enforce the singularity of each car
    """
    def __init__(self, cars: list):
        """ Creates a dictionary using the car codes as keys

        :param cars: a list of objects of type Car
        """
        if len(cars) != 0:
            self._cars = {car.code: car for car in cars}
        else:
            self._cars: dict = {}

    def __getitem__(self, key: str):
        if key in self._cars:
            return self._cars[key]

    def __len__(self):
        return len(self._cars)

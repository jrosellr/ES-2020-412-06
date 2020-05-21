from src.Car import Car
from src.Cars import Cars
from .test_constants import *


def test_cars_ctor(default_car_list: list):
    """ Test case for Cars.__init__(**) method

    Tests the constructor of the Cars class

    EXPECTED BEHAVIOUR:
        The object is instantiated with the default values
    """

    cars = Cars(default_car_list)

    assert len(cars) != 0
    assert len(cars) == DEFAULT_CARS_LEN


def test_getitem_cars(default_cars: Cars, default_car_list: list):
    """ Test case for Cars.__delitem__(**) method

    RESTRICTION:
        The code of the Cart object to be searched should exist in Cars' dictionary.

    TEST CASE:
        Get the object with the given code in the Cars' dictionary.

    EXPECTED BEHAVIOUR:
        The instance of car searched is returned.
    """
    car = default_car_list[0]
    assert default_cars.__getitem__(car.code) == car
    assert default_cars._cars[car.code] == car

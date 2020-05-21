from src.Car import Car
from .test_constants import *


def test_car_ctor(default_car_list):
    """ Test case for Car.__init__(**) method

    Tests the constructor of the Car class

    EXPECTED BEHAVIOUR:
        The object is instantiated with the default values
    """

    default_car_0 = default_car_list[0]
    assert default_car_0.code == DEFAULT_CAR_CODE_0
    assert default_car_0.brand == DEFAULT_CAR_BRAND
    assert default_car_0.pick_up_place == DEFAULT_CAR_PICK_UP_PLACE
    assert default_car_0.days_reserved == DEFAULT_CAR_DAYS_RESERVED

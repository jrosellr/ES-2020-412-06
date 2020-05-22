from src.Hotel import Hotel
from .test_constants import *


def test_hotel_ctor(default_hotel_list):
    """ Test case for Hotel.__init__(**) method

    Tests the constructor of the Hotel class

    EXPECTED BEHAVIOUR:
        The object is instantiated with the default values
    """

    default_hotel_0 = default_hotel_list[0]
    assert default_hotel_0.code == DEFAULT_HOTEL_CODE_0
    assert default_hotel_0.name == DEFAULT_HOTEL_NAME_0
    assert default_hotel_0.days_reserved == DEFAULT_HOTEL_DAYS_RESERVED

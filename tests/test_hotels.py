from src.Hotel import Hotel
from src.Hotels import Hotels
from .test_constants import *


def test_hotels_ctor(default_hotel_list: list):
    """ Test case for Hotels.__init__(**) method

    Tests the constructor of the Hotels class

    EXPECTED BEHAVIOUR:
        The object is instantiated with the default values
     """

    hotels = Hotels(default_hotel_list)

    assert len(hotels) != 0
    assert len(hotels) == DEFAULT_HOTELS_LEN


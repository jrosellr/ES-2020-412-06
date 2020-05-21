from src.Flight import Flight
from .test_constants import *


def test_flight_ctor(default_flight_list):
    """ Test case for Flight.__init__(**) method

    Tests the constructor of the Flight class

    EXPECTED BEHAVIOUR:
        The object is instantiated with the default values
    """

    default_flight_0 = default_flight_list[0]
    assert default_flight_0.code == DEFAULT_FLIGHT_CODE_0
    assert default_flight_0.passengers == DEFAULT_NUM_TRAVELERS
    assert default_flight_0.destination == DEFAULT_FLIGHT_DESTINATION

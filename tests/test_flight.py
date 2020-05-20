from src.Flight import Flight
from .test_constants import *

def test_flight_ctor(default_flight_list):
    """ Test case for flight.__init__(**) method

        ---

        :return: None
    """

    default_flight_0 = default_flight_list[0]
    assert default_flight_0.code == DEFAULT_FLIGHT_CODE_0
    assert default_flight_0.passengers == DEFAULT_FLIGHT_PASSENGERS
    assert default_flight_0.destination == DEFAULT_FLIGHT_DESTINATION

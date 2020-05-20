from src.Flight import Flight
from src.Flights import Flights
from .test_constants import *


def test_flights_ctor(default_flights: Flights):
    """ Test case for Flights.__init__(**) method

    Tests the constructor of the Flights class

    EXPECTED BEHAVIOUR:
        The object is instantiated with the default values
    """

    assert len(default_flights) != 0
    assert len(default_flights) == DEFAULT_FLIGHTS_LEN
    assert default_flights.passengers_per_flight == DEFAULT_FLIGHT_PASSENGERS


def test_setitem_incorrect_flight(default_flights: Flights, default_new_flight: Flight):
    """ Test case for Flights.__setitem__(**) method

    RESTRICTION:
        The codes of the flights stored in Flights should be unique

    TEST CASE:
        Insertion of a Flight object with a duplicated code in Flights' dictionary.

    EXPECTED BEHAVIOUR:
        The insertion is not carried out and Flights is not modified.
    """

    old_len = len(default_flights)
    default_new_flight.code = DEFAULT_FLIGHT_CODE_0
    default_flights[default_new_flight.code] = default_new_flight

    assert old_len != 0
    assert len(default_flights) == old_len


def test_setitem_new_flight(default_flights: Flights, default_new_flight: Flight):
    """ Test case for Flights.__setitem__(**) method

    RESTRICTION:
        The codes of the flights stored in Flights should be unique

    TEST CASE:
        Insertion of a Flight object with a new code not present in Flights' dictionary.

    EXPECTED BEHAVIOUR:
        The insertion is performed and Flights has a new entry in its dictionary.
    """

    old_len = len(default_flights)
    default_flights[default_new_flight.code] = default_new_flight

    assert old_len != 0
    assert len(default_flights) != old_len
    assert len(default_flights) == old_len + 1


def test_delitem_existing_flight(default_flights: Flights):
    """ Test case for Flights.__delitem__(**) method

    Tests the __delitem__ mutator of Flights.

    RESTRICTION:
        The code of the Flight object to be deleted should exist in Flights' dictionary.

    TEST CASE:
        Deletion of a Flight object with a code present in Flights' dictionary.

    EXPECTED BEHAVIOUR:
        The deletion is performed and Flights has one less entry in its dictionary.
    """

    del default_flights[DEFAULT_FLIGHT_CODE_0]
    assert len(default_flights) == DEFAULT_FLIGHTS_LEN - 1


def test_delitem_non_existing_flight(default_flights: Flights):
    """ Test case for Flights.__delitem__(**) method

    RESTRICTION:
        The code of the Flight object to be deleted should exist in Flights' dictionary.

    TEST CASE:
        Deletion of a Flight object with a code not present in Flights' dictionary.

    EXPECTED BEHAVIOUR:
        The deletion is not performed and Flights is not modified.
    """

    del default_flights[DEFAULT_NEW_FLIGHT_CODE]
    assert len(default_flights) != 0
    assert len(default_flights) == DEFAULT_FLIGHTS_LEN

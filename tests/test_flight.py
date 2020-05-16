from src.Flight import Flight


def test_flight_ctor():
    """ Test case for flight.__init__(**) method

        ---

        :return: None
    """

    f = Flight('', '', 0)
    assert f.num_clients == 0
    assert f.code == ''
    assert f.destination == ''

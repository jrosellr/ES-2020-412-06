from src.Flight import Flight


def test_init():
    f = Flight('', '', 0)
    assert f.num_clients == 0
    assert f.code == ''
    assert f.destination == ''

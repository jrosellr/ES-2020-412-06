from src.Reservation import Reservation
from src.Travel import Travel
from src.User import User
from src.Flights import Flights
from src.Flight import Flight
from src.PaymentData import PaymentData
from src.Bank import Bank


def test_reservation_ctor():
    """ Unit test for Reservation.__init__(**)

    :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'test', 0)
    ]))
    reservation = Reservation(travel, usr)
    assert isinstance(reservation, Reservation)

    travel.flights['00'].destination = 'Berlin'
    assert reservation.travel.flights['00'] != travel.flights['00']


def test_reservation_add_new_flight():
    """ Unit test for Reservation.add_flights(**) for new flight

        Length of flights list should be old_len + 1 new element
        :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'test', 0)
    ]))
    reservation = Reservation(travel, usr)
    old_len = len(reservation.travel.flights)
    new_flight = Flight('01', '', 0)
    reservation.add_flight(new_flight)
    new_len = len(reservation.travel.flights)
    assert new_len != 0
    assert new_len != old_len
    assert new_len == old_len + 1


def test_reservation_add_same_flight():
    """ Unit test for Reservation.add_flights(**) for same flight

        Length of flights list should be the same as old_len
        :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'test', 0)
    ]))
    reservation = Reservation(travel, usr)
    old_len = len(reservation.travel.flights)
    new_flight = Flight('00', '', 0)
    reservation.add_flight(new_flight)
    new_len = len(reservation.travel.flights)
    assert new_len != 0
    assert new_len == old_len


def test_reservation_add_flight_empty_travel():
    """ Unit test for Reservation.add_flights(**) from empty travel

        Length of flights list should be old_len + 1 new element
        :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([]))
    reservation = Reservation(travel, usr)
    old_len = len(reservation.travel.flights)
    new_flight = Flight('00', '', 0)
    reservation.add_flight(new_flight)
    new_len = len(reservation.travel.flights)
    assert new_len != 0
    assert new_len != old_len
    assert new_len == old_len + 1


def test_reservation_delete_flights_existing_flight():
    """ Unit test for Reservation.delete_flights(**) with existing flight code

        Length of flights list should be old_len - 1 after existing deletion
        :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'test', 0)
    ]))

    reservation = Reservation(travel, usr)
    old_len = len(reservation.travel.flights)

    reservation.delete_flight('00')

    assert len(reservation.travel.flights) != old_len
    assert len(reservation.travel.flights) == old_len - 1


def test_reservation_delete_flights_non_existing_flight():
    """ Unit test for Reservation.delete_flights(**) with non existing flight code

        Length of flights list should be the same after a failed deletion
        :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'test', 0)
    ]))
    reservation = Reservation(travel, usr)
    reservation.delete_flight('01')
    assert len(reservation.travel.flights) == 1
    assert len(reservation.travel.flights) != 0


def test_reservation_calculate_flights_price_no_flights():
    """ Unit test for Reservation.calculate_flights_price(**)

        Calculated price should be zero when there are no destinations/flights
        :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([]))
    reservation = Reservation(travel, usr)
    assert reservation.calculate_flights_price(5) == 0


def test_reservation_calculate_flights_price_no_clients():
    """ Unit test for Reservation.calculate_flights_price(**)

        Calculated price should be zero when there are no clients
        :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([Flight('00', 'Berlin', 0)]))
    reservation = Reservation(travel, usr)
    assert reservation.calculate_flights_price(5) == 0


def test_reservation_calculate_flights_price():
    """ Unit test for Reservation.calculate_flights_price(**)

        Calculated price should be number of clients * price of flight per client * number of flights
        :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'Berlin', 2),
        Flight('01', 'Roma', 2)
    ]))
    reservation = Reservation(travel, usr)
    assert reservation.calculate_flights_price(5) == 20  # 2 Flights * 2 Clients per Flight * 5 = 20


def test_reservation_calculate_flights_price_add_flight():
    """ Unit test for Reservation.calculate_flights_price(**)

        Calculated price should be number of clients * price of flight per client * number of flights
        :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'Berlin', 2),
        Flight('01', 'Roma', 2)
    ]))
    reservation = Reservation(travel, usr)
    assert reservation.calculate_flights_price(5) == 20  # 2 Flights * 2 Clients per Flight * 5 = 20
    reservation.add_flight(Flight('02', '', 2))
    assert reservation.calculate_flights_price(5) == 30  # 3 Flights * 2 Clients per Flight * 5 = 30


def test_reservation_calculate_flights_price_delete_flight():
    """ Unit test for Reservation.calculate_flights_price(**)

        Calculated price should be number of clients * price of flight per client * number of flights
        :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'Berlin', 2),
        Flight('01', 'Roma', 2)
    ]))
    reservation = Reservation(travel, usr)
    assert reservation.calculate_flights_price(5) == 20  # 2 Flights * 2 Clients per Flight * 5 = 20
    reservation.delete_flight('00')
    assert reservation.calculate_flights_price(5) == 10  # 1 Flight * 2 Clients per Flight * 5 = 10


def test_reservation_calculate_flights_price_delete_all_flights():
    """ Unit test for Reservation.calculate_flights_price(**)

        Calculated price should be number of clients * price of flight per client * number of flights
        :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'Berlin', 2),
        Flight('01', 'Roma', 2)
    ]))
    reservation = Reservation(travel, usr)
    assert reservation.calculate_flights_price(5) == 20  # 2 Flights * 2 Clients per Flight * 5 = 20
    reservation.delete_flight('00')
    reservation.delete_flight('01')
    assert reservation.calculate_flights_price(5) == 0  # 0 Flight * 0 Clients per Flight * 5 = 0


def test_reservation_process_payment_data():
    """ Unit test for Reservation._process_payment_data()

        Amount in payment_data should be != 0 and == number of flights * flight price
        :return: None
    """

    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'Berlin', 2),
        Flight('01', 'Roma', 2)
    ]))
    reservation = Reservation(travel, usr)
    payment_data = reservation._process_payment_data('Test', '000000', '000')
    assert isinstance(payment_data, PaymentData)
    assert payment_data.amount != 0
    assert payment_data.amount == (4 * Reservation._flight_price)


def test_confirm_payment_error(monkeypatch):
    """ Unit test for Reservation.confirm() when Bank.do_payment returns False

        reservation.confirm() should be False
        :return: None
    """

    def mock_do_payment(*args):
        return False

    monkeypatch.setattr(Bank, "do_payment", mock_do_payment)
    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'Berlin', 2),
        Flight('01', 'Roma', 2)
    ]))
    reservation = Reservation(travel, usr)
    assert reservation.confirm('Test_card', '', '123') is not None
    assert reservation.confirm('Test_card', '', '123') is not True
    assert reservation.confirm('Test_card', '', '123') is False


def test_confirm_payment_done(monkeypatch):
    """ Mock test for Reservation.confirm() when Bank.do_payment returns True

        reservation.confirm() should be True
        :return: None
    """

    def mock_do_payment(*args):
        return True

    monkeypatch.setattr(Bank, "do_payment", mock_do_payment)
    usr = User('Test', '000000', 'test/address', '666777888', 'test@example.com')
    travel = Travel(Flights([
        Flight('00', 'Berlin', 2),
        Flight('01', 'Roma', 2)
    ]))
    reservation = Reservation(travel, usr)
    assert reservation.confirm('Test_card', '', '123') is not None
    assert reservation.confirm('Test_card', '', '123') is not False
    assert reservation.confirm('Test_card', '', '123') is True

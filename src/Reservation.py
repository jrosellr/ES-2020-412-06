from src.Travel import Travel
from src.User import User
from src.PaymentData import PaymentData
from src.Skyscanner import Skyscanner
from src.Booking import Booking
from src.Rentalcars import Rentalcars
from src.Bank import Bank
from src.Response import Response
from src.Validator import Validator
import copy


class Reservation:
    """ Module interface, handles all reservation data and operations

    ----

    Public methods:
        save_billing_data(self, full_name: str, dni: str, address: str, mobile_number: str, email: str) -> Response

        save_payment_method(self, payment_method: str) -> Response

        save_payment_data(self, name: str, card_number: str, security_code: str) -> Response

        confirm(self) -> Response

    ----

    Instance attributes:
        _travel: The User's Travel

        _user: The User object that holds the user billing data

        _payment_method: The user's payment method, it can be VISA or MASTERCARD

        _payment_data: The user's payment data

    Class attributes:
        MAX_RETRIES: the maximum attempted connections between the module and the APIs
    """

    MAX_RETRIES: int = 4

    def __init__(self, travel: Travel):
        """ Create an instance of a Reservation object

        The only required parameter of the Reservation ctor is a Travel object,
        the other parameters are filled on demand, when the UI sends the user's data

        :param Travel travel: the user's choice of flights, hotels and cars
        """

        self._travel: Travel = copy.deepcopy(travel)
        self._user = None
        self._payment_method = None
        self._payment_data = None

    def save_billing_data(self, full_name: str, dni: str, address: str, mobile_number: str, email: str) -> Response:
        """ Validate the user's billing data and store the data as a User object

        Creates a User object and validates it's data through Validator, if the required
        fields are valid then the user object is stored in the Reservation

        :param full_name: the full name of the user
        :param dni: the DNI (Spanish national identity document) number << VALIDATED >>
        :param address: the address of the user
        :param mobile_number: the user's mobile number << VALIDATED >>
        :param email: the user's email << VALIDATED >>
        :return: Response code to notify the UI of the status of the Reservation object
        """

        response = Response.INVALID_BILLING_DATA
        usr = User(full_name, dni, address, mobile_number, email)
        if Validator.validate_billing_data(usr):
            self._user = copy.deepcopy(usr)
            response = Response.RESERVATION_DATA_UPDATED

        return response

    def save_payment_method(self, payment_method: str) -> Response:
        """ Validate and save the user's preferred payment method

        If the payment method selected by the user is valid then store it in the Reservation

        :param payment_method: a string containing the user's payment method, can be VISA or MASTERCARD << VALIDATED >>
        :return: Response code to notify the UI of the status of the Reservation object
        """

        response = Response.INVALID_PAYMENT_METHOD
        if Validator.validate_credit_card_type(payment_method):
            self._payment_method = payment_method
            response = Response.RESERVATION_DATA_UPDATED

        return response

    def save_payment_data(self, holder_name: str, card_number: str, security_code: str) -> Response:
        """ Validate the user's payment data as a PaymentData object

        If the required fields are validated then process the information as a
        PaymentData object and store it in the Reservation

        :param holder_name: the name of the Card Holder, it doesn't need to be the same as the user's full name
        :param card_number: the card identification number << VALIDATED >>
        :param security_code: the card CVV << VALIDATED >>
        :return: Response code to notify the UI of the status of the Reservation object
        """

        response = Response.INVALID_PAYMENT_DATA
        if Validator.validate_payment_data(holder_name, card_number, security_code):
            self._payment_data = self._process_payment_data(user_name=holder_name,
                                                            card_number=card_number,
                                                            security_code=security_code,
                                                            credit_card_type=self._payment_method)

            response = Response.RESERVATION_DATA_UPDATED

        return response

    def _process_payment_data(self, user_name: str, card_number: str, security_code: str, credit_card_type: str) -> PaymentData:
        """ Call _configure_travel and create an instance of PaymentData with the amount calculated.

        :param user_name: string with the name of the card holder
        :param card_number: string containing the card number
        :param security_code: integer with the security code of the card
        :return: instance of PaymentData with the total amount of money to pay and client information
        """

        self._configure_travel()
        return PaymentData(user_name, card_number, security_code, self._travel.cost, credit_card_type)

    def _configure_travel(self) -> None:
        """ Retrieve the different prices and set the travel accordingly

        :return: None
        """

        self._travel.ticket_price = self._fetch_ticket_price()
        self._travel.hotel_price = self._fetch_hotel_price()
        self._travel.car_price = self._fetch_car_price()

    @staticmethod
    def _fetch_ticket_price() -> float:
        """ Call the Skyscanner API and request the price of a flight ticket

        This process is extremely simplified, in a real world
        scenario we should retrieve the price for each different flight

        :return: the price of a single flight ticket
        """

        return Skyscanner.fetch_ticket_price()

    @staticmethod
    def _fetch_hotel_price() -> float:
        """ Call the Booking API and request the price for all the hotels

        This process is extremely simplified, in a real world
        scenario we should retrieve the price for each room of each different Hotel and check if all makes sense.

        We assume that the number of hotels is correct and that the price we receive takes into account
        the number of travelers and rooms required for all the hotels, for this project we take that
        'single' hotel price and reuse it for all the Hotels.

        :return: the price to use for all the hotels
        """

        return Booking.fetch_hotel_price()

    @staticmethod
    def _fetch_car_price() -> float:
        """ Call the Rentalcars API and request the price to use for all the cars.

        We assume that the number of cars is correct for the given user and travel configuration. The price we
        fetch is used for all the cars.

        :return: the price to use for all the cars
        """
        return Rentalcars.fetch_car_price()

    def confirm(self) -> Response:
        """ Confirm the reservation and return a Response indicating the status of the Reservation

        Calls the confirmation helper methods and returns the appropriate response if one of them fails

        :return: Response code to notify the UI of the status of the Reservation object
        """

        try:
            if self._confirm_payment(self._payment_data) and self._confirm_flights() and self._confirm_hotels() and self._confirm_cars():
                return Response.CONFIRMATION_SUCCESSFUL
        except ConnectionRefusedError as e:
            return e.args[0]

    def _confirm_payment(self, payment_data: PaymentData) -> bool:
        """ Connect to the Bank API and perform the payment

        Catches ConnectionRefusedError(s) thrown by the Bank API and tries to establish the connection again.

        :param payment_data: the stored payment data in the Reservation
        :return: bool value indicating if the payment is done
        """

        retries = 0
        while retries < self.MAX_RETRIES:
            try:
                return Bank.do_payment(self._user, payment_data)
            except ConnectionRefusedError:
                retries += 1

        raise ConnectionRefusedError(Response.BANK_ERROR)

    def _confirm_flights(self) -> bool:
        """ Connect to the Skyscanner API and perform the payment

        Catches ConnectionRefusedError(s) thrown by the Skyscanner API and tries to establish the connection again.

        :return: bool value indicating if the flights are reserved
        """

        retries = 0
        while retries < self.MAX_RETRIES:
            try:
                return Skyscanner.confirm_reserve(self._user, self._travel._flights)
            except ConnectionRefusedError:
                retries += 1

        raise ConnectionRefusedError(Response.SKYSCANNER_ERROR)

    def _confirm_hotels(self) -> bool:
        """ Connect to the Booking API and perform the payment

        Catches ConnectionRefusedError(s) thrown by the Booking API and tries to establish the connection again.

        :return: bool value indicating if the hotels are reserved
        """

        if self._travel.has_hotels:
            retries = 0
            while retries < self.MAX_RETRIES:
                try:
                    return Booking.confirm_reserve(self._user, self._travel._hotels)
                except ConnectionRefusedError:
                    retries += 1
            raise ConnectionRefusedError(Response.BOOKING_ERROR)
        else:
            return True

    def _confirm_cars(self) -> bool:
        """ Connect to the Rentalcars API and perform the payment

        Catches ConnectionRefusedError(s) thrown by the Rentalcars API and tries to establish the connection again.

        :return: bool value indicating if the cars are reserved
        """

        if self._travel.has_cars:
            retries = 0
            while retries < self.MAX_RETRIES:
                try:
                    return  Rentalcars.confirm_reserve(self._user, self._travel._cars)
                except ConnectionRefusedError:
                    retries += 1
            raise ConnectionRefusedError(Response.RENTALCARS_ERROR)
        else:
            return True

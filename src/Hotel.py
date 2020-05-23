class Hotel:
    """ A Value-Object used to hold the Hotel(s) an user wants to reserve
        ----

        Instance variables:
            code: The hotel's code

            name: The hotel's name

            days_reserved: The number of days the user wants to reserve
    """

    def __init__(self, code: str, name: str, days_reserved: int):
        """ Construct a new Hotel object

        :param code: The hotel's code
        :param name: The hotel's name
        :param days_reserved: The number of days the user wants to reserve
        """
        self.code = code
        self.name = name
        self.days_reserved = days_reserved

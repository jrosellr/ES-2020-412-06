class Hotel:  # FIXME: This is supposed to be a Hotel aggregation
    """ A Value-Object used to hold the Hotel(s) an user wants to reserve

    """

    def __init__(self, code: str, name: str, days_reserved: int):
        self.code = code
        self.name = name
        self.days_reserved = days_reserved

class Hotels:  # FIXME: This is supposed to be a Hotel aggregation
    """ A Value-Object used to hold the Hotel(s) an user wants to reserve

    """

    def __init__(self, code, name, num_clients, num_rooms, days_reserved):
        self.code = code
        self.name = name
        self.num_clients = num_clients
        self.num_rooms = num_rooms
        self.days_reserved = days_reserved

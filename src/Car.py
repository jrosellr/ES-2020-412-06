class Car:
    """ A Value-Object to hold car-related data
        ----

        Instance variables:
            code: The car's code

            brand: The car's brand

            pick_up_place: The place where the car will be picked up and delivered back

            days_reserved: The number of days the client has paid to use the car
    """

    def __init__(self, code, brand, pick_up_place, days_reserved):  # FIXME: This is supposed to be a Car aggregate
        """ Construct a new Car object

        :param code: The car's code
        :param brand: The car's brand
        :param pick_up_place: The place where the car will be picked up and delivered back
        :param days_reserved: The number of days the client has paid to use the car
        """
        self.code = code
        self.brand = brand
        self.pick_up_place = pick_up_place
        self.days_reserved = days_reserved

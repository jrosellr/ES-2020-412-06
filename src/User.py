class User:
    """ A Value-Object used to hold the user data

    """
    def __init__(self, full_name: str, nif: str, address: str, mobile_number: str, email: str):
        """ Construct a new User object

        :param full_name: The first name and last name of the user
        :param nif: The identification code of the user (DNI)
        :param address: The user's address
        :param mobile_number: The user's mobile phone number
        :param email: The user's email address
        """

        self.full_name = full_name
        self.nif = nif
        self.address = address
        self.mobile_number = mobile_number
        self.email = email

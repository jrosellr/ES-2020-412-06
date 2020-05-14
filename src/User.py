class User:
    """ A Value-Object used to hold the user data

    """
    def __init__(self, full_name: str, nif: str, address: str, mobile_number: str, email: str):
        self.full_name = full_name
        self.nif = nif
        self.address = address
        self.mobile_number = mobile_number
        self.email = email

    def get_full_name(self) -> str:
        return self.full_name


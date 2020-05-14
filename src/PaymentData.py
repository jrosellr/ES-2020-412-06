class PaymentData:
    """ A Value-Object used to hold the payment data

    :var user_name: The client's name
    :var card_number: The card identifier number
    :var security-code: Three-number security code
    :var amount: The amount to be charged
    :var credit_card_type: The card can be either VISA or MASTERCARD
    """

    def __init__(self, user_name: str, card_number: str, security_code: str, amount: float):
        self.user_name = user_name
        self.card_number = card_number
        self.security_code = security_code
        self.amount = amount
        self.credit_card_type = None  # To be added in the future

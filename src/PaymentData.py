class PaymentData:
    """ A Value-Object used to hold the payment data

        ----

        Instance variables:
            user_name: The client's name

            card_number: The card number

            security-code: CVV (Card Validation Value, 3-digit number for VISA and MASTERCARD)

            amount: The amount of money to be charged

            credit_card_type: The card can be either VISA or MASTERCARD
    """

    def __init__(self, user_name: str, card_number: str, security_code: str, amount: float, credit_card_type: str):
        """ Construct a new PaymentData object

        :param user_name: The user's name
        :param card_number: The card's number
        :param security_code: The card's CVV
        :param amount: The amount of money to be charged
        """

        self.user_name = user_name
        self.card_number = card_number
        self.security_code = security_code
        self.amount = amount
        self.credit_card_type: str = credit_card_type

class PaymentData:  # TODO: Implement DTO internals
    """ A Value-Object used to hold the payment data

    """
    def __init__(self, name: str, card_code: str, security_code, amount, credit_card_type = None):
        self.name = name
        self.card_code = card_code
        self.security_code = security_code
        self.amount = amount
        self.credit_card_type = credit_card_type

from enum import Enum, unique, auto


@unique
class CardType(Enum):
    VISA = auto()
    MASTERCARD = auto()

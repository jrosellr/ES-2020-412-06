from src.User import User
from .test_constants import *

def test_user_ctor():
    """ Test case for user.__init__(**) method

        ---

        :return: None
    """
    user = User(DEFAULT_USER_NAME, DEFAULT_DNI, DEFAULT_ADDRESS, DEFAULT_MOBILE_NUMBER, DEFAULT_USER_EMAIL)
    assert user.full_name == DEFAULT_USER_NAME
    assert user.nif == DEFAULT_DNI
    assert user.address == DEFAULT_ADDRESS
    assert user.mobile_number == DEFAULT_MOBILE_NUMBER
    assert user.email == DEFAULT_USER_EMAIL

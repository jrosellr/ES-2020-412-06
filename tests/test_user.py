from src.User import User


def test_user_ctor():
    """ Test case for user.__init__(**) method

        ---

        :return: None
    """
    user = User('Bob', '12345678A', 'C/Test, 00', '666777888', 'test@example.com')
    assert user.full_name == 'Bob'
    assert user.nif == '12345678A'
    assert user.address == 'C/Test, 00'
    assert user.mobile_number == '666777888'
    assert user.email == 'test@example.com'

from src.User import User
import os

def example1():
    """
    Retrieve the current directory

    Returns:
        Current directory
    """
    current_path = os.getcwd()
    return current_path


def test_get_current_directory(monkeypatch):
    """
    GIVEN a monkeypatched version of os.getcwd()
    WHEN example1() is called
    THEN check the current directory returned
    """
    def mock_getcwd():
        return '/data/user/directory123'

    monkeypatch.setattr(os, 'getcwd', mock_getcwd)
    assert example1() == '/data/user/directory123'


def example_full_name():
    """
    Retrieve the current directory

    Returns:
        Current directory
    """
    usr = User('Bob', '', '', '', '')
    return usr.get_full_name()


def test_user(monkeypatch):
    def mock_get_user_name(*args):
        return 'Antonio Buenaonda'

    monkeypatch.setattr(User, 'get_full_name', mock_get_user_name)
    assert example_full_name() == 'Antonio Buenaonda'

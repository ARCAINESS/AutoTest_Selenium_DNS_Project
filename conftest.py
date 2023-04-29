import pytest
from termcolor import colored


@pytest.fixture()
def set_up():
    print(colored("Start Test", "yellow"))
    yield
    print(colored("Finish Test", "yellow"))

@pytest.fixture(scope="module")
def set_grow():
    print(colored("Enter System", "red"))
    yield
    print(colored("Exit System", "red"))



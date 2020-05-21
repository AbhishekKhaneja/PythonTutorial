import pytest

#fixture is not required it is defined at the global level in conftest file hence commenting the same
#@pytest.fixture() # using fixture so that before running any test it will be executed first
#def setup():
#    yield # using yield it will run after running the actual test
#   print("I will be executed last")

def test_fixtures(setup): #passing the setup as argument
    print("i will perform the actual operations")


# as we have some sort of requirements in our project like we need to perform prerequities before running or after running any test then we use fixture
# it is like @beforetest and @aftertest in java
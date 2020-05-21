#so in this if we want ot use fixtures in each and every test then ist way io pass the fixture name into each and every test as a argument
# 2nd way is to declare IT inside a class and decalre it as :
import pytest

@pytest.mark.usefixtures("setup") #this will use the fixture from conftest file to all the methods declared in the class
class Testexample:

    #def test_fixtures1(setup): #passing the setup as argument
    def test_fixtures1(self):
        print("i will perform the test_fixtures1 operations")



    #def test_fixtures2(setup): #passing the setup as argument
    def test_fixtures2(self):
        print("i will perform the test_fixtures2 operations")


    #def test_fixtures3(setup):  # passing the setup as argument
    def test_fixtures3(self):
        print("i will perform the test_fixtures3 operations")


    #def test_fixtures4(setup):  # passing the setup as argument
    def test_fixtures4(self):
        print("i will perform the test_fixtures4 operations")
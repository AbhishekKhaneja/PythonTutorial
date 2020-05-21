# suppose the requirement is to invoke the browser for every single test case then we should have a common fixture where the browser invocation is written
#conftest is the file name which is the standard to be followed (file name should be same like this)
#defining fixture in this conftest file and now we can call this fixture in every method or whereever it is required

import pytest


#@pytest.fixture() # using fixture so that before running any test it will be executed first
@pytest.fixture(scope="class") # Now it will considered as @BeforeClass like in java ..it will only run once before/after any class -does not matter how many testcases are there
def setup():
    print("I will be executing first")
    yield # using yield it will run after running the actual test
    print("I will be executed last")

@pytest.fixture()
def dataload():
    print("User profile data is being created")
    return["Rahul","Shetty","rahulshettyacademy@gmail.com"]

#fixture for running a single test with multiple sets of data
#data driven and parametrization can be done with return statement in tuple format
@pytest.fixture(params=[("Rahul","Shetty"),("Abhishek","khaneja"),("Jain","Himanshu")])
def crossbrowser(request):
    return request.param
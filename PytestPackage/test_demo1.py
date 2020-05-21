#any pytest filw will start from test_
#pytest method name should start with test
#Any code should be wrapped in method

# if you want o run the Pytest file from the command prompt
# Step 1 go to the exact path like show below
#py.test is the command to run all the test of Pytest
#C:\Users\abhkhane\PycharmProjects\PythonTesting\PytestPackage>py.test
# use command py.test -v ->> to get some more additional details
# be default if you are running the Pyetst file from the cmd then by default console logs should not be printed
#you have to use command py.test -v -s
# in python if we have the same method name then it will overwrite with the latest one

# if you want to run test in groups then you use mark the testcase as @pytest.mark.smoke and then run using command py.test -m smoke -v -s
# if you want to run the test to be skipped @pytest.mark.skip
import pytest

@pytest.mark.xfail # requirement where we have to run the testcase but it should not be reported in the reports then use this
def test_firstProgram(setup): # fixture passed as argument in this method that means before running any method fixture will run from conftest file
    print("Hello")

@pytest.mark.smoke
@pytest.mark.skip
def test_creditcard():
    print("Good Morning")





def test_crossbrowser(crossbrowser):
    print(crossbrowser[1])
    print(crossbrowser[0])
#If you want to run selected file from command prompt frist go to the directory in Cmd and then use py.test filename -v -s
# if you wwant to run some specific testcases from many files then use command
#-k stands for method names execution ,-s logs in output ,-v stand for more info metadata
import pytest


@pytest.mark.smoke
def test_firstProgram():
   assert "Hi" == "Hello"


def test_credit_card():
   assert "abc" == "abc"
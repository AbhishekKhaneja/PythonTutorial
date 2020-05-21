import pytest

from PytestPackage.Baseloggerclass import baseLoggerclass


@pytest.mark.usefixtures("dataload")
class Testexample2(baseLoggerclass):


    def test_profile(self,dataload): # here method used only with print statement and it will not be reported in the report.html file
        print(dataload[0])
        print(dataload[1])
        print(dataload[2])

    def test_profile1(self,dataload): # here method used with log statement as we are extending the Baselogger class.so we canm use the logger to report the stuff in the Report.html file
        log = self.getlogger()
        log.info(dataload[0])
        log.info(dataload[1])
        log.info(dataload[2])

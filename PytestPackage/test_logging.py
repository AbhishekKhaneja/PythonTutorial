#pytest --html=report.html -v -s is the commmand to be used in the terminal to see the HTML report use this link for more info--https://pypi.org/project/pytest-html/
import logging


def test_loggingdemo():
    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('logfile.log') #defining in which file the logs has been reported
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s") # defining the format
    filehandler.setFormatter(formatter) #make a connection between findhandler and the formatter
    logger.addHandler(filehandler) #findhandler object # since logger is the object and filehandler knows about the log file details

    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("Information Statement")
    logger.warning("Something is in warning mode")
    logger.error("A error has occured")
    logger.critical("A critical issue is reported")


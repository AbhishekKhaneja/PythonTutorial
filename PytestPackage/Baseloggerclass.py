import inspect
import logging
#created this base logger class so that we can directly call tthis getlogger method and we can report in the Report.html file bascically logger is used here to get teh logs print in the report.html file

class baseLoggerclass():
    def getlogger(self):
        loggerName= inspect.stack()[1][3] # here it is used to get logs from where the execution is being called not from the baseclass in thsi particular scenario
        logger = logging.getLogger(loggerName)
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
        return logger


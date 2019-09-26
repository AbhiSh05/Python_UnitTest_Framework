import unittest
from TestScripts import TestClass1
from Utils import ExcelFunctions
from Utils import LogResults
from Utils import EmailReportCreation
from datetime import datetime

# Capturing start Time
Starttime= datetime.now()


#Creating a new Excel File to store fresh results
filename=ExcelFunctions.creatingFileForFirstTime()

# Initailizing Logger
LogResults.startLogger()

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(TestClass1))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

#Terminating Logger
LogResults.endLogger()

# Capturing End Time
Endtime= datetime.now()

#Creating Email Report
EmailReportCreation.EmailReport(Starttime,Endtime,"Example")


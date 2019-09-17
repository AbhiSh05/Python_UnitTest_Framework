import unittest
from ddt import ddt
from ddt import idata
from Utils import ExcelFunctions
from Utils import ConfigValues
from Utils import LogResults as logger

ModuleName='ModuleName1'

'''Files which are neccessary for validation from Objects Folder is imported here. '''
from Objects import Functions1

def dataProvider(testscriptname):
    testdata=ExcelFunctions.ReadingthroughTestData(ConfigValues.InputDataSheet,"InputSheet",testscriptname)
    for i in testdata:
        yield i

@ddt
class TestClass1(unittest.TestCase): # Class is inheritered from unittest.Testcase

    def setUp(self):
        # setUp Function always invoked before test case Function
        print("Setup Functionality")

    def tearDown(self):
        # tearDown Function is always invoked after testcase Function
        print("tearDown Functionality")

    @idata(dataProvider("test1"))
    def test1(self,number): # Sample Test Function
        testCase1 = ExcelFunctions.GettingTestCase(ModuleName, 'TC_01')
        try:
            logger.testCaseStart(testCase1)
            print("test1 function is executed")
            Step1="Results from Function is "+ str(Functions1.SquareNumber(number))
            Step2="Expected Results is "+ str(number*number)
            logger.addStepInfo(1,Step1)
            logger.addStepInfo(2,Step2)
            self.assertEqual(Functions1.SquareNumber(number),2*number*number,"Sqaure of Number is correct") # Assertion is required to validate any test case
            logger.passTestcase(testCase1)
        except AssertionError as e:
            logger.failTestCase(testCase1)
            logger.addStepInfo(3,str(e.args))
            print(e.args)
            raise
        finally:
            logger.testCaseEnd(testCase1)
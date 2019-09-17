import logging
from Utils import ConfigValues
from Utils import ExcelFunctions

def startLogger():
    logging.basicConfig(filename=ConfigValues.LogReport,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M:%S')
def endLogger():
    logging.shutdown()

def addStepInfo(StepNumber,StepInfo):
    logging.info('Step '+ str(StepNumber)+":- "+StepInfo)

def addWarning(WaringNumber,WarningInfo):
    logging.warning('Warning '+ str(WaringNumber)+":- "+WarningInfo)

def passTestcase(testCaseName):
    logging.info("Test case Passed")
    ExcelFunctions.makeEntryInExcelFile(testCaseName['ModuleName'],testCaseName['TestcaseID'],testCaseName['Description'],'Pass')

def failTestCase(testCaseName):
    logging.critical('Test Case Failed')
    ExcelFunctions.makeEntryInExcelFile(testCaseName['ModuleName'],testCaseName['TestcaseID'],testCaseName['Description'], 'Fail')

def testCaseStart(testcaseName):
    logging.info('======================================================================================================')
    logging.info("Test case ' "+testcaseName['ModuleName']+' :-'+testcaseName['TestcaseID']+" ' started")


def testCaseEnd(testcaseName):
    logging.info("Test case ' " + testcaseName['ModuleName']+' :-'+testcaseName['TestcaseID'] + " ' Ended")
    logging.info('======================================================================================================')
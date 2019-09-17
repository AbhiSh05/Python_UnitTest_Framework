from Utils import ConfigValues
from xlutils.copy import copy
# importing xlwt module
import xlwt
import xlrd

def creatingFileForFirstTime():
    workbook = xlwt.Workbook()

    sheet = workbook.add_sheet("Results")

    # Specifying style
    style = xlwt.easyxf('font: bold 1')

    # Specifying column
    sheet.write(0, 0, 'Module Name', style)
    sheet.write(0, 1, 'Test Case ID', style)
    sheet.write(0, 2, 'Description', style)
    sheet.write(0, 3, 'Status', style)
    workbook.save(ConfigValues.TestSummaryReport)

def makeEntryInExcelFile(ModuleName,TestCaseID,Description,Status):
    rb = xlrd.open_workbook(ConfigValues.TestSummaryReport,formatting_info=True)
    r_sheet = rb.sheet_by_index(0)
    r = r_sheet.nrows
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    sheet.write(r,0,ModuleName)
    sheet.write(r,1,TestCaseID)
    sheet.write(r,2,Description)
    sheet.write(r,3,Status)
    wb.save(ConfigValues.TestSummaryReport)


def ReadingthroughTestData(filepath,sheetname,testscriptname):
    wb = xlrd.open_workbook(filepath)
    sheet = wb.sheet_by_name(sheetname)

    listTestdata= []
    for i in range(sheet.nrows):
        #print(sheet.cell_value(0, i))
        if(sheet.cell_value(i,0)==testscriptname and sheet.cell_value(i,2).lower()=='y'):
            listTestdata.append(sheet.cell_value(i,1))

    return listTestdata

def GettingTestCase(modulename,TestCaseID):
    rb= xlrd.open_workbook(ConfigValues.TestcaseSheet)
    r_sheet= rb.sheet_by_name(modulename)
    testcase_dict={}
    for i in range(r_sheet.nrows):
        if(r_sheet.cell_value(i,0))==TestCaseID:
            testcase_dict.update({'ModuleName':modulename})
            testcase_dict.update({'TestcaseID':TestCaseID})
            testcase_dict.update({'Description':r_sheet.cell_value(i,1)})
            break
    return testcase_dict

def GetTestSummaryReportInfo():
    rb=xlrd.open_workbook(ConfigValues.TestSummaryReport)
    r_sheet=rb.sheet_by_index(0)
    list=[]
    for i in range(r_sheet.nrows):
        if r_sheet.cell_value(i,0)!='Module Name':
            new_dict={'TestCaseID':r_sheet.cell_value(i,1),'ModuleName':r_sheet.cell_value(i,0),'Description':r_sheet.cell_value(i,2),'Status':r_sheet.cell_value(i,3)}
            list.append(new_dict)
    return list
'''This file will create the Emailable Test Suite Report that can be used to trigger with Jenkins and sending it to Various StakeHolders'''

from Utils import ConfigValues
from Utils import ExcelFunctions


def EmailReport(startTime,EndTime, ModuleName):
    '''Fetching out the results of Test Execution'''
    SuiteStartTime= startTime.strftime("%d-%m-%Y %H:%M:%S")
    SuiteEndTime=EndTime.strftime("%d-%m-%Y %H:%M:%S")
    SuiteDuration=str(EndTime - startTime)
    GetTestSummaryReportInfo= ExcelFunctions.GetTestSummaryReportInfo()
    ApplicationName='Lumin'
    TotalTestCasesExceuted= 0
    PassTestCases=0
    FailTestCases=0
    ModuleName= ModuleName
    StringTable= ''
    for i,j in GetTestSummaryReportInfo.items():
        if( len(j)!=0 ):
            StringTable+="<tr><b><td colspan=3>"+str(i)+"</b></td></tr>"
            for k in j :
                TotalTestCasesExceuted+=1
                row='<tr><td>'+k['TestCaseID']+'</td><td>'+k['Description']+'</td><td>'+k['Status']+'</td></tr>'
                if k['Status']=='Pass':
                    PassTestCases+=1
                elif k['Status']=='Fail':
                    FailTestCases+=1
                StringTable+=row
    PassPercentage= (PassTestCases/TotalTestCasesExceuted)*100
    FailPercentae= (FailTestCases/TotalTestCasesExceuted)*100

    '''Now it will read the Sample Extent Mialable Report'''
    file= open(ConfigValues.EmailTemplate,'rt')
    value= file.read()

    '''Now we will replace the special tags with data'''
    new_value= value.replace('#APP',ApplicationName).replace('#MOD',ModuleName).replace('#STR',SuiteStartTime).replace('#END',SuiteEndTime).replace('#DUR',SuiteDuration).replace('#NO',str(TotalTestCasesExceuted)).replace('#PASS',str(PassTestCases)).replace('#PERCENTAGE1',str(PassPercentage)+"%").replace('#FAIL',str(FailTestCases)).replace('#PERCENTAGE2',str(FailPercentae)+"%").replace('#TABLE',StringTable)

    '''Now we will save the String new_value in new HTML report which can serve as the Jenkins Emailable Report'''
    write_file= open(ConfigValues.HTMLReport,'w')
    write_file.write(new_value)
    write_file.close()

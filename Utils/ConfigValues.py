'''This file will help you getting the values of Configuration Values saved in Config Files and we can use them throughout the Project'''

import configparser
from datetime import datetime
import os

now= datetime.now()
date_time = now.strftime("%m_%d_%Y_%H_%M_%S")

parentDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = configparser.RawConfigParser()
config.read(parentDir+'\Config\config.properties')

# VALUES
TestSummaryReport= parentDir+config.get('FILEPATHS','TestSummaryReport')+date_time+'.xls'
LogReport= parentDir+config.get('FILEPATHS','LogsFile')+date_time
InputDataSheet= parentDir+config.get('FILEPATHS','InputDataSheet')
TestcaseSheet=parentDir+config.get('FILEPATHS','TestCaseSheet')+".xls"
EmailTemplate= parentDir+config.get('FILEPATHS','EmailTemplate')
HTMLReport= parentDir+config.get('FILEPATHS','HTMLReport')


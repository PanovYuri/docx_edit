import pandas as pd 
import os

WORKING_DIRECTORY = os.getcwd()
SHEET_FILE = os.path.join(WORKING_DIRECTORY, 'data', 'data.xls')

x1 = pd.read_excel(SHEET_FILE)
print(x1.columns)

for i in x1.index:
    print(x1['Должность'][i])
    print(x1['Организация'][i])
    print(x1['Организация'][i])
    
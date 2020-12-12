import pandas as pd 
import os

WORKING_DIRECTORY = os.getcwd()
SHEET_FILE = os.path.join(WORKING_DIRECTORY, 'data', 'data.xls')

x1 = pd.ExcelFile(SHEET_FILE)
df = x1.parse(0)
print(df.head())
print(x1.sheet_names)
#!/usr/bin/env python
# coding: utf-8

#Module Name and Version
def module_version(mod):
    try:
        return print(mod.__name__ +' '+ mod.__version__ + ' imported.')
    except AttributeError:
        return print(mod.__name__ + ' imported.')

#Import modules
import platform
module_version(platform)
print('Version      :', platform.python_version())
print('Version tuple:', platform.python_version_tuple())
print('Compiler     :', platform.python_compiler())
print('Build        :', platform.python_build())
import os
module_version(os)
from pathlib import Path
module_version(Path)
import pandas as pd
module_version(pd)
import openpyxl
module_version(openpyxl)

my_repo = Path(os.getcwd())
data_repo = os.path.join(my_repo.parent, "Data")

#Import Excel and Create DataFrame
wb_file_name = 'weapons_inventory.xlsx'
wb_location = os.path.join(data_repo, wb_file_name)
wb = pd.ExcelFile(wb_location, engine = 'openpyxl')

sheet_num=0
tables = []
for sheet in wb.sheet_names:
    table = pd.read_excel(wb, sheet_name=sheet_num, index_col=None)
    tables.append(pd.DataFrame(data = table))
    sheet_num+=1
    
df = pd.concat(tables)

#Clean DataFrame
df.columns = ['Name', 'Type', 'Accuracy', 'Conceal', 'Avail', 'DamageAmmo', 'Shots', 'RoF', 'Reliability', 'Range', 'Cost', 'Book']
df['Cost'] = df['Cost'].map(lambda x: x.rstrip(' eb'))

def col_numeric(col):
    num_col = pd.Series(pd.to_numeric(col, downcast='float', errors = 'ignore'))
    col = num_col
    
col_numeric(df['Cost'])

col_numeric(df['Accuracy'])

col_numeric(df['Shots'])

col_numeric(df['RoF'])

#Split Damage and Ammo Columns
df[['Damage','Ammo']] = df["DamageAmmo"].str.split(" ",1,expand=True)
weapons_data = df
weapons_data.drop(['DamageAmmo'], axis = 1, inplace = True)
#After various API steps, integrate with python

import gspread

gc = gspread.service_account(filename=r"copy file path on pc")
sh = gc.open("First Project USID")
#to access sheet one, column one and row one on google spreadsheet
print(sh.sheet1.get('A1'))


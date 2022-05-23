#! python3
# dateCleaner.py - cleans dates into a standard format

import re, pyperclip

dates = []
def printEuDate(day,month,year):
    print(day+'/'+month+'/'+year)

def printAsiaDate(year,month,day):
    print(year+'/'+month+'/'+day)

copied_dates = pyperclip.paste()
us_date_re = re.compile(r'(0[1-9]|1[0-2])(-|.|/|\\)(0[1-9]|1[0-9]|2[0-9]|3[0-1])(-|.|/|\\)(\d){4}')
day = ''
result = us_date_re.search('12.29.1999')
if result != None:
    month = result.group()[0:2]
    day = result.group()[3:5]
    year = result.group()[6:]

printEuDate(day,month,year)
printAsiaDate(year,month,day)
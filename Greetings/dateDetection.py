#! python 3

#dateDetection.py - checks for correct dates

import re, pyperclip

def checkLeapYear(year):
    if(int(year) % 4 == 0.0 and int(year) % 100 != 0):
       return True
    elif(int(year) % 400 == 0):
       return False
    else:
       return False

copied_dates = pyperclip.paste()
us_date_re = re.compile(r'(0[1-9]|1[0-2])(-|.|/|\\)(0[1-9]|1[0-9]|2[0-9]|3[0-1])(-|.|/|\\)(\d){4}')
day = ''
result = us_date_re.search('02.29.1929')
if result != None:
    month = result.group()[0:2]
    day = result.group()[3:5]
    year = result.group()[6:]


if(month == '04' or month == '06' or month == '09' or month == '11'):
    if int(day) > 30:
        print('Incorrect day')
elif(month == '02'):
    if(checkLeapYear(year) == False):
        if(int(day) > 28):
            print('Too many days')
    else:
        if(int(day) > 29):
            print('Not a leap year')


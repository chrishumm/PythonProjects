#on every year that is evenly disvisiblre by 4 
#   except every year that is evenly disivislbe by 100 
#   unless the yeari s also evenly disvislbe by 400

import pyinputplus as pyin

def divisibleByFour(year):
    if(year % 4 == 0):
        return True
    else:
        return False
def divisibleByFourHundred(year):
    if(year % 400 == 0):
        return True
    else:
        return False

def divisibleByOneHundred(year):
    if(year % 100 == 0):
        return True
    else:
        return False

year = pyin.inputInt("Please enter a year between 0 and 10000: ", lessThan=10000 ,greaterThan=0)

if(divisibleByFour(year) == True):
    if(divisibleByOneHundred(year) == True):
        if(divisibleByFourHundred(year) == True):
            print("It is a leap year")
    else:
        print("It is a leap year.")
else:
    print("Not a leap year")


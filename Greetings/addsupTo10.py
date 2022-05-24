from logging import exception
import pyinputplus as pyip

def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
        
        sum_of_number = sum(map(int, numbersList))
        if sum_of_number != 10:
            raise exception('The digits must add up to 10, not %s.' %sum(map(int, numbersList)))
        else:
            print('It adds up to 10, congratulations!')
        return int(numbers)

response = pyip.inputCustom(addsUpToTen)

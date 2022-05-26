import pyinputplus as pyip


message = 'Want to know how to keep an idiot busy for a long time?\n'
while True:
    response = pyip.inputYesNo(message)
    if(response == 'no'):
        print('Have a nice day!')
        break
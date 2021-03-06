from cgitb import lookup
from operator import indexOf
from re import L

#Names are stored in lowercase
birthdays = {
    'mei' : 'May 10',
    'chris' : 'June 23',
    'anna' : 'August 10',
    'hanna' :'October 15'
}

valid_dates = ('January', 'February', 'March', 'April','May', 'June', 'July', 'August', 
                'September', 'October', 'November', 'December')

def listValues(birthday_list):
    for x, y in birthday_list.items(): #Printing multiple values from a dictionary
        print('Key: ' + str(x) + ' Value: ' + str(y))

while True:
    print('(Enter a name, (a)dd a new name or (q)uit')
    lookup_name = input()
    if(lookup_name == 'q'):
        break
    elif(lookup_name == 'l'):
        listValues(birthdays)
    else:
        if lookup_name.lower() in birthdays.keys():
            print(lookup_name[0].upper() + lookup_name[1:] + "'s birthday is on " + birthdays[lookup_name.lower()])
        else:
            print("I don't have birthday information for " + lookup_name + '.')
            print("What is their birthay?")
            birthday_date = input()
            birthday_date[0].upper()
            if(birthday_date[:birthday_date.index(' ')] not in valid_dates):
                print("Not a valid date")
            else:
                birthdays[lookup_name.lower()] = birthday_date
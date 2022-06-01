#! python3
# phoneEmailExtractor.py - Extracts phone numbers and emails.

import pyperclip, re

copied_text = pyperclip.paste()
emailRe = re.compile(r'[a-z0-9]+@\w+\.[a-z]{2,3}', re.IGNORECASE)
numbers = re.compile(r'[\+]?[44]?\d{8,10}', re.VERBOSE)
list_of_emails = emailRe.findall(copied_text)
list_of_phone_numbers = numbers.findall(copied_text)
matches = []
matches.append('List of Emails: ')
for count in range(len(list_of_emails)):
    matches.append(list_of_emails[count])

matches.append('List of Phone Numbers: ')

for count in range(len(list_of_phone_numbers)):
    phoneNum = list_of_phone_numbers[count]
    if phoneNum[:3] == '+44':
        phoneNum = ('0' + phoneNum[3:])
        matches.append(phoneNum)
    else:
            matches.append(list_of_phone_numbers[count])



'''
'''


if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied!')
    print('\n'.join(matches))
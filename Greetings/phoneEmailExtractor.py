import pyperclip, re

copied_text = pyperclip.paste()
emailRe = re.compile(r'[a-z0-9]+@\w+\.[a-z]{2,3}', re.IGNORECASE)
numbers = re.compile(r'[\+]?[44]?\d{8,10}', re.VERBOSE)
list_of_emails = emailRe.findall(copied_text)
list_of_phone_numbers = numbers.findall(copied_text)
print('List of Emails:')
for count in range(len(list_of_emails)):
    print(list_of_emails[count] + '\n')

print('List of phone numbers')

for count in range(len(list_of_phone_numbers)):
    print(list_of_phone_numbers[count] + '\n')
'''8 Eastern Way
Milford on Sea
LYMINGTON
SO41 0TB
'''
#! python3
# strongPasswordProtection.py - checks password strength

import pyperclip, re

copied_password = pyperclip.paste()
passwordStrengthRegex = re.compile(r'(\w*\d+\w*)[A-Z]{1,}.*')
try:
    password = passwordStrengthRegex.search('qf4d34ffrfs').group()
    if(len(password) < 8):
        print('Your password is too short')
except:
        print('''Please enter a number  or capital letter 
                for your password''')

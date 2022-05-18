#! python3
# passwordManager.py -- An insecure commandline password manager

PASSWORDS = {'email': 'cisco123',
             'blog': 'test123',
             'ig': 'ig123'}

from operator import indexOf
import sys, pyperclip

def addAccount(account):
    print('Please add a password')
    password = input()
    PASSWORDS2.setdefault(account, password)
    with open('passwords.txt', 'a') as x:
            x.write(account +':' + password +'\n')

with open('passwords.txt', 'r') as x:
        my_lines = x.read()
        new_list = my_lines.splitlines()



PASSWORDS2 = {}
for count, read_passwords in enumerate(new_list):
    try:
        PASSWORDS2.setdefault(read_passwords[:read_passwords.index(':')],read_passwords[read_passwords.index(':')+1:])
    except:
        print('Password file is corrupted')

if len(sys.argv) < 3:
    print('Usage: py passwordManager.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name
masterPassword = sys.argv[2]
if(masterPassword != 'pingas'):
    print('PINGAS')
    exit

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
    print('You can (a)dd the account or (q)uit')
    response = input()
    addAccount(account)
    



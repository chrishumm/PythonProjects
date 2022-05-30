#! python3
# mcb.pyw - a better copy/paste tool
#
# Usage: py.exe mcb.pyw save <keywords> - saves clipboard to keyword
#        py.exe mcb.pyw <keyword>  - copies the keyword into clipboard
#        py.exe mcb.pyw list - list all saved keywords and values
import pyperclip, shelve, sys

mcbShelf = shelve.open('mbc')

if len(sys.argv) == 3 and sys.argv[1] == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(mcbShelf[sys.argv[2]] + ' saved')


elif(len(sys.argv) == 2):
    if(sys.argv[1].lower() == 'list'):
        pyperclip.copy(str(list(mcbShelf.keys())))
        print()
    elif(sys.argv[1] in mcbShelf):
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

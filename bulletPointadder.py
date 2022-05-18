#! python3
# bulletPointAdder.py - Adds bullet points to lines
import pyperclip
text = pyperclip.paste()

#Splits text into lines and inserts into a list
#Adds formatting
split_text = text.splitlines()
for count, value in enumerate(split_text):
    split_text[count] = '* ' + value #+ '\n'

#Createa a string from a list of strings    
text = ''
#text = text.join(value for value in split_text)
text = '\n'.join(split_text)
pyperclip.copy(text)


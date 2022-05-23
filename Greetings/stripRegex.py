#! python3
# stripRegex.py - a regex version of the strip() function
import re, pyperclip

word = pyperclip.paste()
stripRegex = re.compile(rf'\s*|\s*$')
output = re.sub(stripRegex, "",word)
print(output)

#removes all spaces with re.sub
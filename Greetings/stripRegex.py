#! python3
# stripRegex.py - a regex version of the strip() function
import re, pyperclip

def striptheword(word, word_to_strip):
    if(word_to_strip == None):
        word_to_strip = "\s"
    stripRegex = re.compile(rf'{word_to_strip}*|{word_to_strip}*$')
    output = re.sub(stripRegex, "",word)

    return output

word = pyperclip.paste()
print("Input regex, number or letter to strip")
strip_this = input()
print(striptheword(word, strip_this))

#removes all spaces with re.sub
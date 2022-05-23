#! python3
# httpCleaner.py - turns unsecure http into https from clipboard

import re, pyperclip

copiedText = pyperclip.paste()
httpCleanerRe = re.compile(r'[http]\w+')
result = httpCleanerRe.sub('https',copiedText)
print(result)
pyperclip.copy(result)
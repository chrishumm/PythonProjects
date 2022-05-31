import re, os
from pathlib import Path


current_directory = Path.cwd()

print('Input a regex string search\n')
user_regex = input()
regex_search = re.compile(user_regex, re.IGNORECASE)

list_of_text_files = list(current_directory.glob('*.txt'))

for x,y in enumerate(list_of_text_files):
    print('Searching file ' + os.path.basename(list_of_text_files[x]))

    opened_file = open(os.path.basename(list_of_text_files[x]))
    file_contents = opened_file.read()
    if(regex_search.search(file_contents) != None):
        print('Found in  ' + os.path.basename(list_of_text_files[x]))
    opened_file.close()
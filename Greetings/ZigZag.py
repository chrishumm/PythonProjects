from mimetypes import inited
import time, sys
## Initial setup for variables
indent = 0 # How many spaces to indent.
max_indent = 20
increaseIndent = True # Whether the indentation is increasing or not.
output_length = 10
output_speed = 0.1

## Menu for customising the line
print("Enter any character")
output_result = input()[0]
print("Do you want (f)ast, (n)ormal or (s)low?")
if(input() == 'f'):
    output_speed = 0.05
elif(input() == 'n'):
    output_speed = 0.1
elif((input) == 's'):
    output_speed = 0.2
else:
    output_speed = 0.1

## Defining the two main functions    
def printOutput():
        print(' ' * indent, end='')
        print(output_result * output_length) #print the character times by the length
        time.sleep(output_speed)

## Main loop
try:
    while True: # The main program loo
        printOutput()
        if increaseIndent:
            # Increase the number of spaces:
         indent += 1
         if indent == max_indent:
                # Change direction:
               increaseIndent = False
        else:
            # Decrease the number of spaces:
            indent -= 1
            if indent == 0:
                # Change direction:
                increaseIndent = True
except KeyboardInterrupt:
    sys.exit()
import random
import sys

for i in range(100):
 print(random.randint(1, 100))

while True:
    print("Please type exit")
    response = input()
    if response == "exit" or response == "Exit":
     sys.exit()
    else:
        print("You typed " + response+ "! Please type exit")

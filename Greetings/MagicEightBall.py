import random

def getAnswer(eightballNumber):
    if(eightballNumber == 1):
        return "It is certain"
    elif(eightballNumber == 2):
        return "It is decidedly so"
    elif(eightballNumber == 3):
        return "Yes"
    elif(eightballNumber == 4):
        return "Reply hazy try again"
    elif(eightballNumber == 5):
        return "Ask again later"
    elif(eightballNumber == 6):
        return "Concentrate and ask again"
    elif(eightballNumber == 7):
        return "My reply is no"
    elif(eightballNumber == 8):
        return "Outlook not so good"
    elif(eightballNumber == 9):
        return "Very doubtful"
    else:
        print("How did you get that number")

while True:
    print("Write your question and ask the magic eightball or (q)uit")

    input_response = input()
    if(input_response == "q" or input_response == "Q"):
        break

    print(getAnswer(random.randint(1,9)))
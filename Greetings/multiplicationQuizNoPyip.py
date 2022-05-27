import random, time, re, sys

noOfQuestions = 10
correctAnswers = 0
def inputString(typed_input, number_1, number_2):
    if re.compile(r'[0-9]+').search(typed_input) == None:
        print('Not a valid input')
        return False
    allowedRegex = re.compile(r'^%s$' %(number_1*number_2))
    if(allowedRegex.search(typed_input) != None):
        print(typed_input + ' it worked')
        return True
    else:
        print('Incorrect try again!')
        return False

def gameOver(correctAnsers, noOfquestions):
    print('You scored: %s questions correctly out of %s' % (correctAnswers, noOfQuestions))
    sys.exit()

def checkTime(start_time, end_time):
    if end_time - start_time >= 10:
        return True
    else:
        return False


for questionNumber in range(noOfQuestions):
    number_1 = random.randint(0, 9)
    number_2 = random.randint(0, 9)
    incorrect_response = 4
    prompt = 'Question %s# %s x %s = ' %(questionNumber+1, number_1, number_2)
    start_time = time.time()
    while True:
        print(prompt)
        response = input()
        if(inputString(response,number_1, number_2) == True):
            end_time = time.time()
            if checkTime(start_time, end_time) == False:
                correctAnswers += 1
            else:
                print('Time over!')
                gameOver(correctAnswers, noOfQuestions)
            break
        else:
            end_time = time.time()
            if checkTime(start_time, end_time) == True:
                gameOver(correctAnswers, noOfQuestions)

            incorrect_response -=1
            if(incorrect_response <= 0):
                gameOver(correctAnswers, noOfQuestions)
            print('You have %s tries left' %(incorrect_response))

    time.sleep(1)

gameOver(correctAnswers, noOfQuestions)

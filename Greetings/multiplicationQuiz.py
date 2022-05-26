import pyinputplus as pyip
import random, time

noOfQuestions = 10
correctAnswers = 0


for questionNumber in range(noOfQuestions):
    number_1 = random.randint(0, 9)
    number_2 = random.randint(0, 9)

    prompt = 'Question %s# %s x %s = ' %(questionNumber+1, number_1, number_2)
    try:
        pyip.inputStr(prompt, allowRegexes=[r'^%s$' %(number_1*number_2),], blockRegexes=[r'.*','Incorrect'],timeout=8,limit=3)

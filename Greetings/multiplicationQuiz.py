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
    except pyip.TimeoutException:
        print('Out of time! You answered %s correct questions' %(correctAnswers))
        break
    except pyip.RetryLimitException:
        print('Out of tries! You answered %s correct questions' %(correctAnswers))
        break
    else:
        correctAnswers +=1
        print('Correct, you have %s correct answers' % (correctAnswers))

    time.sleep(1)

print('Result   : %s / %s' % (correctAnswers, noOfQuestions))


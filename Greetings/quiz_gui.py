#! python3
# quiz_gui.py - true or false game written in tkinter

import tkinter as tk
import tkinter.font as tkFont
import re
import random
#add later include mp3cd 
#from playsound import playsound
app = tk.Tk()
app.geometry("400x200")

app.title("Countdown Quiz | Created by Chris Humm")
app.config(bg='white')



counter = 5.0

def readQuestions():
   question = {}
   question_regex = re.compile(r"^[^:]*")
   answer_regex = re.compile(r"[:]\w+")

   try:
      with open('questions.txt', 'r') as question_file:
         question_list = question_file.readlines()
         test= question_regex.search(question_list[0]).group()
         for x, y in enumerate(question_list):
            question.update({question_regex.search(question_list[x]).group(): answer_regex.search(question_list[x]).group()[1:]})
         
         question_file.close()
   except:
      helloFile = open('questions.txt', 'w')
      helloFile.write("London is the capital of England:true\nDogs can swim:true\nPigs can fly:false\n")
      helloFile.close()
      question = readQuestions()
   
   return question

question = readQuestions()
def counter_label(label):
  def count():
    global counter
    if(counter <= 0.0):
        label.config(fg='red', text='TIME OUT')
        counter = 0.0
    else:
        counter -= 0.1
        label.config(text=str(counter)[:3])
        label.after(100, count)


  count()
def checkAnswer(questionLabel, answerTally, user_response):
  if(len(question) == 0):
     print('No more questions')
     return

  global correctAnswers
  global inCorrectAnswers
  global counter



  if list(question.values())[0] == 'true' and user_response == 'true':
     print('Correct answer!') 
     correctAnswers+= 1
     answerTally.config(text='Correct Answers: %s\nIncorrect Answers: %s' %(correctAnswers,inCorrectAnswers) , fg='green')
     #PlaySound("correct.wav")
  elif list(question.values())[0] == 'false' and user_response == 'false':
     print('Correct answer!') 
     correctAnswers+= 1
     answerTally.config(text='Correct Answers: %s\nIncorrect Answers: %s' %(correctAnswers,inCorrectAnswers) , fg='green')
     #PlaySound("correct.wav")
  else:
     inCorrectAnswers+=1
     answerTally.config(text='Correct Answers: %s\nIncorrect Answers: %s' %(correctAnswers,inCorrectAnswers) , fg='green')
     print('Incorrect answer!')
     #PlaySound("incorrect.wav")
     
  question.pop(list(question.keys())[0])
  questionLabel.config(text=list(question.keys())[0])


questionLabel = tk.Label(app, text=list(question.keys())[0])
questionLabel.pack()

correctAnswers = 0
inCorrectAnswers = 0

answerTally = tk.Label(app, text='Correct Answers: %s\nIncorrect Answers: %s' %(correctAnswers,inCorrectAnswers))
answerTally.pack()

trueButton = tk.Button(app,
                           text="TRUE",
                           width=10,
                           height=10,
                           command= lambda: checkAnswer(questionLabel,answerTally,"true"))
falsebutton = tk.Button(app,
                           text="FALSE",
                           width=10,
                           height=10,
                           command= lambda: checkAnswer(questionLabel,answerTally,"false"))

trueButton.pack(side=tk.LEFT)
falsebutton.pack(side=tk.RIGHT)

label = tk.Label(app, fg="green")
label.pack()
counter_label(label)


app.mainloop()

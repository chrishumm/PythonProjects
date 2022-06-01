
from tabnanny import check
import tkinter as tk
import tkinter.font as tkFont
    
app = tk.Tk()
app.geometry("400x200")

app.title("Countdown Quiz | Created by Chris Humm")
app.config(bg='white')

question = {'Border Collies are dogs': 'true', 'My name is Chris' :'true', 'My girlfriend is called Mei' : 'true'}

counter = 10.0

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
def checkAnswerTrue(questionNumber, questionLabel, answerTally):
  question.pop(list(question.keys())[questionNumber])
  questionLabel.config(text=list(question.keys())[0])
  global correctAnswers
  if list(question.values())[questionNumber] == 'true':
     print('Correct answer!') 
     correctAnswers+= 1
     answerTally.config(text='Correct Answers: %s' %correctAnswers, fg='green')

  else:
     print('Incorrect answer!')


def checkAnswerFalse(questionNumber):
   if list(question.values())[questionNumber] == 'false':
       print('Correct answer!')
   else:
       print('Incorrect answer!')

       question.pop(list(question.keys())[questionNumber])
       questionLabel.config(text=list(question.keys())[0])

questionLabel = tk.Label(app, text=list(question.keys())[0])
questionLabel.pack()

correctAnswers = 0
answerTally = tk.Label(app, text='Correct Answers: %s' %correctAnswers)
answerTally.pack()
trueButton = tk.Button(app,
                           text="TRUE",
                           width=10,
                           height=10,
                           command= lambda: checkAnswerTrue(0, questionLabel,answerTally))
falsebutton = tk.Button(app,
                           text="FALSE",
                           width=10,
                           height=10,
                           command= lambda: checkAnswerTrue(0, questionLabel))

trueButton.pack(side=tk.LEFT)
falsebutton.pack(side=tk.RIGHT)

label = tk.Label(app, fg="green")
label.pack()
counter_label(label)


app.mainloop()

from re import T
from question import Question
from data import question_data
import pyinputplus as pyin
import os



question_bank = [None] * len(question_data)
for i, value in enumerate(question_data):
    question_bank[i] = Question(value['question'], value['correct_answer'])
class QuestionBrain():
    def __init__(self,q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        pass
    
    def stillHasQuestion(self):
        if self.question_number != len(self.question_list):
            return True
        else:
            return False
    def checkAnswer(self, user_answer : bool):
        if self.question_list[self.question_number].getAnswer() == str(user_answer):
            print("Well Done!")
            self.score += 1
        else:
            self.cls()
            print(f"Uh-oh, the correct answer was {str(self.question_list[self.question_number].getAnswer())}")

        print(f"Your score is currently {self.getScore()} / {self.question_number+1}\n\n")
    def nextQuestion(self):
        answer = pyin.inputBool(f"Q{self.question_number+1} "+ self.question_list[self.question_number].getQuestion() +" (True/False)")
        self.checkAnswer(answer)
        self.question_number+=1

    def getScore(self):
        return self.score

    def cls(self):
        """Clears the screen depending on the OS"""
        # for mac and linux(here, os.name is 'posix')
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            # for windows platform os.system = "nt"
            _ = os.system('cls')

print("test")

questionBrain = QuestionBrain(question_bank)

while questionBrain.stillHasQuestion():
    questionBrain.nextQuestion()

print(f"\nYou scored {questionBrain.getScore()} / {len(question_data)}")
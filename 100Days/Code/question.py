class Question():
    def __init__(self, question_text, question_answer) -> None:
        self._question = question_text
        self._answer = question_answer
        pass

    def getQuestion(self):
        return self._question

    def getAnswer(self):
        return self._answer
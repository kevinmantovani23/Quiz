class QuizBrain:

    def __init__(self, qB):
        self.question_number = 0
        self.question_list = qB
        self.score = 0

    def still_have_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        question_answer = input(f"Q.{self.question_number}: {question.texto} (True/False)?: ")
        if question.resposta == 'True':
            if question_answer[0] == 'T' or question_answer[0] == 't':
                self.score += 1
                print(f'Correct answer, current score: {self.score}/{len(self.question_list)}')
            else:
                print(f'Wrong answer, current score: {self.score}/{len(self.question_list)}')
        else:
            if question_answer[0] == 'F' or question_answer[0] == 'f':
                self.score += 1
                print(f'Correct answer, current score: {self.score}/{len(self.question_list)}')
            else:
                print(f'Wrong answer, current score: {self.score}/{len(self.question_list)}')

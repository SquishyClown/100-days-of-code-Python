class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.tscore = 0


    def still_has_questions(self):
        dlugosc = len(self.question_list)
        if(self.question_number == dlugosc):
            return False
        else:
            return True


    def NextQuestion(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number} {current_question.text} (True/False)")
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_ans, correct_answer):
        if(user_ans.lower() == correct_answer.lower()):
            print("You got it right")
            self.score += 1
            self.tscore += 1
            print(f"Your current score is: {self.score}/{self.tscore}")
        else:
            print("That's wrong")
            self.tscore += 1
            print(f"Your current score is: {self.score}/{self.tscore}")
        print(f"The correct answer was: {correct_answer}.")
        print("")





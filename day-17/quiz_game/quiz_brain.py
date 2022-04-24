class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        curreten_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {curreten_question.text} (True/False)? ")
        self.checking_answer(user_answer, curreten_question.answer)

    def checking_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right. Next answer.")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}. \nYour score is {self.score}/{self.question_number}.")
        print("\n")
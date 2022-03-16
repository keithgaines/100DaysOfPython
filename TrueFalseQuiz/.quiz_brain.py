class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    # if question number less than number of questions on the question list, returns true. 
    def still_has_questions(self):
            return self.question_number < len(self.question_list)

    # asks the next question and calls check_answer to check the answer
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}: {current_question.text}. (True/False)? ")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        """Checks user answer against the correct answer"""
        # converts user answer and correct answer to lowercase, then compares them
        # if user answer correct, adds one to user score
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct_answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}\n") 
       
        
        # displays final score once all questions have been asked
        if self.question_number == len(self.question_list):
            print(f"Your final score is {self.score}/{self.question_number}")
            input("Press any key to end program...")


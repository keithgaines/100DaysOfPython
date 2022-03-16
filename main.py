from operator import truediv
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# assigns text from question_data list/nested dictionary entry to question_text variable
# assigns answer from question_data list/nested dictionary entry to question_answer variable
# assigns both of those parameters to new_question variable
# adds new_question to question_bank list
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.still_has_questions = True

while quiz.still_has_questions == True:
    quiz.next_question()










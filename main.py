from question_model import Question
from data import question_data
# new_q = Question("name", "young")
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("You completed the score")
print(f"Your final score was {quiz.score}/{len(quiz.q_list)}")









# class User:
#     def __init__(self, user_id, user_unsername):
#         self.id = user_id
#         self.unsername = user_unsername
#         self.followers = 0
#         self.following = 0
#
#     def following (self, user):
#         user.followers += 1
#         self.following += 1
#
#
# usre_1 = User("001","Marcin")
#
# print(usre_1.unsername)
#
#

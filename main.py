import random

#give your questions attributes
class MultipleChoiceQuestion:
    def __init__(self, question, options, correct_answer, explanation):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation

#display questions of the quizes with the index and the actual options
    def display_question(self):
        print(self.question)
        for idx, option in enumerate(self.options):
            print(f"{idx + 1}. {option}")
        print()
#check if the answer is correct
    def check_answer(self, user_answer):
        return self.options[user_answer - 1] == self.correct_answer


# Creating the full quiz with randomly shuffle the questions. At the end of the quiz the all of correct and incorrect
# will be displayed with the total amount of correct score and the explaination
def administer_quiz(questions):
    random.shuffle(questions)  # Shuffle the questions
    score = 0
    total_questions = len(questions)
    responses = []  # Store user responses

    for idx, question in enumerate(questions, start=1):
        print(f"Question {idx}/{total_questions}:")
        question.display_question()
        user_answer = int(input("Enter your answer (1, 2, 3, etc.): "))
        responses.append((question, user_answer))
        if question.check_answer(user_answer):
            score += 1


    print("Quiz Results:")
    print(f"You scored {score} out of {total_questions}.\n")

    print("Correct answers:")
    for idx, (question, user_answer) in enumerate(responses, start=1):
        if question.check_answer(user_answer):
            print(f"{idx}. {question.question}")
            print(f"   Your answer: {question.options[user_answer - 1]}")
            print(f"   Explanation: {question.explanation}\n")

    print("Incorrect answers:")
    for idx, (question, user_answer) in enumerate(responses, start=1):
        if not question.check_answer(user_answer):
            print(f"{idx}. {question.question}")
            print(f"   Your answer: {question.options[user_answer - 1]}")
            print(f"   Correct answer: {question.correct_answer}")
            print(f"   Explanation: {question.explanation}\n")


# Define your questions here
questions = [
    MultipleChoiceQuestion(
        "What is the capital of France?",
        ["Paris", "London", "Berlin", "Rome"],
        "Paris",
        "Paris is the capital of France."
    ),
    MultipleChoiceQuestion(
        "Who wrote 'Romeo and Juliet'?",
        ["William Shakespeare", "Charles Dickens", "Jane Austen", "F. Scott Fitzgerald"],
        "William Shakespeare",
        "William Shakespeare wrote 'Romeo and Juliet'."
    ),
    MultipleChoiceQuestion(
        "What is the powerhouse of the cell?",
        ["Mitochondrion", "Nucleus", "Ribosome", "Endoplasmic reticulum"],
        "Mitochondrion",
        "Mitochondrion is often referred to as the powerhouse of the cell because it produces energy in the form of ATP."
    )
]

# Administer the quiz
administer_quiz(questions)

























import random
import json

# Define the MultipleChoiceQuestion class
class MultipleChoiceQuestion:
    def __init__(self, question, options, correct_answers, explanation, multi_answer=False):
        self.question = question
        self.options = options
        self.correct_answers = correct_answers  # A list of correct answers
        self.explanation = explanation
        self.multi_answer = multi_answer  # Whether this question requires multiple correct answers

    # Display the question with options
    def display_question(self):
        print(self.question)
        for idx, option in enumerate(self.options):
            print(f"{idx + 1}. {option}")
        print()

    # Check if the user's answers are correct (handle single or multi-answer questions)
    def check_answer(self, user_answers):
        if self.multi_answer:
            return set(self.correct_answers) == set(user_answers)
        else:
            return self.options[user_answers[0] - 1] == self.correct_answers[0]

# Function to load questions from a JSON file
def load_questions_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)  # Load the JSON data

    questions = []
    for item in data:
        question = MultipleChoiceQuestion(
            question=item['question'],
            options=item['options'],
            correct_answers=item['correct_answers'],
            explanation=item['explanation'],
            multi_answer=item.get('multi_answer', False)
        )
        questions.append(question)

    return questions

# Function to administer the quiz
def administer_quiz(questions):
    random.shuffle(questions)  # Shuffle the questions
    score = 0
    total_questions = len(questions)
    responses = []  # Store user responses

    for idx, question in enumerate(questions, start=1):
        print(f"\nQuestion {idx}/{total_questions}:")
        question.display_question()

        # For multi-answer questions, allow the user to input multiple answers
        if question.multi_answer:
            print(f"This question requires multiple answers. Enter all correct answers (e.g., 1 2 3):")
            while True:
                try:
                    user_input = input("Enter your answers (space-separated numbers): ").split()
                    user_answers = [int(ans) for ans in user_input if ans.isdigit()]
                    if all(1 <= ans <= len(question.options) for ans in user_answers):
                        break
                    else:
                        print(f"Please enter valid numbers between 1 and {len(question.options)}.")
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")
        else:
            while True:
                try:
                    user_answer = int(input("Enter your answer (1, 2, 3, etc.): "))
                    if 1 <= user_answer <= len(question.options):
                        user_answers = [user_answer]  # Store answer in a list for consistency
                        break
                    else:
                        print(f"Please enter a number between 1 and {len(question.options)}.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        responses.append((question, user_answers))

        if question.check_answer(user_answers):
            score += 1

    # Display results
    print("\n--- Quiz Results ---")
    print(f"You scored {score} out of {total_questions}.\n")

    if score == total_questions:
        print("Congratulations! You answered all questions correctly!\n")
    else:
        print("Correct answers:")
        for idx, (question, user_answers) in enumerate(responses, start=1):
            if question.check_answer(user_answers):
                print(f"{idx}. {question.question}")
                print(f"   Your answer: {[question.options[ans - 1] for ans in user_answers]}")
                print(f"   Explanation: {question.explanation}\n")

        print("Incorrect answers:")
        for idx, (question, user_answers) in enumerate(responses, start=1):
            if not question.check_answer(user_answers):
                print(f"{idx}. {question.question}")
                print(f"   Your answer: {[question.options[ans - 1] for ans in user_answers]}")
                print(f"   Correct answers: {[question.options[question.options.index(ans)] for ans in question.correct_answers]}")
                print(f"   Explanation: {question.explanation}\n")

# Main loop to administer quiz multiple times if the user wants to retake it
def main():
    filename = "questions.json"  # Path to your JSON file
    questions = load_questions_from_file(filename)

    while True:
        administer_quiz(questions)
        play_again = input("Do you want to retake the quiz? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

# Run the main function to start the quiz
if __name__ == "__main__":
    main()

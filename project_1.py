def display_question(question, options):
    """Display a multiple-choice question."""
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

def get_user_answer(options):
    """Get and validate user's answer."""
    while True:
        user_input = input("Your answer (enter the  option number): ").strip()
        if user_input.isdigit() and 1 <= int(user_input) <= len(options):
            return int(user_input) - 1
        else:
            print("Invalid input. Please enter a number corresponding to the options.")

def check_answer(user_answer, correct_answer):
    """Check if the user's answer is correct."""
    return user_answer == correct_answer

def run_quiz(questions):
    """Run the quiz with provided questions and options."""
    score = 0
    for q_number, q_data in enumerate(questions, start=1):
        print(f"\nQuestion {q_number}:")
        display_question(q_data["question"], q_data["options"])
        user_answer = get_user_answer(q_data["options"])
        if check_answer(user_answer, q_data["correct_index"]):
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer is:", q_data["options"][q_data["correct_index"]])
    return score

def main():
    # Define the questions and options
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_index": 0
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Blue whale", "Giraffe", "Hippopotamus"],
            "correct_index": 1
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "correct_index": 1
        }
    ]

    # Run the quiz
    score = run_quiz(questions)

    # Display final score
    print("\nQuiz completed! Your score is:", score, "out of", len(questions))

if __name__ == "__main__":
    main()
  

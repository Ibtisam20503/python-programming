import random

def ask_questions():
    questions = [
        ("What is your name?", "name"),
        ("How old are you?", "age"),
        ("What is your favorite color?", "color"),
        ("What is your favorite food?", "food"),
        ("Which city do you live in?", "city"),
        ("Which SHS did you attend?", "shs"),
        ("What is your favorite soccer team?", "team")
    ]

    # Shuffle questions for bonus marks
    random.shuffle(questions)

    answers = {}

    for q_text, key in questions:
        answer = input(q_text + " ")
        answers[key] = answer

    return answers

def create_summary(data):
    return (
        f"\nHello, {data['name']}!\n"
        f"You are {data['age']} years old, love the color {data['color']}, and enjoy eating {data['food']}.\n"
        f"You live in {data['city']}, went to {data['shs']}, and support {data['team']}.\n"
        f"Sounds like an awesome life!\n"
    )

def save_to_file(data, summary, rating):
    filename = f"{data['name']}.txt"
    with open(filename, "w") as f:
        f.write(summary)
        f.write(f"\nUser rating: {rating} star(s)\n")
    print(f"Summary saved to {filename}")

def main():
    while True:
        user_data = ask_questions()
        summary = create_summary(user_data)
        print(summary)

        save = input("Would you like to save this summary to a file? (yes/no): ").lower()
        if save == "yes":
            while True:
                try:
                    rating = int(input("Please rate the assistant (1 to 5 stars): "))
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("Rating must be between 1 and 5.")
                except ValueError:
                    print("Please enter a number.")

            save_to_file(user_data, summary, rating)

        restart = input("Would you like to restart and enter new info? (yes/no): ").lower()
        if restart != "yes":
            print("Goodbye!")
            break

if _name_ == "_main_":
    main()
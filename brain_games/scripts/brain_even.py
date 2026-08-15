import random
from brain_games.cli import welcome_user


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_even(number) else "no"
    question = f"Question: {number}"
    return correct_answer, question

def start_game():

    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_count = 0
    rounds_to_win = 3

    while correct_count < rounds_to_win:
        correct_answer, question = get_question_and_answer()
        print(question)

        user_answer = input("Your answer: ").strip().lower()

        if user_answer == correct_answer:
            print("Correct!")
            correct_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    start_game()


if __name__ == '__main__':
    main()

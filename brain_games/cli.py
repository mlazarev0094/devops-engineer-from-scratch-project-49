import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def get_user_unswer():
    return input("Your answer: ").strip().lower()


def display_correct():
    print("Correct!")


def display_wrong(user_answer, correct_answer, name):
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")

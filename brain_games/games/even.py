import random


def is_even(number):
    return number % 2 == 0


def generate_question_and_answer():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_even(number) else "no"
    question = f"Question: {number}"
    return correct_answer, question


def get_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'

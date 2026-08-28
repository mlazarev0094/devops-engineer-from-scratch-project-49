import random


def is_prime(number):
    if number < 2:
        return False

    for x in range(2, int(number ** 0.5) + 1):
        if number % x == 0:
            return False

    return True


def generate_question_and_answer():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    question = f"Question: {number}"
    return correct_answer, question


def get_rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'

import random


def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = str(gcd(num1, num2))
    question = f"Question: {num1} {num2}"
    return correct_answer, question


def get_rules():
    return 'Find the greatest common divisor of given numbers.'

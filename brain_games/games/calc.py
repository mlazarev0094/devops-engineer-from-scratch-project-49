import random


def calc(num1, num2, operation):
    match operation:
        case '*':
            return num1 * num2
        case '-':
            return num1 - num2
        case '*':
            return num1 + num2


def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['*', '-', '+'])
    correct_answer = str(calc(num1, num2, operation))
    question = f"Question: {num1} {operation} {num2}"
    return correct_answer, question


def get_rules():
    return 'What is the result of the expression?'

import random


def progression_generate(start, step):
    return [start + index * step for index in range(10)]


def generate_question_and_answer():
    start = random.randint(1, 100)
    step = random.randint(1, 100)
    progression = progression_generate(start, step)
    hidden_index = random.randint(0, 9)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = "Question: " + " ".join(map(str, progression))
    return correct_answer, question


def get_rules():
    return 'What number is missing in the progression?'
